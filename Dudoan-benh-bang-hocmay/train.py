# Thêm các thư viện cần thiết
import yaml
from joblib import dump, load
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import seaborn as sn
import matplotlib.pyplot as plt

class DuDoanBenhLy:
    # Khởi tạo và tải file cấu hình
    def __init__(self, ten_mo_hinh=None):
        # Tải file cấu hình
        try:
            with open('./config.yaml', 'r') as f:
                self.config = yaml.safe_load(f)
        except Exception as e:
            print("Lỗi khi đọc file cấu hình...")

        # Cài đặt chế độ chi tiết
        self.verbose = self.config['verbose']
        # Tải dữ liệu huấn luyện
        self.train_features, self.train_labels, self.train_df = self._load_train_dataset()
        # Tải dữ liệu kiểm tra
        self.test_features, self.test_labels, self.test_df = self._load_test_dataset()
        # Phân tích tương quan các đặc trưng trong dữ liệu huấn luyện
        self._feature_correlation(data_frame=self.train_df, show_fig=False)
        # Định nghĩa mô hình
        self.ten_mo_hinh = ten_mo_hinh
        # Đường dẫn lưu mô hình
        self.model_save_path = self.config['model_save_path']

    # Hàm tải dữ liệu huấn luyện
    def _load_train_dataset(self):
        df_train = pd.read_csv(self.config['data']['training_data_path'])
        cols = df_train.columns[:-2]
        train_features = df_train[cols]
        train_labels = df_train['prognosis']

        # Kiểm tra tính hợp lệ của dữ liệu
        assert (len(train_features.iloc[0]) == 132)
        assert (len(train_labels) == train_features.shape[0])

        if self.verbose:
            print("Kích thước dữ liệu huấn luyện: ", df_train.shape)
            print("Kích thước đặc trưng huấn luyện: ", train_features.shape)
            print("Kích thước nhãn huấn luyện: ", train_labels.shape)
        return train_features, train_labels, df_train

    # Hàm tải dữ liệu kiểm tra
    def _load_test_dataset(self):
        df_test = pd.read_csv(self.config['data']['test_data_path'])
        cols = df_test.columns[:-1]
        test_features = df_test[cols]
        test_labels = df_test['prognosis']

        # Kiểm tra tính hợp lệ của dữ liệu
        assert (len(test_features.iloc[0]) == 132)
        assert (len(test_labels) == test_features.shape[0])

        if self.verbose:
            print("Kích thước dữ liệu kiểm tra: ", df_test.shape)
            print("Kích thước đặc trưng kiểm tra: ", test_features.shape)
            print("Kích thước nhãn kiểm tra: ", test_labels.shape)
        return test_features, test_labels, df_test

    # Tính toán tương quan các đặc trưng
    def _feature_correlation(self, data_frame=None, show_fig=False):
        corr = data_frame.corr()
        sn.heatmap(corr, square=True, annot=False, cmap="YlGnBu")
        plt.title("Tương quan các đặc trưng")
        plt.tight_layout()
        if show_fig:
            plt.show()
        plt.savefig('feature_correlation.png')

    # Chia tập dữ liệu huấn luyện và xác thực
    def _train_val_split(self):
        X_train, X_val, y_train, y_val = train_test_split(self.train_features, self.train_labels,
                                                          test_size=self.config['data']['validation_size'],
                                                          random_state=self.config['random_state'])

        if self.verbose:
            print("Số lượng đặc trưng huấn luyện: {0}\tSố lượng nhãn huấn luyện: {1}".format(len(X_train), len(y_train)))
            print("Số lượng đặc trưng xác thực: {0}\tSố lượng nhãn xác thực: {1}".format(len(X_val), len(y_val)))
        return X_train, y_train, X_val, y_val

    # Lựa chọn mô hình
    def select_model(self):
        if self.ten_mo_hinh == 'mnb':
            self.clf = MultinomialNB()
        elif self.ten_mo_hinh == 'decision_tree':
            self.clf = DecisionTreeClassifier(criterion=self.config['model']['decision_tree']['criterion'])
        elif self.ten_mo_hinh == 'random_forest':
            self.clf = RandomForestClassifier(n_estimators=self.config['model']['random_forest']['n_estimators'])
        return self.clf

    # Huấn luyện mô hình
    def train_model(self):
        X_train, y_train, X_val, y_val = self._train_val_split()
        classifier = self.select_model()
        classifier.fit(X_train, y_train)
        confidence = classifier.score(X_val, y_val)
        y_pred = classifier.predict(X_val)
        accuracy = accuracy_score(y_val, y_pred)
        conf_mat = confusion_matrix(y_val, y_pred)
        clf_report = classification_report(y_val, y_pred)
        score = cross_val_score(classifier, X_val, y_val, cv=3)

        if self.verbose:
            print('\nĐộ chính xác huấn luyện: ', confidence)
            print('\nDự đoán xác thực: ', y_pred)
            print('\nĐộ chính xác xác thực: ', accuracy)
            print('\nMa trận nhầm lẫn xác thực: \n', conf_mat)
            print('\nĐiểm xác thực chéo: \n', score)
            print('\nBáo cáo phân loại: \n', clf_report)

        dump(classifier, str(self.model_save_path + self.ten_mo_hinh + ".joblib"))

    # Hàm dự đoán trên dữ liệu kiểm tra
    def make_prediction(self, saved_model_name=None, test_data=None):
        try:
            clf = load(str(self.model_save_path + saved_model_name + ".joblib"))
        except Exception as e:
            print("Mô hình không tìm thấy...")

        if test_data is not None:
            result = clf.predict(test_data)
            return result
        else:
            result = clf.predict(self.test_features)
        accuracy = accuracy_score(self.test_labels, result)
        clf_report = classification_report(self.test_labels, result)
        return accuracy, clf_report

if __name__ == "__main__":
    # Mô hình đang huấn luyện
    ten_mo_hinh_hien_tai = 'decision_tree'
    # Khởi tạo lớp
    dp = DuDoanBenhLy(ten_mo_hinh=ten_mo_hinh_hien_tai)
    # Huấn luyện mô hình
    dp.train_model()
    # Đánh giá hiệu suất mô hình trên dữ liệu kiểm tra
    do_chinh_xac_test, bao_cao_phan_loai = dp.make_prediction(saved_model_name=ten_mo_hinh_hien_tai)
    print("Độ chính xác mô hình trên dữ liệu kiểm tra: ", do_chinh_xac_test)
    print("Báo cáo phân loại dữ liệu kiểm tra: \n", bao_cao_phan_loai)

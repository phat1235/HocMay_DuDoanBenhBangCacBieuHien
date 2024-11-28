
### 1. **byte**
   - **Giới thiệu**: `byte` là kiểu dữ liệu số nguyên có kích thước 1 byte (8 bit), giá trị trong khoảng từ -128 đến 127. 
   - **Bài tập**: Kiểm tra xem một số nguyên có nằm trong phạm vi của `byte` hay không.
     ```java
     public class ByteExample {
         public static void main(String[] args) {
             int num = 150;
             if (num >= Byte.MIN_VALUE && num <= Byte.MAX_VALUE) {
                 System.out.println(num + " nằm trong phạm vi byte.");
             } else {
                 System.out.println(num + " không nằm trong phạm vi byte.");
             }
         }
     }
     ```
   - **Giải thích**: Chương trình kiểm tra xem giá trị của `num` có nằm trong phạm vi của kiểu `byte` (từ -128 đến 127) hay không.

### 2. **short**
   - **Giới thiệu**: `short` là kiểu dữ liệu số nguyên có kích thước 2 byte (16 bit), giá trị trong khoảng từ -32,768 đến 32,767.
   - **Ví dụ**:
     ```java
     short s = 25000;
     System.out.println(s);  // In ra giá trị của s
     ```
   - **Bài tập**: Tính tổng của hai số nguyên kiểu `short` và in ra kết quả.
     ```java
     public class ShortExample {
         public static void main(String[] args) {
             short num1 = 1500, num2 = 2000;
             short sum = (short) (num1 + num2);
             System.out.println("Tổng: " + sum);
         }
     }
     ```
   - **Giải thích**: Chương trình tính tổng của hai số nguyên kiểu `short` và in ra kết quả. Lưu ý, cần phải ép kiểu khi cộng các số `short` lại với nhau.

### 3. **int**
   - **Giới thiệu**: `int` là kiểu dữ liệu số nguyên có kích thước 4 byte (32 bit), giá trị trong khoảng từ -2,147,483,648 đến 2,147,483,647.
   - **Ví dụ**:
     ```java
     int i = 50000;
     System.out.println(i);  // In ra giá trị của i
     ```
   - **Bài tập**: Tính diện tích hình chữ nhật với chiều dài và chiều rộng kiểu `int`.
     ```java
     public class IntExample {
         public static void main(String[] args) {
             int length = 15, width = 10;
             int area = length * width;
             System.out.println("Diện tích hình chữ nhật: " + area);
         }
     }
     ```
   - **Giải thích**: Chương trình tính diện tích của hình chữ nhật với chiều dài và chiều rộng kiểu `int`.

### 4. **long**
   - **Giới thiệu**: `long` là kiểu dữ liệu số nguyên có kích thước 8 byte (64 bit), giá trị trong khoảng từ -9,223,372,036,854,775,808 đến 9,223,372,036,854,775,807.
   - **Ví dụ**:
     ```java
     long l = 10000000000L;
     System.out.println(l);  // In ra giá trị của l
     ```
   - **Bài tập**: Tính số lượng giây trong một năm, với năm là kiểu `long`.
     ```java
     public class LongExample {
         public static void main(String[] args) {
             long secondsInYear = 365L * 24 * 60 * 60;  // Số giây trong một năm
             System.out.println("Số giây trong một năm: " + secondsInYear);
         }
     }
     ```
   - **Giải thích**: Chương trình tính số giây trong một năm (365 ngày) và lưu vào biến `long`.

### 5. **float**
   - **Giới thiệu**: `float` là kiểu dữ liệu số thực có kích thước 4 byte (32 bit), được sử dụng để lưu trữ số thực với độ chính xác đơn.
   - **Ví dụ**:
     ```java
     float f = 5.75f;
     System.out.println(f);  // In ra giá trị của f
     ```
   - **Bài tập**: Tính chu vi hình tròn với bán kính nhập vào từ bàn phím, sử dụng `float`.
     ```java
     import java.util.Scanner;
     public class FloatExample {
         public static void main(String[] args) {
             Scanner scanner = new Scanner(System.in);
             System.out.print("Nhập bán kính: ");
             float radius = scanner.nextFloat();
             float circumference = 2 * 3.14f * radius;
             System.out.println("Chu vi hình tròn: " + circumference);
         }
     }
     ```
   - **Giải thích**: Chương trình yêu cầu người dùng nhập bán kính và tính chu vi hình tròn bằng công thức `2 * pi * radius`.

### 6. **double**
   - **Giới thiệu**: `double` là kiểu dữ liệu số thực có kích thước 8 byte (64 bit), được sử dụng để lưu trữ số thực với độ chính xác kép.
   - **Ví dụ**:
     ```java
     double d = 19.99;
     System.out.println(d);  // In ra giá trị của d
     ```
   - **Bài tập**: Tính thể tích hình cầu với bán kính nhập vào từ bàn phím, sử dụng `double`.
     ```java
     import java.util.Scanner;
     public class DoubleExample {
         public static void main(String[] args) {
             Scanner scanner = new Scanner(System.in);
             System.out.print("Nhập bán kính: ");
             double radius = scanner.nextDouble();
             double volume = (4.0 / 3) * 3.14 * radius * radius * radius;
             System.out.println("Thể tích hình cầu: " + volume);
         }
     }
     ```
   - **Giải thích**: Chương trình yêu cầu người dùng nhập bán kính và tính thể tích hình cầu với công thức `(4/3) * pi * r^3`.

### 7. **char**
   - **Giới thiệu**: `char` là kiểu dữ liệu dùng để lưu trữ một ký tự Unicode có kích thước 2 byte (16 bit).
   - **Ví dụ**:
     ```java
     char c = 'A';
     System.out.println(c);  // In ra ký tự 'A'
     ```
   - **Bài tập**: Kiểm tra xem một ký tự là chữ hoa hay chữ thường.
     ```java
     import java.util.Scanner;
     public class CharExample {
         public static void main(String[] args) {
             Scanner scanner = new Scanner(System.in);
             System.out.print("Nhập một ký tự: ");
             char ch = scanner.next().charAt(0);
             if (Character.isUpperCase(ch)) {
                 System.out.println(ch + " là chữ hoa.");
             } else if (Character.isLowerCase(ch)) {
                 System.out.println(ch + " là chữ thường.");
             } else {
                 System.out.println("Không phải chữ cái.");
             }
         }
     }
     ```
   - **Giải thích**: Chương trình nhận một ký tự và kiểm tra xem nó có phải là chữ hoa hay chữ thường.

### 8. **boolean**
   - **Giới thiệu**: `boolean` là kiểu dữ liệu lưu trữ giá trị `true` hoặc `false`, thường dùng trong các biểu thức điều kiện.
   - **Ví dụ**:
     ```java
     boolean isJavaFun = true;
     System.out.println(isJavaFun);  // In ra giá trị true
     ```
   - **Bài tập**: Kiểm tra số nguyên là số chẵn hay lẻ, sử dụng `boolean`.
     ```java
     public class BooleanExample {
         public static void main(String[] args) {
             int number = 7;
             boolean isEven = (number % 2 == 0);
             System.out.println(number + " là số chẵn: " + isEven);
         }
     }
     ```
   - **Giải thích**: Chương trình kiểm tra nếu một số nguyên là số chẵn hay lẻ và lưu kết quả vào biến `boolean`.



Dưới đây là phần trình bày chi tiết cho **Yêu Cầu 3** trong ảnh bạn gửi về việc sử dụng các cấu trúc điều kiện và vòng lặp trong Java:

---

### **Yêu Cầu 3: Trình bày cấu trúc điều kiện: if-else, switch-case, và vòng lặp: for, while, và do-while**

#### **1. Cấu trúc điều kiện if-else**

Cấu trúc điều kiện `if-else` trong Java cho phép chương trình kiểm tra một điều kiện và thực hiện các câu lệnh khác nhau tùy thuộc vào điều kiện đó.

- **Cú pháp**:
  ```java
  if (điều kiện) {
      // Câu lệnh thực hiện nếu điều kiện đúng
  } else {
      // Câu lệnh thực hiện nếu điều kiện sai
  }
  ```

- **Ví dụ**:
  ```java
  public class IfElseExample {
      public static void main(String[] args) {
          int x = 10;
          if (x > 5) {
              System.out.println("x lớn hơn 5");
          } else {
              System.out.println("x nhỏ hơn hoặc bằng 5");
          }
      }
  }
  ```

#### **2. Cấu trúc điều kiện switch-case**

Cấu trúc `switch-case` cho phép kiểm tra một giá trị với nhiều trường hợp khác nhau, giúp mã nguồn gọn gàng và dễ đọc hơn khi có nhiều điều kiện kiểm tra.

- **Cú pháp**:
  ```java
  switch (biểu thức) {
      case giá trị1:
          // Câu lệnh thực hiện nếu biểu thức bằng giá trị1
          break;
      case giá trị2:
          // Câu lệnh thực hiện nếu biểu thức bằng giá trị2
          break;
      default:
          // Câu lệnh thực hiện nếu biểu thức không bằng bất kỳ giá trị nào
  }
  ```

- **Ví dụ**:
  ```java
  public class SwitchExample {
      public static void main(String[] args) {
          int day = 3;
          switch (day) {
              case 1:
                  System.out.println("Chủ nhật");
                  break;
              case 2:
                  System.out.println("Thứ hai");
                  break;
              case 3:
                  System.out.println("Thứ ba");
                  break;
              default:
                  System.out.println("Ngày không hợp lệ");
          }
      }
  }
  ```

#### **3. Vòng lặp for**

Vòng lặp `for` trong Java được sử dụng khi bạn biết trước số lần lặp.

- **Cú pháp**:
  ```java
  for (khởi tạo; điều kiện; bước nhảy) {
      // Câu lệnh thực hiện trong vòng lặp
  }
  ```

- **Ví dụ**:
  ```java
  public class ForLoopExample {
      public static void main(String[] args) {
          for (int i = 0; i < 5; i++) {
              System.out.println(i);  // In ra các giá trị từ 0 đến 4
          }
      }
  }
  ```

#### **4. Vòng lặp while**

Vòng lặp `while` thực hiện lặp đi lặp lại một đoạn mã trong khi điều kiện là đúng.

- **Cú pháp**:
  ```java
  while (điều kiện) {
      // Câu lệnh thực hiện trong vòng lặp
  }
  ```

- **Ví dụ**:
  ```java
  public class WhileLoopExample {
      public static void main(String[] args) {
          int i = 0;
          while (i < 5) {
              System.out.println(i);  // In ra các giá trị từ 0 đến 4
              i++;
          }
      }
  }
  ```

#### **5. Vòng lặp do-while**

Vòng lặp `do-while` tương tự như vòng lặp `while`, nhưng nó sẽ luôn thực hiện ít nhất một lần, ngay cả khi điều kiện không thỏa mãn.

- **Cú pháp**:
  ```java
  do {
      // Câu lệnh thực hiện trong vòng lặp
  } while (điều kiện);
  ```

- **Ví dụ**:
  ```java
  public class DoWhileLoopExample {
      public static void main(String[] args) {
          int i = 0;
          do {
              System.out.println(i);  // In ra các giá trị từ 0 đến 4
              i++;
          } while (i < 5);
      }
  }
  ```

---

#### **Giải Thích Các Cấu Trúc:**

- **if-else**: Dùng để kiểm tra một điều kiện duy nhất và thực hiện một hành động nếu điều kiện đó là đúng, ngược lại thực hiện một hành động khác.
- **switch-case**: Thích hợp khi bạn cần kiểm tra một biến đối chiếu với nhiều giá trị khác nhau.
- **for**: Dùng khi bạn biết số lần lặp trước.
- **while**: Sử dụng khi bạn cần lặp một câu lệnh cho đến khi một điều kiện không còn thỏa mãn.
- **do-while**: Dùng khi bạn muốn đảm bảo ít nhất một lần thực thi vòng lặp trước khi kiểm tra điều kiện.

#### **Bài Tập Minh Họa**

- **Bài tập 1**: Viết chương trình kiểm tra một số có phải là số chẵn hay không.
  ```java
  public class EvenOddCheck {
      public static void main(String[] args) {
          int num = 10;
          if (num % 2 == 0) {
              System.out.println(num + " là số chẵn.");
          } else {
              System.out.println(num + " là số lẻ.");
          }
      }
  }
  ```

- **Bài tập 2**: Viết chương trình sử dụng vòng lặp `for` để in các số từ 1 đến 10.
  ```java
  public class PrintNumbers {
      public static void main(String[] args) {
          for (int i = 1; i <= 10; i++) {
              System.out.println(i);
          }
      }
  }
  ```

---
### **Yêu Cầu 4: Trình bày bốn nguyên tắc OOP.**

**OOP (Object-Oriented Programming)** hay lập trình hướng đối tượng là một phương pháp lập trình được sử dụng rộng rãi trong các ngôn ngữ như Java, C++, Python, v.v. OOP tập trung vào việc mô hình hóa các đối tượng trong thế giới thực dưới dạng các lớp (class) và đối tượng (object). Dưới đây là 4 nguyên tắc chính của OOP:

#### **1. Encapsulation (Đóng gói)**
Encapsulation là nguyên tắc của OOP mà trong đó các dữ liệu (thuộc tính) và các phương thức thao tác trên dữ liệu đó được gói gọn lại trong một lớp. Điều này giúp bảo vệ dữ liệu khỏi việc truy cập trực tiếp từ bên ngoài và chỉ có thể được truy cập qua các phương thức công khai (public methods).

- **Ví dụ**: Dữ liệu của đối tượng `Person` không thể bị thay đổi trực tiếp mà chỉ có thể thay đổi thông qua các phương thức `setName` hoặc `setAge`.
  ```java
  public class Person {
      private String name;  // Dữ liệu được bảo vệ
      private int age;
      
      // Phương thức getter và setter
      public String getName() {
          return name;
      }

      public void setName(String name) {
          this.name = name;
      }
      
      public int getAge() {
          return age;
      }

      public void setAge(int age) {
          if (age >= 0) {
              this.age = age;
          } else {
              System.out.println("Age must be non-negative");
          }
      }
  }
  ```

#### **2. Inheritance (Kế thừa)**
Kế thừa là khả năng của một lớp con (subclass) kế thừa các thuộc tính và phương thức của lớp cha (superclass). Điều này giúp tái sử dụng mã nguồn và mở rộng các chức năng mà không cần phải viết lại mã.

- **Ví dụ**: Lớp `Dog` kế thừa từ lớp `Animal`, do đó nó có thể sử dụng phương thức `makeSound()` của lớp `Animal`.
  ```java
  class Animal {
      public void makeSound() {
          System.out.println("Animal makes sound");
      }
  }

  class Dog extends Animal {
      @Override
      public void makeSound() {
          System.out.println("Dog barks");
      }
  }

  public class Main {
      public static void main(String[] args) {
          Dog dog = new Dog();
          dog.makeSound();  // In ra: Dog barks
      }
  }
  ```

#### **3. Polymorphism (Đa hình)**
Polymorphism cho phép một đối tượng có thể có nhiều dạng khác nhau. Điều này có thể đạt được qua việc sử dụng phương thức `overriding` (ghi đè) hoặc `overloading` (nạp chồng).

- **Ví dụ**:
  - **Overriding**: Một phương thức trong lớp con có thể ghi đè phương thức cùng tên trong lớp cha.
  ```java
  class Animal {
      public void sound() {
          System.out.println("Animal makes a sound");
      }
  }

  class Cat extends Animal {
      @Override
      public void sound() {
          System.out.println("Cat meows");
      }
  }
  
  public class Main {
      public static void main(String[] args) {
          Animal animal = new Cat();
          animal.sound();  // In ra: Cat meows
      }
  }
  ```
  - **Overloading**: Một phương thức có thể có nhiều phiên bản khác nhau, với số lượng hoặc kiểu tham số khác nhau.
  ```java
  public class Calculator {
      public int add(int a, int b) {
          return a + b;
      }
      
      public double add(double a, double b) {
          return a + b;
      }
      
      public static void main(String[] args) {
          Calculator calc = new Calculator();
          System.out.println(calc.add(5, 3));        // In ra: 8
          System.out.println(calc.add(5.5, 3.3));    // In ra: 8.8
      }
  }
  ```

#### **4. Abstraction (Trừu tượng)**
Abstraction giúp ẩn đi những chi tiết cài đặt phức tạp và chỉ hiển thị các phương thức hoặc chức năng cần thiết. Điều này giúp người sử dụng dễ dàng làm việc với đối tượng mà không cần biết chi tiết bên trong.

- **Ví dụ**: Trong một lớp trừu tượng, bạn có thể khai báo các phương thức mà không cung cấp cài đặt, và lớp con sẽ phải cài đặt các phương thức này.
  ```java
  abstract class Shape {
      abstract void draw();  // Phương thức trừu tượng, chưa có cài đặt
  }

  class Circle extends Shape {
      @Override
      void draw() {
          System.out.println("Drawing Circle");
      }
  }

  public class Main {
      public static void main(String[] args) {
          Shape shape = new Circle();
          shape.draw();  // In ra: Drawing Circle
      }
  }
  ```

---

### **Bài Tập Minh Họa**

#### **Bài Tập 1: Sử dụng Encapsulation**

Viết một lớp `BankAccount` có các thuộc tính `accountNumber` (số tài khoản) và `balance` (số dư tài khoản). Cung cấp phương thức để truy xuất và thay đổi số dư tài khoản, đồng thời ngăn không cho thay đổi số tài khoản trực tiếp.

```java
public class BankAccount {
    private String accountNumber;
    private double balance;

    public BankAccount(String accountNumber, double balance) {
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
        } else {
            System.out.println("Insufficient funds");
        }
    }
}
```

#### **Bài Tập 2: Sử dụng Inheritance**

Viết một lớp `Vehicle` có phương thức `startEngine()`, và tạo các lớp con như `Car` và `Motorcycle` kế thừa từ `Vehicle`, với các phương thức `startEngine()` riêng.

```java
class Vehicle {
    public void startEngine() {
        System.out.println("Vehicle engine started");
    }
}

class Car extends Vehicle {
    @Override
    public void startEngine() {
        System.out.println("Car engine started");
    }
}

class Motorcycle extends Vehicle {
    @Override
    public void startEngine() {
        System.out.println("Motorcycle engine started");
    }
}
```

#### **Bài Tập 3: Sử dụng Polymorphism**

Viết một chương trình cho phép nhiều đối tượng có thể có những hành động khác nhau khi gọi phương thức `speak()`, ví dụ như `Dog`, `Cat`, và `Bird`.

```java
class Animal {
    public void speak() {
        System.out.println("Animal speaks");
    }
}

class Dog extends Animal {
    @Override
    public void speak() {
        System.out.println("Dog barks");
    }
}

class Cat extends Animal {
    @Override
    public void speak() {
        System.out.println("Cat meows");
    }
}

class Bird extends Animal {
    @Override
    public void speak() {
        System.out.println("Bird chirps");
    }
}
```

#### **Bài Tập 4: Sử dụng Abstraction**

Viết một chương trình với lớp trừu tượng `Shape` và các lớp con `Rectangle`, `Circle` để tính diện tích.

```java
abstract class Shape {
    abstract double area();
}

class Rectangle extends Shape {
    double width, height;

    Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    @Override
    double area() {
        return width * height;
    }
}

class Circle extends Shape {
    double radius;

    Circle(double radius) {
        this.radius = radius;
    }

    @Override
    double area() {
        return Math.PI * radius * radius;
    }
}
```

---

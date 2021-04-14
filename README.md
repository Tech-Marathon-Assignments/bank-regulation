# Problem statement

**Đề bài**: Theo quy định của ngân hàng Vietcombank, việc vay tiêu dùng không thế chấp phải thỏa mãn các điều kiện sau:
- Khách hàng có độ tuổi tối thiểu là 20 khi bắt đầu vay và không quá 60 tuổi tại thời điểm kết thúc khoản vay.
- Khách hàng có thu nhập ổn định tối thiểu từ 3 triệu trở lên.
- Giấy tờ pháp lý rõ ràng, phải có bản gốc, không tẩy xóa, các trang bổ sung phải có đầy đủ và được cơ quan chức năng đóng dấu giáp lai cùng trang chính. (để đơn giản, ta chỉ cần tạo một biến lưu trữ tính hợp pháp của giấy tờ là được)
- Thời gian vay tối đa 60 tháng.
- Đối với tiêu dùng không thế chấp hạn mức vay tối đa là 20 lần thu nhập bình quân hàng tháng và không quá 500 triệu đồng. <br/>
Viết chương trình kiểm tra xem người dùng đủ điều kiện để vay vốn tiêu dùng không thế chấp chưa và số tiền tối đa có thể vay được.

**Problem**: According to Vietcombank's regulations, unsecured consumer loans must satisfy the following conditions:
- Customers are at least 20 years old at the start of the loan and not more than 60 years old at the time of loan termination.
- Customers with a minimum stable income of 3 million or more.
- Clear legal papers must be original, not erased, additional pages must be complete and stamped on the same page by authorities. (For simplicity, we just need to create a variable to store the legality of the paper.)
- The maximum loan period of 60 months.
- For non-mortgage consumers, the maximum loan limit is 20 times of the average monthly income and not more than VND 500 million. <br/>
Write a program that checks whether a user qualifies for a non-mortgage consumer loan and the maximum amount that can be borrowed.

**Input**: 18 10000000 False 12 100000000
**Output**: "Unqualified"

**Input**: 21 10000000 True 24 100000000
**Output**: "Qualified"

# Instructions

## Setup

- Create a virtual environment

```bash
python -m venv venv
```

- To activate virtual environment, on Windows:

```bash
.\venv\Scripts\activate
```

on MacOS or Linux:

```bash
source venv\bin\activate
```

- Install require package:

```bash
pip install autopep8 pylint pytest
```

## Coding and checking

- Write down your solution in main.py.
- You can test your code by changing the parameters in the main function caller.
- When you're finished, check your solution by opening the command prompt and type "py.test" or "pytest test_main".
- When everything is done, submit your assignment and our autograding system will grade your assignment.

## Submission

```bash
git add .
git commit -m "submit *insert solution name*"
git push
```

# Video instruction

Link: \*_insert link here_\*

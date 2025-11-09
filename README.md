# online-bookstore

Sure — here is a ready-to-use **README.md file** (no explanations, just the file content).
Copy this entire text into a file named `README.md` and upload it to your GitHub repo.

---

### ✅ README.md

```markdown
# 📚 Online Bookstore (Flask + MySQL + Automation Testing)

A dynamic Online Bookstore web application built using **Flask (Python), MySQL, HTML, CSS, JavaScript**, and **Selenium Automation Testing**.

---

## 🚀 Features

- User Registration & Login
- Dynamic Book Listing (Fetched from MySQL)
- Add to Cart / Checkout System
- Order Placement (Simulated Payment)
- Admin Panel to Add/Delete Books
- Selenium Automated Test Cases

---

## 🛠 Tech Stack

| Component | Technology Used |
|----------|----------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python Flask |
| Database | MySQL |
| Testing | Selenium WebDriver |

---

## 📂 Project Structure

```

onlinebookstore/
│── app.py                     # Flask backend application
│── database.sql               # Database structure and initial data
│── automation_test/
│      └── test_cases.py       # Selenium test automation script
│
└── templates/
├── index.html
├── checkout.html
├── login.html
├── register.html
└── admin.html

````

---

## 🛢 Database Setup (MySQL)

Run this SQL script (`database.sql`) in MySQL:

```sql
CREATE DATABASE bookstore;
USE bookstore;

CREATE TABLE books(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    price DECIMAL(10,2)
);

INSERT INTO books(title, author, price) VALUES
("Clean Code", "Robert Martin", 500),
("JavaScript: The Good Parts", "Douglas Crockford", 400),
("The Pragmatic Programmer", "Andrew Hunt", 650);

CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);
````

---

## ▶️ Run the Application (Flask)

### Install dependencies

```
pip install flask flask-mysqldb
```

### Update database credentials in `app.py`

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'bookstore'
```

### Run app

```
python app.py
```

Open browser → [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🤖 Automation Testing (Selenium)

### Install Selenium

```
pip install selenium
```

Download ChromeDriver (same version as Chrome):
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

### Run the test script:

```
python automation_test/test_cases.py
```

---

## ✅ Automated Test Results

| Test Case ID | Test Description            | Status |
| ------------ | --------------------------- | ------ |
| TC_F_01      | Register User               | ✅ PASS |
| TC_F_02      | Login User                  | ✅ PASS |
| TC_F_03      | Search Books                | ✅ PASS |
| TC_F_04      | Add to Cart                 | ✅ PASS |
| TC_F_05      | Order Placement (Simulated) | ❌ FAIL |
| TC_F_06      | Admin Add Book              | ✅ PASS |

> TC_F_05 is intentionally failed as per test case document (Payment Gateway not implemented)

---

## 📌 Future Enhancements

* Real payment gateway integration
* Add book filtering and sorting
* Email confirmation on order

---

## 🙌 Developed By

**Akash Nimbolkar**
Mini Project — Software Testing & Quality Assurance

---

⭐ If you like this project, consider giving it a star on GitHub!

➡ Repository Link: *[https://github.com/akash-nimbolkar/online-bookstore](https://github.com/akash-nimbolkar/online-bookstore)*

```

---

If you want, I can also:

✅ Upload screenshots and update README  
✅ Generate a **PDF Test Report** for submission  

Just say: **"Generate PDF Test Report"**
```

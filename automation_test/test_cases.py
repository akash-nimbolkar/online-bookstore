from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def print_result(test_id, result):
    print(f"{test_id} --> {'✅ PASS' if result else '❌ FAIL'}")

# ------------------- TC_F_01 : Register User -------------------
driver.get("http://127.0.0.1:5000/register")
time.sleep(1)

driver.find_element(By.NAME, "username").send_keys("testuser1")
driver.find_element(By.NAME, "password").send_keys("1234")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)

result = "login" in driver.current_url
print_result("TC_F_01 Register new user", result)


# ------------------- TC_F_02 : Login -------------------
driver.get("http://127.0.0.1:5000/login")
time.sleep(1)

driver.find_element(By.NAME, "username").send_keys("testuser1")
driver.find_element(By.NAME, "password").send_keys("1234")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)

result = "admin" in driver.current_url
print_result("TC_F_02 Login with valid credentials", result)


# ------------------- TC_F_03 : Search Book -------------------
driver.get("http://127.0.0.1:5000")
time.sleep(1)

books = driver.find_elements(By.CLASS_NAME, "book-card")
result = len(books) > 0
print_result("TC_F_03 Search Books", result)


# ------------------- TC_F_04 : Add to Cart (Buy Now button) -------------------
driver.find_element(By.CLASS_NAME, "book-card").click()
time.sleep(1)

result = "checkout" in driver.current_url
print_result("TC_F_04 Add Book to cart", result)


# ------------------- TC_F_05 : Place Order (Simulation) -------------------
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)

result = "Payment Done" in driver.page_source
print_result("TC_F_05 Order Placement", result)


# ------------------- TC_F_06 : Add Book (Admin Panel) -------------------
driver.get("http://127.0.0.1:5000/admin")
time.sleep(1)

driver.find_element(By.NAME, "title").send_keys("Automation Testing Book")
driver.find_element(By.NAME, "author").send_keys("John")
driver.find_element(By.NAME, "price").send_keys("450")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)

result = "Automation Testing Book" in driver.page_source
print_result("TC_F_06 Add Book", result)


driver.quit()

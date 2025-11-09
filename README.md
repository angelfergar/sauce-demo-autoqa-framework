# 🤖 **Sauce Demo QA Automation Project**

This Project is a QA Automation Framework built to validate the basic functionality of the [Sauce Demo](https://www.saucedemo.com/) web. It covers Smoke Testing for login, inventory management, cart, checkout, and order completion flows. The goal is to show the process of verification, error handling and reporting. Some test cases contain errors to showcase the framework's ability to detect failures.

The framework is implemented using **Python, Selenium, pytest, unittest and the Page Object Model (POM)**, with modular design for maintainability and scalability.
 
It uses **Python, Selenium, pytest, and unittest** to perform smoke tests on the basic functionality of the platform, covering:

---

## 📌 **Project Structure**
```
project/
│
├─ base/
│ └─ base_page.py
│ └─ selenium_webdriver.py
│ └─ webdriver_factory.py
│
├─ pages/
│ ├─ cart/
│ │ └─ cart_page.py
│ ├─ checkout/
│ │ └─ checkout_page.py
│ ├─ login/
│ │ └─ login_page.py
│ └─ overview/
│ └─ overview_page.py
│ ├─ shop/
│ │ └─ shop_page.py
│
├─ screenshots/
│
├─ tests/
│ ├─ cart/
│ │ └─ cart_test.py
│ ├─ checkout/
│ │ └─ checkout_test.py
│ ├─ login/
│ │ └─ login_test.py
│ └─ overview/
│ │└─ overview_test.py
│ ├─ shop/
│ │ └─ shop_test.py
│ └─ conftest.py
│ └─ test_suite.py
│
├─ utilities/
│ └─ custom_logger.py
│ └─ test_status.py
│ └─ util.py
│
└─ inventory_data.csv
└─ README.md
└─ report.html
└─ requirements.txt
└─ 2025-11-09_saucedemo.log
```

---

## ⚙️ **1. Framework Overview**

The project is built using a Page Object Model (POM) with the following layers:

### **1.1 Base Classes**

* **SeleniumDriver**

Its main purpose is to simplify Selenium Webdriver actions such as clicking elements, sending keys, waiting for elements, and verifying visibility.

* **BasePage**

It is used by all Page Objects to share core Selenium methods, ensuring their interactions are centralized for maintainability.

* **WebDriverFactory**

It provides WebDriver instances for Chrome, Firefox, or Edge for initializing browsers and navigate to the base URL of the Sauce Demo web.

### **1.2 Page Objects**

* **LoginPage**

It handles tests for the login/logout, as well as error validation during login operations.

* **ShopPage** 

It tests product listings and their info, sorting, as well as adding/removing items from the cart.

* **CartPage**

It handles shopping cart operations such as verifying items, removing items, and flows to the Shop and Checkout pages.

* **CheckoutPage**

 It tests form validation methods, and navigation from the Cart to the Overview page.

* **OverviewPage** 

It handles final review and order completion.

### **1.3 Utilities**

* **Util**
 
It includes a list of methods that can be used on other modules. These include:

- Text and list verification.

- CSV data loading for test validations.

* **CustomLogger**

It generates structured logging for debugging, gathering info and detect errors.

* **TestStatus**

It provides information on the verification steps, logs the results, take screenshots, and asserts the final status for the tests.

### **1.4 Tests**

Each test was done using a combination of pytest and unittest, providing a modular test structure. The order for the tests is managed with pytest.mark.order to simulate user flows.

There is a test assigned for each Page Class.

login_test.py → LoginPage

shop_test.py → ShopPage

cart_test.py → CartPage

checkout_test.py → CheckoutPage

overview_test.py → OverviewPage

All of these tests were included in a Test Suite list, so they can be run each time the script for the Test Suite is executed.

After each Test Suite execution, we will obtain a **report.html and a .log file** including all the information and results related to the execution. We will also have a list of screenshots that provide additional information, useful at the time of checking the final status of the tests.

---

## 📥 **2. Jenkins Integration**

The framework can be integrated with Jenkins, ensuring continuous validation for the tests. By adding this framework to Jenkins, we can:

* Run tests consistently across different environments and browsers.

* Automatically generate and publish test reports and logs.

* Archive screenshots and logs for debugging.

* Ensure new changes are validated immediately.

This section explain how to configure Jenkins to run the framework on on Windows.

### **2.1 Job Configuration**

**Step 1: Create a Freestyle Item**

Go to Jenkins > New Item > Freestyle Project > Give it a name > Ok

**Step 2: Source Code Management**

Choose Git > Enter the repository's URL > Introduce the credentials > Select Main as the Branch

**Step 3: Build Steps**

Select the option "Execute Windows Batch Command" and add:

```
echo %CD%
pip install -r requirements.txt
set PYTHONPATH=%CD%
pytest -s -v tests/test_suite.py --browser Firefox --html=report.html
```

**Step 4: Running the Test**

After setting up the new Item, just click on "Build Now" to run the Test Suite.

---

## 🛠️ **3. Framework Highlights**

* By using POM we get a clear separation between tests and the actions performed in each page.

* Cross-browser support on Chrome, Firefox and Edge thanks to the WebDriverFactory class.

* SeleniumDriver and BasePage offer reusability, and provide a list of methods that make the process of building actions for pages and tests much simpler.

* Having a custom logger allows the framework to have information about each step of the validation, giving a clear way to track errors during validation.

* The framework can be easily integrated in a CI/CD process.

---

🤝 **4. Contribution**

Suggestions and improvements are welcome! 🚀

**Author:** Ángel Fernández

**Email:** anfernagar@gmail.com

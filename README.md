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

## 🛠️ **2. Test Suites**

### **2.1 Login/Logout**

| **TC ID** | **Test Case Description**                                                        | **Expected Result**                                                                                           |
| --------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| TC01      | Verify successful login using valid credentials (`standard_user / secret_sauce`) | User is redirected to the Inventory page                                                                      |
| TC02      | Verify error message for locked user (`locked_out_user / secret_sauce`)          | Correct error message displayed (“Epic sadface: Sorry, this user has been locked out.”)                       |
| TC03      | Verify error message with invalid username/password                              | Correct error message displayed (“Epic sadface: Username and password do not match any user in this service”) |
| TC04      | Verify error message when no password is entered                                 | Correct error message displayed ("Epic sadface: Password is required")                                        |
| TC05      | Verify error message when no username is entered                                 | Correct error message displayed ("Epic sadface: Username is required"                                         |
| TC06      | Verify logout cannot be performed without opening sidebar menu                   | Logout option is inaccessible                                                                                 |
| TC07      | Verify logout using the sidebar menu                                             | User is redirected to the Login page                                                                          |

### **2.2 Inventory**

| **TC ID** | **Test Case Description**                                        | **Expected Result**                                    |
| --------- | ---------------------------------------------------------------- | ------------------------------------------------------ |
| TC09      | Verify that 6 products are displayed                             | All 6 items are in the inventory list                  |
| TC10      | Verify product titles are correct                                | Product titles match the expected data                 |
| TC11      | Verify product descriptions are correct                          | Product descriptions match the expected data           |
| TC12      | Verify product prices are correct                                | Product prices match the expected data                 |
| TC13      | Verify sorting A → Z works correctly                             | Products appear in ascending alphabetical order        |
| TC14      | Verify sorting Z → A works correctly                             | Products appear in descending alphabetical order       |
| TC15      | Verify sorting by price (Low → High)                             | Products are ordered from lowest to highest price      |
| TC16      | Verify sorting by price (High → Low)                             | Products are ordered from highest to lowest price      |
| TC17      | Verify each product has an “Add to Cart” button                  | All products display the button                        |
| TC18      | Verify adding all products updates cart count correctly          | Cart shows “6” after adding all products               |
| TC19      | Verify button changes from “Add to Cart” to “Remove”             | Add buton changes to “Remove”                          |
| TC20      | Verify removing product updates cart count                       | Cart doesn't show a number after removing all products |

### **2.3 Shopping Cart**

| **TC ID** | **Test Case Description**                                          | **Expected Result**                             |
| --------- | ------------------------------------------------------------------ | ----------------------------------------------- |
| TC21      | Verify “Cart” button takes you to Shopping Cart page               | User is redirected to Shopping Cart page        |
| TC22      | Verify product appears correctly in cart                           | Product is displayed in the cart                |
| TC23      | Verify product info in cart matches store info                     | Product name matches the inventory page         |
| TC24      | Verify “Remove” button is available for all items                  | Each product has a “Remove” button              |
| TC25      | Verify cart updates when removing an item                          | Product is removed from the list                |
| TC26      | Verify “All Items” button takes you back to Inventory page         | User is redirected to Inventory page            |
| TC27      | Verify “Continue Shopping” button takes you back to Inventory page | User is redirected to Inventory page            |
| TC28      | Verify “Checkout” button takes you to Checkout page                | User is redirected to Checkout page             |

### **2.4 Checkout**

| **TC ID** | **Test Case Description**                                                      | **Expected Result**                                                |
| --------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| TC29      | Verify “Cancel” button takes you back to Shoppng Cart page                     | User is redirected to Shopping Cart page                           |
| TC30      | Verify Cart icon navigates back to Shopping Cart page                          | User is redirected to Shopping Cart page                           |
| TC31      | Verify error message when all fields are empty                                 | Correct error message displayed  (“Error: First Name is required”) |
| TC32      | Verify error message when only First Name is entered                           | Correct error message displayed (“Error: Last Name is required”)   |
| TC33      | Verify error message when First and Last Name entered, but missing Postal Code | Correct error message displayed (“Error: Postal Code is required”) |
| TC34      | Verify successful navigation when all fields are filled                        | User is redirected to Checkout: Overview page                      |

### **2.5 Checkout: Overview and Completion**

| **TC ID** | **Test Case Description**                              | **Expected Result**                                     |
| --------- | -------------------------------------------------------| ------------------------------------------------------- |
| TC35      | Verify “Cancel” button takes you back to Checkout page | User is redirected to previous step                     |
| TC36      | Verify Cart icon navigates back to Shopping Cart page  | User is redirected to Shopng Cart page                  |
| TC37	     | Verify “Finish” button completes the order             | User is redirected to Checkout: Complete page           |
| TC38      | Verify success message after completing order          | Correct message displayed (“Thank you for your order!”) |
| TC39      | Verify “Back Home” button navigates to Inventory page  | User is redirected to Inventory page                    |

---

## 📥 **3. Jenkins Integration**

The framework can be integrated with Jenkins, ensuring continuous validation for the tests. By adding this framework to Jenkins, we can:

* Run tests consistently across different environments and browsers.

* Automatically generate and publish test reports and logs.

* Archive screenshots and logs for debugging.

* Ensure new changes are validated immediately.

This section explain how to configure Jenkins to run the framework on on Windows.

### **3.1 Job Configuration**

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

## 📈 **4. Framework Highlights**

* By using POM we get a clear separation between tests and the actions performed in each page.

* Cross-browser support on Chrome, Firefox and Edge thanks to the WebDriverFactory class.

* SeleniumDriver and BasePage offer reusability, and provide a list of methods that make the process of building actions for pages and tests much simpler.

* Having a custom logger allows the framework to have information about each step of the validation, giving a clear way to track errors during validation.

* The framework can be easily integrated in a CI/CD process.

---

🤝 **5. Contribution**

Suggestions and improvements are welcome! 🚀

**Author:** Ángel Fernández

**Email:** anfernagar@gmail.com

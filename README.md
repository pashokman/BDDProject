# BDDProject

# How to create BDDTests

1. Create a project like usual.
2. Create directory (module) - "features".
3. Create file with name like this - "search.feature"
4. Describe a test in created file, like this:
```
Feature: Login Feature

    Scenario: Login with valid credentials
        Given I navigate to login page
        When I enter valid email and valid password into the fields
        And I click on Login button
        Then I should get successfully logged in

    Scenario: Login with valid emain and invalid password
        Given I navigate to login page
        When I enter valid email and invalid password into the fields
        And I click on Login button
        Then I should get a proper warning message
```
5. Install - "pip instal behave"
6. In "features" directory (module), create directory (module) - "steps".
7. In "steps" directory (module) create file with name like "search.py".
8. Run command - "behave features". Copy from console text like this into the "search.py" file:
```
@given(u'I am on the Application Home page')
def step_impl(context):
    raise NotImplementedError...
```
9. Add into "search.py" file - "from behave import given, when, then".
10. Change "raise NotImplementedError..." into "print('Inside - I am on the Application Home page')".
11. Run command - "behave features" or "behave features/search.feature". All features, scenarious, steps should pass.
12. Create file "environment.py" to centrilized hooks under "features" package.
13. Add hooks into a file "environment.py" (functions that will run before and after each scenario, after each step).
```
from selenium import webdriver

def before_scenario(context, driver):
    context.driver = webdriver.Chrome()

def after_scenario(context, driver):
    context.driver.quit()

def after_step(context, step):
    print('Inside - After Step')
    print()
```
14. Create "behave.ini" file into a root project folder, with this code (this is enable print statements in console):
```
[behave]
stdout_capture = false
stderr_capture = false
log_capture = false
```
15. If we set the parameter in search.feature file, we should change the fuction in search.py file, like this (in function name, in function parameters, in function body):

search.feature
```
Feature: Search Feature

    Scenario: Search for a valid product
        Given I am on the Application Home page
        When I enter valid product "HP" into Search box field
        And I click on Search button
        Then Valid product should be displayed in Search results page
```
search.py
```
@when(u'I enter valid product "{product}" into Search box field')
def step_impl(context, product):
    print(f'Inside - I enter valid product - {product} into Search box field')
```
16. To convert default test scenario into data driven test, we should change test from first example into second one (can run multiple times with different sets of data):

login.feature
```
Feature: Login Feature

    Scenario: Login with valid credentials
        Given I navigate to login page
        When I enter valid Email as "test_auto@gmail.com" and valid Password as "12345" into the fields
        And I click on Login button
        Then I should get successfully logged in
```
```    
Feature: Login Feature

    Scenario Outline: Login with valid credentials
        Given I navigate to login page
        When I enter valid Email as "<email>" and valid Password as "<password>" into the fields
        And I click on Login button
        Then I should get successfully logged in
        Examples:
            |email                  |password   |
            |test_auto@gmail.com    |12345      |
            |amotoorione@gmail.com  |secondone  |
```
17. To specify tag by wich we can run our tests we shoul use "@" before the test name in "search.feature" file, like this:
```
    @login  @regression
    Scenario: Login with valid emain and invalid password
        Given I navigate to login page
        When I enter valid email and invalid password into the fields
        And I click on Login button
        Then I should get a proper warning message
```
18. To run only tests with some tags: "behave features --tags=search".
19. To run all tests exept tests with some tag: "behave features --tags=-search".
20. To run tests with multiple tags "behave features --tags=search --tags=regression".
21. To add Background (function that apply to all test scenarios in feature file - pre-request steps) - DRY principle.
```
Feature: Search Feature

    Background:
        Given I am on the Application Home page

    @search @smoke
    Scenario: Search for a valid product
        When I enter valid product "HP" into Search box field
        And I click on Search button
        Then Valid product should be displayed in Search results page
```
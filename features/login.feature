Feature: Login Feature

    @login @smoke
    Scenario Outline: Login with valid credentials
        Given I navigate to login page
        When I enter valid Email as "<email>" and valid Password as "<password>" into the fields
        And I click on Login button
        Then I should get successfully logged in
        Examples:
            |email                  |password   |
            |test_auto@gmail.com    |12345      |
            |amotoorione@gmail.com  |secondone  |

    @login  @regression
    Scenario: Login with valid emain and invalid password
        Given I navigate to login page
        When I enter valid email and invalid password into the fields
        And I click on Login button
        Then I should get a proper warning message

    @login @regression
    Scenario: Login with invalid emain and valid password
        Given I navigate to login page
        When I enter invalid email and valid password into the fields
        And I click on Login button
        Then I should get a proper warning message

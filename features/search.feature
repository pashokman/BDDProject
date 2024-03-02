Feature: Search Feature

    Background:
        Given I am on the Application Home page

    @search @smoke
    Scenario: Search for a valid product
        When I enter valid product "HP" into Search box field
        And I click on Search button
        Then Valid product should be displayed in Search results page
    
    @search @regression
    Scenario: Search for an invalid product
        When I enter invalid product "Honda" into Search box field
        And I click on Search button
        Then Proper message should be displayed in Search results page

    @search @regression
    Scenario: Search without providing any product details
        When I don't enter any product into Search box field
        And I click on Search button
        Then Proper message should be displayed in Search results page
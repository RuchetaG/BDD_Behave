Feature: User should be able to login

    Background:
        Given User is on the login page

    Scenario: User enters username and password and login is successful
        When User enters the username
        And User enters the "Rucheta@123"
        Then User should be logged into the system

    Scenario: User enters username and incorrect password
        When User enters the username
        And User enters the "password"
        Then Error should be displayed
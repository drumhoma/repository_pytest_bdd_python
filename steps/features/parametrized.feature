# noinspection CucumberUndefinedStep
Feature: parametrized

  Scenario: Parametrized given, when, then
    Given there are <start> cucumbers
    When I eat <eat> cucumbers
    Then I should have <left> cucumbers
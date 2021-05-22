# noinspection CucumberUndefinedStep
Feature: Outline

Examples:
| start | eat | left |
|  12   |  5  |  7   |
|  5    |  4  |  1   |

  Scenario Outline: Eat fruits
    Given there are <start> <fruits>
    When I eat <eat> <fruits>
    Then I should have <left> <fruits>

    Examples:
      | fruits  |
      | oranges |
      | apples  |

  Scenario Outline: Eat vegetables
    Given there are <start> <vegetables>
    When I eat <eat> <vegetables>
    Then I should have <left> <vegetables>

    Examples:
      | vegetables |
      | carrots    |
      | tomatoes   |
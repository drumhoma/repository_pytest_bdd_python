Feature: Blog
  A site where you can publish your articles.

      # noinspection CucumberUndefinedStep
  Scenario: Publishing the article
    Given I'm an author user
    And I have an article

    When I go to the article page
    And I press the publish button

    Then I should not see the error message
    And the article should be published
    # Note: will query the database
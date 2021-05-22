# coding=utf-8
"""Multiple site support feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features\\backgrounds.feature', 'Greg posts to a client\'s blog')
def test_greg_posts_to_a_clients_blog():
    """Greg posts to a client's blog."""


@scenario('features\\backgrounds.feature', 'Wilson posts to his own blog')
def test_wilson_posts_to_his_own_blog():
    """Wilson posts to his own blog."""


@given('I am logged in as Greg')
def i_am_logged_in_as_greg():
    """I am logged in as Greg."""
    raise NotImplementedError


@given('I am logged in as Wilson')
def i_am_logged_in_as_wilson():
    """I am logged in as Wilson."""
    raise NotImplementedError


@given('a blog named "Expensive Therapy" owned by "Wilson"')
def a_blog_named_expensive_therapy_owned_by_wilson():
    """a blog named "Expensive Therapy" owned by "Wilson"."""
    raise NotImplementedError


@given('a blog named "Greg\'s anti-tax rants"')
def a_blog_named_gregs_antitax_rants():
    """a blog named "Greg's anti-tax rants"."""
    raise NotImplementedError


@given('a customer named "Wilson"')
def a_customer_named_wilson():
    """a customer named "Wilson"."""
    raise NotImplementedError


@given('a global administrator named "Greg"')
def a_global_administrator_named_greg():
    """a global administrator named "Greg"."""
    raise NotImplementedError


@when('I try to post to "Expensive Therapy"')
def i_try_to_post_to_expensive_therapy():
    """I try to post to "Expensive Therapy"."""
    raise NotImplementedError


@then('I should see "Your article was published."')
def i_should_see_your_article_was_published():
    """I should see "Your article was published."."""
    raise NotImplementedError


@then('pytest-bdd generate features/backgrounds.feature > test_backgrounds.py')
def pytestbdd_generate_featuresbackgroundsfeature__test_backgroundspy():
    """pytest-bdd generate features/backgrounds.feature > test_backgrounds.py."""
    raise NotImplementedError


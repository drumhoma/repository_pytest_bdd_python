import pytest
from pytest_bdd import scenario, given, when, then


# Here we use pytest to parametrize the test with the parameters table
@pytest.mark.parametrize(
    ["start", "eat", "left"],
    [(12, 5, 7)],
)
@scenario(
    "features\\parametrized.feature",
    "Parametrized given, when, then",
)
# Note that we should take the same arguments in the test function that we use
# for the test parametrization either directly or indirectly (fixtures depend on them).
def test_parametrized(start, eat, left):
    """We don't need to do anything here, everything will be managed by the scenario decorator."""


@given("there are <start> cucumbers", target_fixture="start_cucumbers")
def start_cucumbers(start):
    return dict(start=start)


@when("I eat <eat> cucumbers")
def eat_cucumbers(start_cucumbers, start, eat):
    start_cucumbers["eat"] = eat


@then("I should have <left> cucumbers")
def should_have_left_cucumbers(start_cucumbers, start, eat, left):
    assert start - eat == left
    assert start_cucumbers["start"] == start
    assert start_cucumbers["eat"] == eat

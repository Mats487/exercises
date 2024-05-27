import pytest
from parentheses import matching_parentheses


@pytest.mark.parametrize('string', [
    ('()'),
    ('((()))'),
    ('()()()')
])
def test_matching_parentheses(string):
    assert matching_parentheses(string), f"Parentheses {string}, are matching."

@pytest.mark.parametrize('string', [
    ('()))'),
    ('((())))'),
    ('())((())(()'),
    (')(')
])
def test_nonmatching_parentheses(string):
    assert not matching_parentheses(string), f"Parentheses {string}, don't match."


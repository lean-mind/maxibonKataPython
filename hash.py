#!/usr/bin/env python3
from hypothesis import given, example, assume
from hypothesis.strategies import text, integers

# Function under test:
def hash(text):
    return text

# Tests:

@given(text())
def test_hash_is_always_the_same_given_the_same_input(text):
    assert hash(text) == hash(text)

@given(text(), text())
def test_hash_is_different_for_each_input(text1, text2):
    assume(text1 != text2)
    assert hash(text1) != hash(text2)


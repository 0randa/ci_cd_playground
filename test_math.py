#!/usr/bin/env python3


def add(a: int, b: int) -> int:
    return a + b


def test_add():
    assert add(9, 10) == 19
    assert add(3, 2) == 5

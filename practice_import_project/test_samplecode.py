#!/usr/bin/env python3

import samplecode

def test_say_hi():
    name = 'Cody'
    sentence = samplecode.say_hi(name)
    assert sentence == 'Hi, Cody!', 'Sentence is not formatted correctly'

def test_add_2():
    number = 2
    value = samplecode.add_2(number)
    assert value == 4, f"Number doesn't add up to 4"

def test_minus_2():
    number = 5
    value = samplecode.minus_2(number)
    assert value == 3, f"Number doesn't add up to 4. Value given is {value}"


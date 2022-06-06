import pytest
from madlib_cli.madlib import read_template, parse_template, merge_for_test

#Please comment out the input collections before executing the tests
mainString = """Make Me A Video Game!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find."""


def test_read_template():
    actual = read_template("../assets/templateFile.txt")
    expected = mainString
    assert actual == expected


def test_parse_template():
    actual_stripped = parse_template(mainString)
    expected_stripped = "Make Me A Video Game!\n\nI the {} and {} {} have {}{}'s {} sister and plan to steal her {} {}!\n\nWhat are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {} and {} {} that open up the {} worlds connected to A {} Lair. There are {} {} and {} {} in the game, along with hundreds of other goodies for you to find."
    # expected_parts = ("Adjective", "Adjective", "A_First_Name", "Adjective","Adjective", "Plural Noun", "Large Animal", "Small Animal", "A Girl's Name", "Adjective", "Plural Noun", "Adjective", "Plural Noun", "Number 1-50", "First Name's", "Number", "Plural Noun", "Number", "Plural Noun")
    assert actual_stripped == expected_stripped
    # assert actual_parts == expected_parts

inputsforTesting = ['happy','sad','jumana','eated','sama','shiny','great','friends','elephant','bird','jumana','wet','pens', 'dry','cats', '30','lara', '78','students', '20','couples']

def test_merge_for_test():
    actual = merge_for_test("Make Me A Video Game!\n\nI the {} and {} {} have {}{}'s {} sister and plan to steal her {} {}!\n\nWhat are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {} and {} {} that open up the {} worlds connected to A {} Lair. There are {} {} and {} {} in the game, along with hundreds of other goodies for you to find.",inputsforTesting)
    expected = """Make Me A Video Game!

I the happy and sad jumana have eatedsama's shiny sister and plan to steal her great friends!

What are a elephant and backpacking bird to do? Before you can help jumana, you'll have to collect the wet pens and dry cats that open up the 30 worlds connected to A lara Lair. There are 78 students and 20 couples in the game, along with hundreds of other goodies for you to find."""
    assert actual == expected

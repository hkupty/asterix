# encoding: utf-8
from asterix.core import build_deps_graph, component

def test_single_component():
    deps = {"one": component(set(), lambda: True)}
    assert build_deps_graph(deps) == {None: {"one",}}

def test_complex_component_graph():
    deps = {
        "one": component(set(), lambda: True),
        "two": component(
            {"three", "one"}, lambda *args: True
        ),
        "three": component({"four", "one"}, lambda *args: True),
        "four": component({"one", }, lambda *args: True),
        "five": component({"two", "four"}, lambda *args: True),
        "six": component({"four", "three", "five"}, lambda *args: True),
        "seven": component({"six", "one"}, lambda *args: True),
        "eight": component({"seven", "one", "five"}, lambda *args: True),
    }
    assert build_deps_graph(deps) == {
        None: {"one",},
        'five': {'six', 'eight'},
        'four': {'six', 'five', 'three'},
        'one': {'two', 'eight', 'four', 'seven', 'three'},
        'seven': {'eight'},
        'six': {'seven'},
        'three': {'six', 'two'},
        'two': {'five'}
    }

def test_missing_dependency():
    """The function build_deps_graph does not check dependencies.

    This means the next step will fail, not this one.
    """
    deps = {"one": component({"two",}, lambda: True)}
    assert build_deps_graph(deps) == {"two": {"one",}}

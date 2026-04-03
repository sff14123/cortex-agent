import pytest
from scripts.cortex.skeleton import get_node_skeleton

def test_get_node_skeleton_minimal():
    node_dict = {
        "name": "my_func",
        "signature": "def my_func():",
        "raw_body": '"""My Docstring"""\n    pass'
    }
    result = get_node_skeleton(node_dict, detail="minimal")
    assert result == "my_func"

def test_get_node_skeleton_standard_with_docstring():
    # Test """ docstring
    node_dict = {
        "name": "my_func",
        "signature": "def my_func():",
        "raw_body": '"""My Docstring"""\n    pass'
    }
    result = get_node_skeleton(node_dict, detail="standard")
    assert result == 'def my_func():\n    """My Docstring"""'

    # Test ''' docstring
    node_dict = {
        "name": "my_func",
        "signature": "def my_func():",
        "raw_body": "'''My Docstring'''\n    pass"
    }
    result = get_node_skeleton(node_dict, detail="standard")
    assert result == "def my_func():\n    '''My Docstring'''"

    # Test /* docstring
    node_dict = {
        "name": "myFunc",
        "signature": "void myFunc() {",
        "raw_body": "/* My Docstring */\n    return;"
    }
    result = get_node_skeleton(node_dict, detail="standard")
    assert result == "void myFunc() {\n    /* My Docstring */"

    # Test // docstring
    node_dict = {
        "name": "myFunc",
        "signature": "void myFunc() {",
        "raw_body": "// My Docstring\n    return;"
    }
    result = get_node_skeleton(node_dict, detail="standard")
    assert result == "void myFunc() {\n    // My Docstring"


def test_get_node_skeleton_standard_without_docstring():
    node_dict = {
        "name": "my_func",
        "signature": "def my_func():",
        "raw_body": "    pass"
    }
    result = get_node_skeleton(node_dict, detail="standard")
    assert result == "def my_func():"

def test_get_node_skeleton_full_truncated():
    node_dict = {
        "name": "my_func",
        "signature": "def my_func():",
        "raw_body": "line1\nline2\nline3\nline4\nline5\nline6\nline7"
    }
    result = get_node_skeleton(node_dict, detail="full")
    assert result == "line1\nline2\nline3\nline4\nline5 ... (truncated)"

def test_get_node_skeleton_missing_keys():
    node_dict = {}
    result = get_node_skeleton(node_dict, detail="minimal")
    assert result == "unnamed"

    result = get_node_skeleton(node_dict, detail="standard")
    assert result == ""

    result = get_node_skeleton(node_dict, detail="full")
    assert result == " ... (truncated)"

import pytest
from string_utils import StringUtils 

string_utils = StringUtils()

@pytest.mark.parametrize('string, result', [('test', 'Test'), ('Test', 'Test'), ('1test', '1test')])   
def test_capitilize(string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result

@pytest.mark.parametrize('string, result', [(' test', 'test'), (' Test', 'Test'), (' 1test', '1test'), 
(' test test', 'test test'), ('test', 'test')])  
def test_trim(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result

@pytest.mark.parametrize('string, delimeter, result', [('t,e,s,t', ',',["t", "e", "s", "t"]), 
("1:2:3", ':', ["1", "2", "3"]), ('', ', ', [])])
def test_list_delimeter(string, delimeter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(string, delimeter)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [('test', 't', True), ('test', 'v', False)])
def test_contain_is(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [('test', 's', 'tet'), ('test', 't', 'es'), ('test', '', 'test')])
def test_delete_symbol(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [('test', 't', True), ('test', 's', False), (' test', ' ', True)])
def test_starts_with_true(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [('test', 't', True), ('tests', 't', False), ('test ', ' ', True), ('tests', 't', False)])
def test_end_with_true(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, result', [('test', False), ('', True), ('  ', True), (' test ', False)])
def test_is_empty(string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == result
    
@pytest.mark.parametrize('string, joiner, result', [(['t', 'e', 's', 't'], ', ', 't, e, s, t'), ([1,2,3,4], ", ", "1, 2, 3, 4"), 
(["Sky", "Pro"], ", ", "Sky, Pro"), (["Sky", "Pro"], "-", "Sky-Pro")])
def test_list_to_string(string, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(string, joiner)
    assert res == result



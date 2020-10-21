from unittest.mock import call
import unittest.mock as mock
import merge_the_tools.src.merge_the_tools as m

def test_divide_string():
    string = 'AABCAAADA'
    k = 3
    result = m.divide_string(string, k)
    assert result == ['AAB', 'CAA', 'ADA']

def test_remove_duped():
    string = 'AAB'
    result = m.remove_duped(string)
    assert result == 'AB'

@mock.patch('merge_the_tools.src.merge_the_tools.divide_string')
@mock.patch('merge_the_tools.src.merge_the_tools.remove_duped')
def test_merge_the_tools(mock_remove_duped, mock_divide_string):

    mock_divide_string.return_value = ['AA', 'BB']
    mock_remove_duped.side_effect = ['A', 'B']

    string = 'AABB'
    k = 2
    result = m.merge_the_tools(string, k)

    assert mock_divide_string.call_count == 1
    mock_divide_string.assert_called_with(string, k)
    assert mock_remove_duped.call_count == 2
    mock_remove_duped.assert_has_calls([call('AA'), call('BB')])
    assert result == 'A\nB'

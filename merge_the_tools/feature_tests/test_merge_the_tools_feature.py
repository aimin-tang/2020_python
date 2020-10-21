from merge_the_tools.src import merge_the_tools

def test_merge_the_tools():
    string = 'AABCAAADA'
    k = 3
    result = merge_the_tools.merge_the_tools(string, k)
    assert result == 'AB\nCA\nAD'

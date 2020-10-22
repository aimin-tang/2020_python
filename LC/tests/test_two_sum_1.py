from two_sum_1 import Solution

def test_with_ex1():
    r = Solution().twoSum([2, 7, 11, 15], 9)
    assert r == [0, 1]

def test_with_ex2():
    r = Solution().twoSum([3, 2, 4], 6)
    assert r == [1, 2]

def test_with_ex3():
    r = Solution().twoSum([3, 3], 6)
    assert r == [0, 1]


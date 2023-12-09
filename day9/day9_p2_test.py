import day9_p2

def test_1():
  nums = [10, 13, 16, 21, 30, 45]
  expected = 5
  
  assert day9_p2.extrapolate_2(nums) == expected

def test_2():
  nums = [0, -4, -8, -12]
  expected = 4
  
  assert day9_p2.extrapolate_2(nums) == expected

def test_3():
  nums = [1, 3, 6, 10, 15, 21]
  expected = 0
  
  assert day9_p2.extrapolate_2(nums) == expected

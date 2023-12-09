import day9_p1

def test_1():
  nums = [0, 3, 6, 9, 12, 15]
  expected = 18
  
  assert day9_p1.extrapolate(nums) == expected

def test_2():
  nums = [1, 3, 6, 10, 15, 21]
  expected = 28
  
  assert day9_p1.extrapolate(nums) == expected

def test_3():
  nums = [10, 13, 16, 21, 30, 45]
  expected = 68
  
  assert day9_p1.extrapolate(nums) == expected

def test_4():
  nums = ["0", "-2", "-4", "-6"]
  expected = -8

  assert day9_p1.extrapolate(nums) == expected
  
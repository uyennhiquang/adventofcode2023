import day2_p2

def test_g1():
  s = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
  expected = 48
  actual = day2_p2.power_cubes(s)

  assert actual == expected

def test_g3():
  s = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
  expected = 1560
  actual = day2_p2.power_cubes(s)

  assert actual == expected

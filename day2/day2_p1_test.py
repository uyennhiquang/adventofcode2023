import day2_p1

def test_true():
  s = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
  expected = 1
  actual = day2.if_possible(s)

  assert actual == expected

def test_false():
  s = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
  expected = None
  actual = day2.if_possible(s)

  assert actual == expected
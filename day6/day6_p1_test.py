import day6_p1

def test_calc_ways_1():
  time = 7
  distance = 9
  expected = 4

  assert day6_p1.calc_ways(time, distance) == expected

def test_calc_ways_2():
  time = 15
  distance = 40
  expected = 8

  assert day6_p1.calc_ways(time, distance) == expected

def test_calc_ways_big():
  time = 71530
  distance = 940200

  assert day6_p1.calc_ways(time, distance) == 71503
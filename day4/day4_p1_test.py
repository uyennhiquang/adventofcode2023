import day4_p1

def test_calc_points_winning_nums():
  lines = []
  with open("test_input_1") as f:
    for line in f:
      lines.append(line.strip())

  s = lines[0]

  assert len(day4_p1.calc_points(s)) == 5

def test_calc_points_my_nums():
  lines = []
  with open("test_input_1") as f:
    for line in f:
      lines.append(line.strip())

  s = lines[0]

  assert len(day4_p1.calc_points(s)) == 8

def test_calc_points_1():
  lines = []
  with open("test_input_1") as f:
    for line in f:
      lines.append(line.strip())

  s = lines[0]
  points = day4_p1.calc_points(s)

  assert points == 8

def test_calc_points_2():
  lines = []
  with open("test_input_1") as f:
    for line in f:
      lines.append(line.strip())

  s = lines[2]
  points = day4_p1.calc_points(s)

  assert points == 2

def test_calc_points_no_match():
  lines = []
  with open("test_input_1") as f:
    for line in f:
      lines.append(line.strip())

  s = lines[5]
  points = day4_p1.calc_points(s)

  assert points == 0

      
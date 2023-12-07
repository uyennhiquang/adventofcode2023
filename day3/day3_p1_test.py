import day3_p1

def test_is_symbol_num():
  c = "2"
  assert day3_p1.is_symbol(c) == False

def test_is_symbol_dot():
  c = "."
  assert day3_p1.is_symbol(c) == False

def test_is_symbol_symbol():
  c = "$"
  assert day3_p1.is_symbol(c) == True

def test_is_part_middle_line_middle_nums():
  lines = []
  with open("test_input") as f:
    for line in f:
      lines.append(line.strip())
  line_index = 3

  assert len(day3_p1.is_part(lines, line_index)) == 2
    
def test_is_part_middle_line_middle_nums_2():
  lines = []
  with open("test_input") as f:
    for line in f:
      lines.append(line.strip())
  line_index = 8

  assert len(day3_p1.is_part(lines, line_index)) == 1

def test_is_part_middle_line_begin_nums():
  lines = []
  with open("test_input") as f:
    for line in f:
      lines.append(line.strip())
  line_index = 5

  assert len(day3_p1.is_part(lines, line_index)) == 2

def test_is_part_middle_line_end_nums_1():
  lines = []
  with open("test_input") as f:
    for line in f:
      lines.append(line.strip())
  line_index = 5

  assert len(day3_p1.is_part(lines, line_index)) == 2

def test_is_part_first_line():
  lines = []
  with open("test_input") as f:
    for line in f:
      lines.append(line.strip())
  line_index = 0

  assert len(day3_p1.is_part(lines, line_index)) == 2

def test_is_part_last_line():
  lines = []
  with open("test_input") as f:
    for line in f:
      lines.append(line.strip())
  line_index = len(lines)-1

  assert len(day3_p1.is_part(lines, line_index)) == 2

def test_is_part_first_line_real_input():
  lines = []
  with open("input") as f:
    for line in f:
      lines.append(line.strip())
  line_index = 0

  assert len(day3_p1.is_part(lines, line_index)) == 6

def test_is_part_last_line():
  lines = []
  with open("input") as f:
    for line in f:
      lines.append(line.strip())
  line_index = len(lines)-1

  assert len(day3_p1.is_part(lines, line_index)) == 5
          
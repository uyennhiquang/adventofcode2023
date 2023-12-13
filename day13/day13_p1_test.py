import day13_p1

def test_line_vertical_sym_false():
  line = "#.##..##."
  dividing_index = 0
  expected = False
  
  assert day13_p1.line_vertical_sym(line, dividing_index) == expected


def test_line_vertical_sym_false_2():
  line = "#.#.##.#."
  dividing_index = 0
  expected = False
  
  assert day13_p1.line_vertical_sym(line, dividing_index) == expected

def test_line_vertical_sym_false_3():
  line = "#.##..##."
  dividing_index = 2
  expected = False
  
  assert day13_p1.line_vertical_sym(line, dividing_index) == expected
  
def test_line_vertical_sym_false_4():
  line = "..##..###"
  dividing_index = 6
  expected = False
  
  assert day13_p1.line_vertical_sym(line, dividing_index) == expected
 
def test_line_vertical_sym_true():
  line = "#.##..##."
  dividing_index = 4
  expected = True
  
  assert day13_p1.line_vertical_sym(line, dividing_index) == expected

def test_line_vertical_sym_true_2():
  line = "..#.##.#."
  dividing_index = 4
  expected = True
  
  assert day13_p1.line_vertical_sym(line, dividing_index) == expected

def test_pattern_vertical():
  file = "test_input_vertical"
  pattern = []
  with open(file) as f:
    for line in f:
      pattern.append(line)

  expected = ("v", 5)
  assert day13_p1.pattern_to_num(pattern) == expected

def test_pattern_vertical_sym_false():
  file = "test_input_horizontal"
  pattern = []
  with open(file) as f:
    for line in f:
      pattern.append(line)

  expected = ("h", 400)
  assert day13_p1.pattern_to_num(pattern) == expected

def test_hor_1():
  file = "test_input_1"
  pattern = []
  with open(file) as f:
    for line in f:
      pattern.append(line)

  expected = ("h", 700)
  assert day13_p1.pattern_to_num(pattern) == expected

def test_hor_2():
  file = "test_input_2"
  pattern = []
  with open(file) as f:
    for line in f:
      pattern.append(line)

  expected = ("h", 1200)
  assert day13_p1.pattern_to_num(pattern) == expected
  
def test_ver_1():
  file = "test_input_3"
  pattern = []
  with open(file) as f:
    for line in f:
      pattern.append(line)

  expected = ("v", 12)
  assert day13_p1.pattern_to_num(pattern) == expected


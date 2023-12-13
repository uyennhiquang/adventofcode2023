import day13_p2

def test_line_smudges_one():
  line = "#.##..##."
  i = 0
  expected = 1
  
  assert day13_p2.line_vertical_smudge(line, i) == expected
  # file = "test_input_vertical"
  # pattern = []
  # with open(file) as f:
    # for line in f:
      # pattern.append(line.strip())

def test_line_smudges_none():
  line = "#.##..##."
  i = 4
  expected = 0
  
  assert day13_p2.line_vertical_smudge(line, i) == expected
 
def test_line_smudges_several():
  line = "#.##..##."
  i = 3
  expected = 2
  
  assert day13_p2.line_vertical_smudge(line, i) == expected
 
def test_pattern_1():
  file = "test_input_vertical"
  pattern = []
  with open(file) as f:
    for line in f:
      pattern.append(line.strip())
  expected = ("h", 300)

  assert day13_p2.pattern_to_num(pattern) == expected
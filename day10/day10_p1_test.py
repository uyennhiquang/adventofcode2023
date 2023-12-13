import day10_p1

def test_s_position():
  file = "test_input"
  input_list = []
  with open(file) as f:
    for line in f:
      input_list.append(line.strip())
  
  r, c = day10_p1.messy_to_clean(input_list)

  assert r == 1 and c == 1

def test_1():
  file = "test_input"
  input_list = []
  with open(file) as f:
    for line in f:
      input_list.append(line.strip())
    
  expected = 4
  assert day10_p1.messy_to_clean(input_list) == expected
  
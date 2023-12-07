import day3_p2

def test_middle_true():
  lines = []
  with open("test_input_2") as f:
    for line in f:
      lines.append(line.strip())

  line_index = 1
  assert len(day3_p2.is_part(lines, line_index)) == 1
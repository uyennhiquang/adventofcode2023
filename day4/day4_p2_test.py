import day4_p2

def test_scratch_card_count():
  lines = []
  with open("test_input_1") as f:
    for line in f:
      lines.append(line.strip())

  s = lines[0]
  card_count = day4_p2.calc_scratchcard_copies(s)

  for i in range(1, 6):
    if str(i) not in card_count:
      assert False
  assert True

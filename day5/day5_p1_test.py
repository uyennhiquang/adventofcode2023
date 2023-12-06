import day5_p1

def test_source_destination_types():
  section = []
  with open("test_input") as f:
    next(f)
    next(f)
    for line in f:
      line = line.strip()
      if line == "":
        break
      else:
        section.append(line)
  
  expected_source = "soil"
  expected_destination = "seed"

  actual_source, actual_destination = day5_p1.create_map(section)

  assert actual_source == expected_source
  assert actual_destination == expected_destination

def test_map():
  section = []
  with open("test_input") as f:
    next(f)
    next(f)
    for line in f:
      line = line.strip()
      if line == "":
        break
      else:
        section.append(line)
  
  actual_map = day5_p1.create_map(section)

  assert actual_map[98] == 50
  assert actual_map[50] == 52
  
def test_seed_to_location_1():
  seed = 13
  file = "test_input"
  assert day5_p1.seed_to_location(file, seed) == 35

def test_seed_to_location_2():
  seed = 79
  file = "test_input"
  assert day5_p1.seed_to_location(file, seed) == 82
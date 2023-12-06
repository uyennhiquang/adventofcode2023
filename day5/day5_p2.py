import re

def seed_to_location(file, seed):
  seed = int(seed)
  current = seed

  with open(file) as f:
    next(f)
    next(f)
    a_section = []
    for line in f:
      line = line.strip()
      if line == "":
        a_map = create_map(a_section)

        # If the current number isn't within the current range
        for a_range in a_map:
          the_range = a_map[a_range]
          if current >= the_range["source"] and current <= the_range["source"] + the_range["length"] - 1:
            current = the_range["destination"] + (current - the_range["source"])
            break
          else:
            pass
            
        a_section = []
      else:
        a_section.append(line)
    
    a_map = create_map(a_section)
    
    # If the current number isn't within the current range
    for a_range in a_map:
      the_range = a_map[a_range]
      if current >= the_range["source"] and current <= the_range["source"] + the_range["length"] - 1:
        current = the_range["destination"] + (current - the_range["source"])
        break
      else:
        pass
 
  return current
 
def create_map(section_string):
  a_map = dict()
  range_count = 1

  header = section_string[0]
  source_type = re.findall("(?<=-)[a-z]+(?=\s)", header)[0]
  destination_type = re.findall("^[a-z]+(?=-)", header)[0]

  ranges = section_string[1:]
  for a_range in ranges:
    temp_dict = dict()
    destination_num, source_num, length = a_range.split()

    length = int(length)
    destination_num = int(destination_num)
    source_num = int(source_num)

    temp_dict["source"] = source_num
    temp_dict["destination"] = destination_num
    temp_dict["length"] = length

    a_map[range_count] = temp_dict
    range_count += 1

  return a_map

def maine():
  file = "input"
  locations = []
  with open(file) as f:
    seeds = next(f)
    _, seeds = seeds.split(":")
    seeds = seeds.split()
    seeds = seeds[::-1]
    while len(seeds) != 0:
      start_seed = int(seeds.pop())
      seed_count = int(seeds.pop())
      current_seed = start_seed
      for _ in range(seed_count):
        locations.append(seed_to_location(file, current_seed))
        current_seed += 1
  small = 0
  for location in locations:
    if small == 0:
      small = location
    else:
      if location < small:
        small = location
  print(small, len(locations))

if __name__ == "__main__":
  maine()
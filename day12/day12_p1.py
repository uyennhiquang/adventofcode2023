BROKEN = "#"
OPERATIONAL = "."
UNKNOWN = "?"


def line_to_variation(s):
  record, groups_count = s.strip().split()
  groups_count = groups_count.split(",")
  variations = set()

  # Find a variation
  variation = ""
  current_group = ""
  current_group_index = 0
  current_group_length = int(groups_count[current_group_index])

  for i in range(len(record)):
    if len(current_group) == current_group_length:
      if current_group_index + 1 < len(groups_count):
        current_group_index += 1
      current_group = ""

    current_group_length = int(groups_count[current_group_index])
    if record[i] == UNKNOWN:
      # In the case that we're forming a group 
      if current_group != "":
        if len(current_group + BROKEN) <= current_group_length:
          variation += BROKEN
          current_group += BROKEN
        else:
          variation += OPERATIONAL
      # In the case we're not in the middle of a group formation and the next thing is a broken spring
      elif i+1 < len(record) and record[i+1] == BROKEN:
        if len(BROKEN*2) <= current_group_length:
          variation += BROKEN
          current_group += BROKEN
        else:
          variation += OPERATIONAL
        
    else:
      if record[i] == BROKEN:
        current_group += record[i]
      variation += record[i]

  return variation


def maine():
  pass

if __name__ == "__main__":
  maine()
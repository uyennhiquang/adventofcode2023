ROUNDED_ROCK = "O"
CUBE_ROCK = "#"
EMPTY_SPACE = "."

def sort_load(a_col):
  sorted_load = a_col[:]

  for i in range(1, len(sorted_load)):
    if sorted_load[i] != ROUNDED_ROCK:
      continue
    current_index = i
    while sorted_load[current_index-1] == EMPTY_SPACE:
      sorted_load[current_index], sorted_load[current_index-1] = sorted_load[current_index-1], sorted_load[current_index]
      current_index -= 1
      if current_index <= 0:
        break
  
  return sorted_load

def calc_load(load):
  sum = 0
  for i in range(len(load)):
    if load[i] == ROUNDED_ROCK:
      sum += len(load) - i
  
  return sum

def maine():
  file = "input"
  sum = 0
  loads = dict()

  with open(file) as f:
    for line in f:
      line = line.strip()
      for i in range(len(line)):
        if i not in loads:
          loads[i] = [line[i]]
        else:
          loads[i].append(line[i])
      # loads.append(line.strip())

    for i in loads:
      sorted_load = sort_load(loads[i])
      total = calc_load(sorted_load)
      sum += total
      # sum += calc_load(sort_load(loads[i]))

    print(sum)
      

if __name__ == "__main__":
  maine()
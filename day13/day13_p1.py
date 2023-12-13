# Pattern is a 2d list
def line_vertical_sym(line, i):
  left_index = i
  right_index = i+1

  while left_index - 1 > -2 and right_index + 1 <= len(line):
    if line[left_index] != line[right_index]:
      return False
    left_index -= 1
    right_index += 1
  return True

def pattern_to_num(pattern):
  # Check for vertical mirror
  # If i = 1, then the vertical mirror is between 0,1 and 2 items, so return 2
  # for dividing_index in range(len(pattern[0])-2):
  vertical_symmetry = None
  for dividing_index in range(len(pattern[0].strip())-1):
    for i in range(len(pattern)):
      current_line = pattern[i].strip()
      if line_vertical_sym(current_line, dividing_index) == False:
        vertical_symmetry = False
        break
    
    if vertical_symmetry == False:
      vertical_symmetry = None
      continue 
    if vertical_symmetry == None:
      vertical_symmetry = True
      break
  if vertical_symmetry:
    return "v", dividing_index + 1
  else: 
    horizontal_symmetry = None
    # Check for horizontal mirror
    for dividing_index in range(len(pattern)-1):
      left_index = dividing_index
      right_index = dividing_index + 1
      while left_index - 1 > -2 and right_index + 1 <= len(pattern):
        if pattern[left_index].strip() != pattern[right_index].strip():
          horizontal_symmetry = False
          break
        else:
          left_index -= 1
          right_index += 1
      if horizontal_symmetry == False:
        horizontal_symmetry = None
      elif horizontal_symmetry == None:
        return "h", (dividing_index + 1) * 100
      

def maine():
  file = "input"
  sum = 0
  with open(file) as f:
    pattern = []
    for line in f:
      line = line.strip()
      if line != "":
        pattern.append(line)
      else:
        pos, num = pattern_to_num(pattern)
        # if pos == "v":
          # sum += num
        # elif pos == "h":
          # sum += 
        sum += num
        pattern = []
  pos, num = pattern_to_num(pattern)
  sum += num
  print(sum)
        

if __name__ == "__main__":
  maine()
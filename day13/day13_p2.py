# Pattern is a 2d list
def line_vertical_smudge(line, i):
  left_index = i
  right_index = i+1
  smudges = 0

  while left_index - 1 > -2 and right_index + 1 <= len(line):
    if line[left_index] != line[right_index]:
      smudges += 1
    left_index -= 1
    right_index += 1
    if smudges > 1:
      return smudges

  return smudges

def pattern_to_num(pattern):
  # Check for vertical mirror
  # If i = 1, then the vertical mirror is between 0,1 and 2 items, so return 2
  # for dividing_index in range(len(pattern[0])-2):
  vertical_symmetry = None
  for dividing_index in range(len(pattern[0].strip())-1):
    smudges = 0
    for i in range(len(pattern)):
      current_line = pattern[i].strip()
      smudges += line_vertical_smudge(current_line, dividing_index)
      if smudges > 1:
        vertical_symmetry = False
        break
   
    if vertical_symmetry == False or smudges < 1:
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
      smudges = 0
      left_index = dividing_index
      right_index = dividing_index + 1
      """ 
      In order to determine if the current dividing mirror index is valid, count the number of smudges. A smudge is defined when characters at the same index from each compared line are different. Inside the while loop, which is when we do the pair of lines comparison, if we've counted more than 2 smudges, then there must be no symmetry. After the while loop when we're done counting smudges, if the number of smudge isn't one, then there's also no symmetry with this dividing mirror index.
      """
      while left_index - 1 > -2 and right_index + 1 <= len(pattern) and horizontal_symmetry == None:
        left_line = pattern[left_index].strip()
        right_line = pattern[right_index].strip()
        if left_line != right_line:
          for i in range(len(left_line)):
            if smudges > 1:
              horizontal_symmetry = False
              break
            if left_line[i] != right_line[i]:
              smudges += 1

        # else:
        left_index -= 1
        right_index += 1

      if horizontal_symmetry == False or smudges < 1:
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
def is_symbol(c):
  return not(c.isdigit()) and c != "."

def is_part(lines, line_index):
  part_nums = []
  # line_index = 0
  # line = "467..114.."
  # current_num = "467"

  current_num = ""
  line = lines[line_index]
  current_i = 0
  begin_i = None
  end_i = None
  previous_line = None
  next_line = None
  exist_edge = False
  exist_sandwiched = False 
  if line_index > 0:
    previous_line = lines[line_index-1]
  # If the current processed line is not the last line
  if line_index < len(lines)-1:
    next_line = lines[line_index+1]
 
  for c in line:
    if current_num != "" and not c.isdigit():
      if end_i == None:
        end_i = current_i - 1
        
      # Is a part number if the edge-touching characters are all symbols provided these conditions:
      # 1.The line must not be the first and last line
      # 2.The begin index must not be 0 and the ending index must not be the last index

      # Middle line
      if previous_line != None and next_line != None:
        if begin_i == 0:
          exist_edge = (is_symbol(line[end_i+1]) == True) or (is_symbol(previous_line[end_i+1]) == True) or (is_symbol(next_line[end_i+1]) == True)
        elif end_i == len(line)-1:
          exist_edge = (is_symbol(line[begin_i-1]) == True) or (is_symbol(previous_line[begin_i-1]) == True) or (is_symbol(next_line[begin_i-1]))
        else:
          exist_edge = (is_symbol(line[begin_i-1]) == True or is_symbol(line[end_i+1]) == True) or (is_symbol(previous_line[begin_i-1]) == True or is_symbol(previous_line[end_i+1]) == True) or (is_symbol(next_line[begin_i-1]) == True or is_symbol(next_line[end_i+1]) == True)
          
        if not exist_edge:
          for i in range(begin_i, end_i+1):
            if is_symbol(previous_line[i]) == True or is_symbol(next_line[i]) == True:
              exist_sandwiched = True
              break
      
      # First line 
      elif previous_line == None:
        # Number starting from index 0
        if begin_i == 0:
          exist_edge = (is_symbol(line[end_i+1]) == True) or (is_symbol(next_line[end_i+1]) == True)
        elif end_i == len(line)-1:
          exist_edge = (is_symbol(line[begin_i-1]) == True) or (is_symbol(next_line[begin_i-1]))
        else:
          exist_edge = (is_symbol(line[begin_i-1]) == True or is_symbol(line[end_i+1]) == True) or (is_symbol(next_line[begin_i-1]) == True or is_symbol(next_line[end_i+1]) == True)

        if not exist_edge:
          for i in range(begin_i, end_i+1):
            if is_symbol(next_line[i]) == True:
              exist_sandwiched = True
              break

      elif next_line == None:
        if begin_i == 0:
          exist_edge = (is_symbol(line[end_i+1]) == True) or (is_symbol(previous_line[end_i+1]) == True)
        elif end_i == len(line)-1:
          exist_edge = (is_symbol(line[begin_i-1]) == True) or (is_symbol(previous_line[begin_i-1]) == True)
        else:
          exist_edge = (is_symbol(line[begin_i-1]) == True or is_symbol(line[end_i+1]) == True) or (is_symbol(previous_line[begin_i-1]) == True or is_symbol(previous_line[end_i+1]) == True)
          
        if not exist_edge:
          for i in range(begin_i, end_i+1):
            if is_symbol(previous_line[i]):
              exist_sandwiched = True
              break

      if exist_edge or exist_sandwiched:
        part_nums.append(int(current_num))

      begin_i = None
      end_i = None
      exist_edge = False
      exist_sandwiched = False
      current_num = ""

    if c.isdigit():
      current_num += c
      if begin_i == None:
        begin_i = current_i

    current_i += 1

  # When it reaches the end of the line and there's still a number recorded
  if current_num != "" and current_i == len(line):
    if end_i == None:
      end_i = current_i - 1
    
    # Middle line
    if previous_line != None and next_line != None:
      if begin_i == 0:
        exist_edge = (is_symbol(line[end_i+1]) == True) or (is_symbol(previous_line[end_i+1]) == True) or (is_symbol(next_line[end_i+1]) == True)
      elif end_i == len(line)-1:
        exist_edge = (is_symbol(line[begin_i-1]) == True) or (is_symbol(previous_line[begin_i-1]) == True) or (is_symbol(next_line[begin_i-1]))
      else:
        exist_edge = (is_symbol(line[begin_i-1]) == True or is_symbol(line[end_i+1]) == True) or (is_symbol(previous_line[begin_i-1]) == True or is_symbol(previous_line[end_i+1]) == True) or (is_symbol(next_line[begin_i-1]) == True or is_symbol(next_line[end_i+1]) == True)
          

    # First line 
    elif previous_line == None:
      # Number starting from index 0
      if begin_i == 0:
        exist_edge = (is_symbol(line[end_i+1]) == True) or (is_symbol(next_line[end_i+1]) == True)
      elif end_i == len(line)-1:
        exist_edge = (is_symbol(line[begin_i-1]) == True) or (is_symbol(next_line[begin_i-1]))
      else:
        exist_edge = (is_symbol(line[begin_i-1]) == True or is_symbol(line[end_i+1]) == True) or (is_symbol(next_line[begin_i-1]) == True or is_symbol(next_line[end_i+1]) == True)

      if not exist_edge:
        for i in range(begin_i, end_i+1):
          if is_symbol(next_line[i]) == True:
            exist_sandwiched = True
            break

    elif next_line == None:
      if begin_i == 0:
        exist_edge = (is_symbol(line[end_i+1]) == True) or (is_symbol(previous_line[end_i+1]) == True)
      elif end_i == len(line)-1:
        exist_edge = (is_symbol(line[begin_i-1]) == True) or (is_symbol(previous_line[begin_i-1]) == True)
      else:
        exist_edge = (is_symbol(line[begin_i-1]) == True or is_symbol(line[end_i+1]) == True) or (is_symbol(previous_line[begin_i-1]) == True or is_symbol(previous_line[end_i+1]) == True)

      for i in range(begin_i, end_i+1):
        if is_symbol(previous_line[i]) == True:
          exist_sandwiched = True
          break

    if exist_edge or exist_sandwiched:
      part_nums.append(int(current_num))

  return part_nums

def maine():
  total = 0
  lines = []
  with open("input") as f:
    for line in f:
      line = line.strip()
      lines.append(line)
      # if len(is_part(line)) > 0:
        # nums = is_part(line)
        # for num in nums:
            # total += num
  for i in range(len(lines)):
    nums = is_part(lines, i)
    for num in nums:
      total += num

  print(total)

if __name__ == "__main__":
  maine()
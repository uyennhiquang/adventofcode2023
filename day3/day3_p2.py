GEAR_SYMBOL = "*"

def is_symbol(c):
  return c.isdigit()

def is_part(lines, line_index):
  num1 = ""
  num2 = ""
  part_nums = []
  # line_index = 0
  # line = "467..114.."
  # current_num = "467"

  current_num = ""
  line = lines[line_index]
  current_i = 0
  gear_i = None
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
    if gear_i != None:
        
      # Is a part number if the edge-touching characters are all symbols provided these conditions:
      # 1.The line must not be the first and last line
      # 2.The begin index must not be 0 and the ending index must not be the last index

      # Middle line
      if previous_line != None and next_line != None:
        if gear_i == 0:
          exist_edge = (is_symbol(line[gear_i+1]) == True) or (is_symbol(previous_line[gear_i+1]) == True) or (is_symbol(next_line[gear_i+1]) == True)
        elif gear_i == len(line)-1:
          exist_edge = (is_symbol(line[gear_i-1]) == True) or (is_symbol(previous_line[gear_i-1]) == True) or (is_symbol(next_line[gear_i-1]))
        else:
          exist_edge = (is_symbol(line[gear_i-1]) == True or is_symbol(line[gear_i+1]) == True) or (is_symbol(previous_line[gear_i-1]) == True or is_symbol(previous_line[gear_i+1]) == True) or (is_symbol(next_line[gear_i-1]) == True or is_symbol(next_line[gear_i+1]) == True)
          
        if not exist_edge:
          for i in range(gear_i, gear_i+1):
            if is_symbol(previous_line[i]) == True or is_symbol(next_line[i]) == True:
              exist_sandwiched = True
              break
      
        if exist_edge or exist_sandwiched:
          if gear_i - 3 >= 0 and gear_i + 3 < len(line):
            top_row = previous_line[gear_i-3:gear_i+3]
            bot_row = next_line[gear_i-3:gear_i+3]
            left_row = line[gear_i-3:gear_i]
            right_row = line[gear_i+1:gear_i+4]
          elif gear_i - 3 < 0:
            top_row = previous_line[:gear_i+3]
            bot_row = next_line[:gear_i+3]
            left_row = line[:gear_i]
            right_row = line[gear_i+1:gear_i+4]
          elif gear_i + 3 >= len(line):
            top_row = previous_line[gear_i-3:]
            bot_row = next_line[gear_i-3:]
            left_row = line[gear_i-3:gear_i]
            right_row = line[gear_i+1:]

          for c in left_row:
            # if not c.isdigit() and 
            if c.isdigit():
             if num1 == "":
               num1 += c
             else:
               num2 += c

          for c in right_row:
           if c.isdigit():
            if num1 == "":
              num1 += c
            else:
              num2 += c
            
          # Top and bot
          for i in range(len(top_row)):
            if top_row[i].isdigit():
              if num1 == "":
                num1 += top_row[i]
              else:
                num2 += top_row[i]
            elif bot_row[i].isdigit():
              if num1 == "":
                num1 += bot_row[i]
              else:
                num2 += bot_row[i]
            
      # First line 
      elif previous_line == None:
        # Number starting from index 0
        if gear_i == 0:
          exist_edge = (is_symbol(line[gear_i+1]) == True) or (is_symbol(next_line[gear_i+1]) == True)
        elif gear_i == len(line)-1:
          exist_edge = (is_symbol(line[gear_i-1]) == True) or (is_symbol(next_line[gear_i-1]))
        else:
          exist_edge = (is_symbol(line[gear_i-1]) == True or is_symbol(line[gear_i+1]) == True) or (is_symbol(next_line[gear_i-1]) == True or is_symbol(next_line[gear_i+1]) == True)

        if not exist_edge:
          for i in range(gear_i, gear_i+1):
            if is_symbol(next_line[i]) == True:
              exist_sandwiched = True
              break

      elif next_line == None:
        if gear_i == 0:
          exist_edge = (is_symbol(line[gear_i+1]) == True) or (is_symbol(previous_line[gear_i+1]) == True)
        elif gear_i == len(line)-1:
          exist_edge = (is_symbol(line[gear_i-1]) == True) or (is_symbol(previous_line[gear_i-1]) == True)
        else:
          exist_edge = (is_symbol(line[gear_i-1]) == True or is_symbol(line[gear_i+1]) == True) or (is_symbol(previous_line[gear_i-1]) == True or is_symbol(previous_line[gear_i+1]) == True)
          
        if not exist_edge:
          for i in range(gear_i, gear_i+1):
            if is_symbol(previous_line[i]):
              exist_sandwiched = True
              break


      if num1 != None and num2 != None:
        part_nums.append(int(num1) * int(num2))
      gear_i = None
      exist_edge = False
      exist_sandwiched = False
      num1 = ""
      num2 = ""

    if c == GEAR_SYMBOL:
      # current_num += c
      if gear_i == None:
        gear_i = current_i

    current_i += 1

  # When it reaches the end of the line and there's still a number recorded
  if current_num != "" and current_i == len(line):
    if gear_i == None:
      gear_i = current_i - 1
    
    # Middle line
    if previous_line != None and next_line != None:
      if gear_i == 0:
        exist_edge = (is_symbol(line[gear_i+1]) == True) or (is_symbol(previous_line[gear_i+1]) == True) or (is_symbol(next_line[gear_i+1]) == True)
      elif gear_i == len(line)-1:
        exist_edge = (is_symbol(line[gear_i-1]) == True) or (is_symbol(previous_line[gear_i-1]) == True) or (is_symbol(next_line[gear_i-1]))
      else:
        exist_edge = (is_symbol(line[gear_i-1]) == True or is_symbol(line[gear_i+1]) == True) or (is_symbol(previous_line[gear_i-1]) == True or is_symbol(previous_line[gear_i+1]) == True) or (is_symbol(next_line[gear_i-1]) == True or is_symbol(next_line[gear_i+1]) == True)
          

    # First line 
    elif previous_line == None:
      # Number starting from index 0
      if gear_i == 0:
        exist_edge = (is_symbol(line[gear_i+1]) == True) or (is_symbol(next_line[gear_i+1]) == True)
      elif gear_i == len(line)-1:
        exist_edge = (is_symbol(line[gear_i-1]) == True) or (is_symbol(next_line[gear_i-1]))
      else:
        exist_edge = (is_symbol(line[gear_i-1]) == True or is_symbol(line[gear_i+1]) == True) or (is_symbol(next_line[gear_i-1]) == True or is_symbol(next_line[gear_i+1]) == True)

      if not exist_edge:
        for i in range(gear_i, gear_i+1):
          if is_symbol(next_line[i]) == True:
            exist_sandwiched = True
            break

    elif next_line == None:
      if gear_i == 0:
        exist_edge = (is_symbol(line[gear_i+1]) == True) or (is_symbol(previous_line[gear_i+1]) == True)
      elif gear_i == len(line)-1:
        exist_edge = (is_symbol(line[gear_i-1]) == True) or (is_symbol(previous_line[gear_i-1]) == True)
      else:
        exist_edge = (is_symbol(line[gear_i-1]) == True or is_symbol(line[gear_i+1]) == True) or (is_symbol(previous_line[gear_i-1]) == True or is_symbol(previous_line[gear_i+1]) == True)

      for i in range(gear_i, gear_i+1):
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

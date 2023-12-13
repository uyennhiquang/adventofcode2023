up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)
GROUND = "."
STARTING = "S"

pipe_to_direction = {
  "|": [up, down],
  "-" : [left, right],
  "L": [up, right],
  "J": [up, left],
  "7": [left, down],
  "F": [right, down],
}

def messy_to_clean(input_list):
  clean = [["" for __ in range(len(input_list[0]))] for _ in range(len(input_list))]
  s_row = None
  s_col = None
  
  # Find the position of starting
  for row_num in range(len(input_list)):
    if STARTING not in input_list[row_num]:
      continue
    else:
      for col_num in range(len(input_list[row_num])):
        if input_list[row_num][col_num] == STARTING:
          s_row = row_num
          s_col = col_num

  # return s_row, s_col
  starting = [s_row, s_col]
  current = [None, None]
  next_pos = [None, None]
  steps = 0

  # Walk 
  while current != starting:
    if current[0] == None and current[1] == None:
      current = starting[:]
      
      # Gets the item to be used to determine if the item connects to the starting position
      up_thing = input_list[current[0]-1][current[1]]
      left_thing = input_list[current[0]][current[1]-1]
      down_thing = input_list[current[0]+1][current[1]]
      right_thing = input_list[current[0]][current[1]+1]

      if down in pipe_to_direction[up_thing]:
        # Go up
        next_pos[0] = current[0] - 1
        next_pos[1] = current[1]
        connection = down
      elif right in pipe_to_direction[left_thing]:
        # Go left
        next_pos[0] = current[0]
        next_pos[1] = current[1] - 1
        connection = right
      elif up in pipe_to_direction[down_thing]:
        # Go down
        next_pos[0] = current[0] + 1
        next_pos[1] = current[1]
        connection = up
      elif left in pipe_to_direction[right_thing]:
        # Go right
        next_pos[0] = current[0]
        next_pos[1] = current[1] + 1
        connection = left
    
    else:
      current_row = current[0]
      current_col = current[1]
      a_pipe = input_list[current_row][current_col]

      for direction in pipe_to_direction[a_pipe]:
        if direction == connection:
          continue
        else:
          next_pos[0] += direction[0]
          next_pos[1] += direction[1]
          if direction == right:
            connection = left

          elif direction == left:
            connection = right
          elif direction == up:
            connection = down
          else:
            connection = up
          break
          # for a_direction in pipe_to_direction[a_pipe]:
            # if direction != a_direction:
              # connection = a_direction
      
    current = next_pos[:]
    steps += 1
    
  return (steps) // 2
 
def maine():
  file = "input"
  input_list = []
  with open(file) as f:
    for line in f:
      input_list.append(line.strip())
  print(messy_to_clean(input_list))


if __name__ == "__main__":
  maine()
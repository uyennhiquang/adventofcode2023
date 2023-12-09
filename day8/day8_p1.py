import re

START_NODE = "AAA"
END_NODE = "ZZZ"

def steps(file):
  steps = 0
  i = 0
  node_dict = dict()
  current_node = START_NODE
  
  with open(file) as f:
    instruction = next(f).strip()
    next(f)

    for line in f:
      line = line.strip()
      name, left, right = re.findall("[A-Z]{3}", line)
      node_dict[name] = {
        "L": left,
        "R": right
      }
  while current_node != END_NODE:
    if i >= len(instruction):
      i = 0
    
    direction = instruction[i]
    current_node = node_dict[current_node][direction]
    i += 1
    steps += 1

  return steps
    
def maine():
  file = "input"
  print(steps(file))

if __name__ == "__main__":
  maine()
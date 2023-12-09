import re

def steps(file):
  steps = 0
  i = 0
  current_nodes = []
  z_count = 0
  node_dict = dict()
  
  with open(file) as f:
    instruction = next(f).strip()
    next(f)

    for line in f:
      line = line.strip()
      name, left, right = re.findall("[\dA-Z]{3}", line)
      node_dict[name] = {
        "L": left,
        "R": right
      }
      if len(re.findall("^.{2}A",  name)) != 0:
        current_nodes.append(name)

  while z_count != len(current_nodes):
    z_count = 0
    if i >= len(instruction):
      i = 0
    
    direction = instruction[i]
    next_nodes = []
    for current_node in current_nodes:
      next_node = node_dict[current_node][direction]
      if len(re.findall("^.{2}Z", next_node)) != 0:
        z_count += 1
      next_nodes.append(next_node)

    current_nodes = next_nodes
      
    i += 1
    steps += 1

  return steps
    
def maine():
  file = "input"
  print(steps(file))

if __name__ == "__main__":
  maine()
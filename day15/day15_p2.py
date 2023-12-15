import re

def hashmap(s):
  # example: 
  # rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
  a_map = dict()
  steps = s.split(",")
  for step in steps:
    label = re.findall("[a-z]+(?<=)", step)[0]
    key = hash_advent(label)

    # If the step is removal
    if step[len(step)-1] == "-":
      if key not in a_map:
        continue
      elif label not in a_map[key]:
        continue
      else:
        # Access which box the lens is it
        # Get the index of the lens
        # Iterate over the box and decrement every len whose index is larger than the popped lens
        a_map[key]["count"] -= 1
        popped_lens_index = a_map[key][label]["index"]
        a_map[key].pop(label)
        for a_label in a_map[key]:
          if type(a_map[key][a_label]) == type(dict()):
            if a_map[key][a_label]["index"] > popped_lens_index:
              a_map[key][a_label]["index"] -= 1
            
    else:
      a_length = int(step[len(step)-1])
      if key not in a_map:
        # a_map[key] = [label+ " " + step[len(step)-1]]
        a_map[key] = {
          "count": 1,
          label: {
            "length": a_length
          }
        }
        a_map[key][label]["index"] = a_map[key]["count"] - 1

      else:
        # If current label is a duplicate, replace it
        if label in a_map[key]:
          a_map[key][label]["length"] = a_length
        else:
          a_map[key]["count"] += 1
          a_map[key][label] = {
            "length": a_length,
          }
          a_map[key][label]["index"] = a_map[key]["count"] - 1
  
  return a_map
        
def hash_advent(s):
  val = 0
  for c in s:
    val += ord(c)
    val *= 17
    val = val % 256
  return val
    
def maine():
  # print(hash_advent("pc"))
  # a_map = hashmap("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7")
  file = "input"
  with open(file) as f:
    for line in f:
      steps = line.strip()

  a_map = hashmap(steps)
  sum = 0
  for box in a_map:
    if a_map[box]["count"] == 0:
      continue
    else:
      for label in a_map[box]:
        if type(a_map[box][label]) == type(dict()):
          sum += (box+1) * (a_map[box][label]["index"] + 1) * a_map[box][label]["length"]
  
  print(sum)


if __name__ == "__main__":
  maine()
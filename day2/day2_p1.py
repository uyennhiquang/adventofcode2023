import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def if_possible(s):
  game_id = re.findall("(?<=Game\s)\d+", s)[0]

  reds = re.findall("\d+(?=\sred)", s)
  greens = re.findall("\d+(?=\sgreen)", s)
  blues = re.findall("\d+(?=\sblue)", s)

  for red in reds:
    if int(red) > MAX_RED:
      return None
  for green in greens:
    if int(green) > MAX_GREEN:
      return None
  for blue in blues:
    if int(blue) > MAX_BLUE:
      return None
  return int(game_id) 

def maine():
  total = 0
  with open("input") as f:
    for line in f:
      line = line.strip()
      if if_possible(line) != None:
        total += if_possible(line)
      
  print(total)

if __name__ == "__main__":
  maine()
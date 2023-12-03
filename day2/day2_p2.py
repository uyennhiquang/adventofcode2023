import re

def power_cubes(s):
  max_red = 0
  max_green = 0
  max_blue = 0

  reds = re.findall("\d+(?=\sred)", s)
  greens = re.findall("\d+(?=\sgreen)", s)
  blues = re.findall("\d+(?=\sblue)", s)

  for red in reds:
    if int(red) > max_red:
      max_red = int(red)

  for green in greens:
    if int(green) > max_green:
      max_green = int(green)

  for blue in blues:
    if int(blue) > max_blue:
      max_blue = int(blue)

  return max_red * max_green * max_blue
  
def maine():
  total = 0
  with open("input") as f:
    for line in f:
      line = line.strip()
      total += power_cubes(line)

  print(total)

if __name__ == "__main__":
  maine()
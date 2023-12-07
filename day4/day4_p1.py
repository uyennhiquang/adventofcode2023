import re

def calc_points(s):
  base = 2
  count = 0
  winning_nums = set(re.findall("(?<=:\s).+(?=\s\|)", s)[0].split())
  my_nums = re.findall("(?<=\|\s).+", s)[0].split()

  for num in my_nums:
    if num in winning_nums:
      count += 1

  points = 2 ** (count - 1)
  if points < 1:
    return 0
  return points

  # return winning_nums
  
def maine():
  sum = 0
  with open("input") as f:
    for line in f:
      s = line.strip()
      sum += calc_points(s)
  print(sum)

if __name__ == "__main__":
  maine()
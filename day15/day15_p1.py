def hash_advent(s):
  val = 0
  for c in s:
    val += ord(c)
    val *= 17
    val = val % 256
  return val
    
def maine():
  file = "input" 
  with open(file) as f:
    for line in f:
      inputs = line.strip().split(",")
  sum = 0
  for elt in inputs:
    sum += hash_advent(elt)
  print(sum)
    

if __name__ == "__main__":
  maine()
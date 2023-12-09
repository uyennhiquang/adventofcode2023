def extrapolate(nums):
  # zero_count = None
  extrap = int(nums[len(nums)-1])
  all_zero = None
  while True:
    temp_nums = []
    # construct the temporary nums
    for i in range(len(nums)-1):
      diff = int(nums[i+1]) - int(nums[i])
      if diff != 0:
        all_zero = False
      temp_nums.append(diff)
    
    if all_zero == None:
      break

    nums = temp_nums
    extrap += nums[len(nums)-1]
    all_zero = None

  return extrap
        
def maine():
  sum = 0
  with open("input") as f:
    for line in f:
      sum += extrapolate(line.strip().split())

  print(sum)
    

if __name__ == "__main__":
  maine()
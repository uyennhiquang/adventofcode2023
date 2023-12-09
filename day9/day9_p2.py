def extrapolate_2(nums, all_zero=None):
  if all_zero == True:
    return 0
  else:
    temp_nums = []
    for i in range(len(nums)-1):
      diff = int(nums[i+1]) - int(nums[i])
      if diff != 0:
        all_zero = False
      temp_nums.append(diff)
    
    if all_zero == None:
      all_zero = True
    else:
      all_zero = None

    return int(nums[0]) - extrapolate_2(temp_nums, all_zero)

def maine():
  sum = 0
  with open("input") as f:
    for line in f:
      sum += extrapolate_2(line.strip().split())
# 
  print(sum)

  # nums = [0, 3, 6, 9]
  # print(extrapolate_2(nums))
    
if __name__ == "__main__":
  maine()
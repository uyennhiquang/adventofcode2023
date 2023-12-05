import re

def calc_scratchcard_copies(s):
  count = 0
  current_card = int(re.findall("\d+(?=:)", s)[0])
  scratch_card_nums = [str(current_card)]

  winning_nums = set(re.findall("(?<=:\s).+(?=\s\|)", s)[0].split())
  my_nums = re.findall("(?<=\|\s).+", s)[0].split()

  for num in my_nums:
    if num in winning_nums:
      count += 1
      scratch_card_nums.append(str(current_card+count))

  return scratch_card_nums
  
def maine():
  winning_copies = dict()
  total_cards = 0
  with open("input") as f:
    for line in f:
      s = line.strip()
      current_card = re.findall("\d+(?=:)", s)[0]
      winning_cards = calc_scratchcard_copies(s)
      # winning_copies[current_card] = 1

      for winning_card in winning_cards:
        if winning_card not in winning_copies: 
          winning_copies[winning_card] = 1

        elif winning_card == current_card:
          winning_copies[winning_card] += 1
          winning_cards = winning_cards[1:]
          for winning_card_dupes in winning_cards:
            if winning_card_dupes not in winning_copies: 
              winning_copies[winning_card_dupes] = 1 * winning_copies[current_card]
            else:
              winning_copies[winning_card_dupes] += 1 * winning_copies[current_card]

          break

        else:
          winning_copies[winning_card] += 1
          
  for winning_card in winning_copies:
    total_cards += winning_copies[winning_card]
  print(total_cards)

if __name__ == "__main__":
  maine()
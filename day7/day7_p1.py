import re

RANKS = ["A", "K", "Q","J", "T", "9", "8", "7", "6", "5", "4", "3","2"]
RANKS_TO_STRENGTH = dict()
for i in range(len(RANKS)):
  RANKS_TO_STRENGTH[RANKS[i]] = len(RANKS) - i

TYPE_TO_STRENGTH = {
  "fik": 7,
  "fok": 6,
  "fh": 5,
  "tk": 4,
  "tp": 3,
  "op": 2,
  "hc": 1
}

class Card:
  __slots__ = ["__name", "__type", "__bid"]
  
  def __init__(self, name, bid=0):
    self.__name = name
    self.__bid = bid
    if len(set(name)) == 1:
      self.__type = "fik"
    elif len(set(name)) == len(name):
      self.__type = "hc"
    elif len(set(name)) == len(name) - 1:
      self.__type = "op"
    elif len(set(name)) == 1+1:
      temp_dict = dict()
      for c in name:
        if c not in temp_dict:
          temp_dict[c] = 1
        else:
          temp_dict[c] += 1
      for key in temp_dict:
        if temp_dict[key] == 1 or temp_dict[key] == 4:
          self.__type = "fok"
          break
        else:
          self.__type = "fh"
          break
    else:
      temp_dict = dict()
      for c in name:
        if c not in temp_dict:
          temp_dict[c] = 1
        else:
          temp_dict[c] += 1
      for key in temp_dict:
        if temp_dict[key] == 2:
          self.__type = "tp"
          break
        elif temp_dict[key] == 3:
          self.__type = "tk"
          break
        else: 
          continue

        
  def get_name(self):
    return self.__name

  def get_type(self):
    return self.__type
    
  def __repr__(self):
    return self.__name

  def __lt__(self, other):
    if type(self) == type(other):
      if self.get_type() != other.get_type():
        return TYPE_TO_STRENGTH[self.get_type()] < TYPE_TO_STRENGTH[other.get_type()]
      else:
        i = 0
        while self.get_name()[i] == other.get_name()[i]:
          i += 1
        return RANKS_TO_STRENGTH[self.get_name()[i]] < RANKS_TO_STRENGTH[other.get_name()[i]]
          
      
    raise ValueError("Wrong type!")
    
  
  def calc_bid(self, rank):
    return self.__bid * rank
  # regex = "|".join(RANKS)
  # ranks_captured = re.findall(regex, s)
  # ex:
  # {  }
  
def maine():
  sum = 0
  cards = []
  with open("input") as f:
    for line in f:
      line = line.strip()
      name, bid = line.split()
      cards.append(Card(name, int(bid)))
  cards = sorted(cards)
  for i in range(len(cards)):
    sum += cards[i].calc_bid(i+1)
  print(sum)
  # print(RANKS_TO_STRENGTH)


if __name__ == "__main__":
  maine()
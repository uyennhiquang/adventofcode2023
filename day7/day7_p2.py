import re

RANKS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3","2", "J"]
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
  
  def __set_type(self):
    if len(set(self.__name)) == 1:
      self.__type = "fik"
    elif len(set(self.__name)) == len(self.__name):
      self.__type = "hc"
    elif len(set(self.__name)) == len(self.__name) - 1:
      self.__type = "op"
    elif len(set(self.__name)) == 1+1:
      temp_dict = dict()
      for c in self.__name:
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
      for c in self.__name:
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
    
  def __init__(self, name, bid=0):
    self.__name = name
    self.__bid = bid
    self.__set_type()
    if "J" in set(name) and len(set(name)) != 1:
      temp_dict = dict()
      for i in range(len(name)):
        if name[i] not in temp_dict:
          temp_dict[name[i]] = {
            "count": 1,
            "indices": [i]
          }
        else:
          temp_dict[name[i]]["count"] += 1
          temp_dict[name[i]]["indices"].append(i)
          
      most_rank = ""
      most = 0
      for key in temp_dict:
        if temp_dict[key]["count"] > most and key != "J":
          most = temp_dict[key]["count"]
          most_rank = key
      temp_name = list(name)
      for i in temp_dict["J"]["indices"]:
        temp_name[i] = most_rank
      temp_name = "".join(temp_name)

      self.__name = temp_name
      self.__set_type()
      self.__name = name

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

if __name__ == "__main__":
  maine()
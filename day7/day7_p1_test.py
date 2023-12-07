import day7_p1

def test_make_card_fik():
  s = "AAAAA"
  card = day7_p1.Card(s)

  assert card.get_name() == s
  assert card.get_type() == "fik"
  
def test_make_card_fok():
  s = "AA8AA"
  card = day7_p1.Card(s)

  assert card.get_name() == s
  assert card.get_type() == "fok"
   
def test_make_card_fh():
  s = "23332"
  card = day7_p1.Card(s)

  assert card.get_name() == s
  assert card.get_type() == "fh"

def test_make_card_tk():
  s = "TATT2"
  card = day7_p1.Card(s)

  assert card.get_name() == s
 
def test_make_card_tp():
  s = "23432"
  card = day7_p1.Card(s)

  assert card.get_name() == s
  assert card.get_type() == "tp"

  assert card.get_type() == "tp"

def test_compare_diff_type():
  card1 = day7_p1.Card("23332")
  card2 = day7_p1.Card("234AT")

  assert card1 > card2

def test_compare_same_type():
  card1 = day7_p1.Card("77888")
  card2 = day7_p1.Card("77788")

  assert card1 > card2

def test_total_bids():
  file = "test_input"
  cards = []
  with open(file) as f:
    for line in f:
      line = line.strip()
      name, bid = line.split()
      cards.append(day7_p1.Card(name, int(bid)))

  sum = 0
  cards = sorted(cards)
  for i in range(len(cards)):
    sum += cards[i].calc_bid(i+1)

  assert sum == 6440
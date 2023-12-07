import day7_p2

def test_occur_twice():
  name = "KK53J"
  card = day7_p2.Card(name)

  assert card.get_type() == "tk"

def test_occur_mult_j():
  name = "23JJJ"
  card = day7_p2.Card(name)

  assert card.get_type() == "fok"
  assert card.get_name() == name
 
def test_occur_unique():
  name = "2341J"
  card = day7_p2.Card(name)

  assert card.get_type() == "op"
 
def test_same_occur_twice():
  name = "KK55J"
  card = day7_p2.Card(name)

  assert card.get_type() == "fh"
  
def test_fok_1():
  name = "T55J5"
  card = day7_p2.Card(name)
  
  assert card.get_type() == "fok"
  
def test_input():
  file = "test_input"
  expected = 5905
  sum = 0
  cards = []

  with open(file) as f:
    for line in f:
      name, bid = line.strip().split()
      cards.append(day7_p2.Card(name, int(bid)))
  cards = sorted(cards)

  for i in range(len(cards)):
    sum += cards[i].calc_bid(i+1)

  assert sum == expected

# tests a bunch of Js
def test_j1_tk():
  card = day7_p2.Card("6JA22")
  assert card.get_type() == "tk"
  assert card.get_name() == "6JA22"

def test_j2_fh():
  card = day7_p2.Card("25J52")
  assert card.get_type() == "fh"

def test_j3_op():
  card = day7_p2.Card("5TK4J")
  assert card.get_type() == "op"

def test_j5_fik():
  card = day7_p2.Card("9J999")
  assert card.get_type() == "fik"

def test_j6_tk():
  card = day7_p2.Card("J73JK")
  assert card.get_type() == "tk"
  
def test_j7_fik():
  card = day7_p2.Card("JJJJJ")
  assert card.get_type() == "fik"
  
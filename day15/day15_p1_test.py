import day15_p1

def test_hash_1():
  s = "rn=1"
  expected = 30
  
  assert day15_p1.hash_advent(s) == expected
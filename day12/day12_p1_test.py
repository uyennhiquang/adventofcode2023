import day12_p1

def test_single_variation():
  s = "?#?#?#?#?#?#?#? 1,3,1,6"
  expected = ".#.###.#.######"

  assert day12_p1.line_to_variation(s) == expected
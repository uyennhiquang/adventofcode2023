import day14_p1

def test_sort_load_1():
  load = list("OO.O.O..##")
  expected = list("OOOO....##")

  assert day14_p1.sort_load(load) == expected

def test_sort_load_2():
  load = list(".O...#O..O")
  expected = list("O....#OO..")

  assert day14_p1.sort_load(load) == expected

def test_sort_load_3():
  load = list(".O.#......")
  expected = list("O..#......")

  assert day14_p1.sort_load(load) == expected
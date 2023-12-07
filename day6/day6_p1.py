def calc_ways(time, distance):
  time_held = 2
  boat_speed = time_held
  distance_travelled = (time - time_held) * boat_speed
  ways = 0

  for time_held in range(1, time):
    distance_travelled = (time - time_held) * time_held
    if distance_travelled > distance: 
      ways += 1

  return ways

def maine():
  prod = 1
  with open("day6/input") as f:
    data = []
    for line in f:
      data.append(line)
    times = data[0].split()
    times = times[1:]
    time = int("".join(times))

    distances = data[1].split()
    distances = distances[1:]
    distance = int("".join(distances))

    # for i in range(len(times)):
      # time = int(times[i])
      # distance = int(distances[i])
      # prod *= calc_ways(time, distance)
    # print(time, distance)

  print(calc_ways(time, distance))

if __name__ == "__main__":
  maine()
i = 0
while i < 5:
  print("Looping!")
  i += 1
  for i in range(10):
    print("Looping!")
    print(f"i is: {i}")

player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]
inch_heights = list()
# for height in player_heights:
#     inch_height = height * 7920
#     inch_heights.append(inch_height)
inch_heights = [height * 7920 for height in player_heights]
player_heights = [height * 7920 for height in player_heights]
print(player_heights)
print(inch_heights)
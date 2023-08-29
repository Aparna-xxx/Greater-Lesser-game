import art
import game_data
import random

count = 0
data = game_data.data
print(art.logo)
print("Is B greater than or less than A?(greater/lesser)")


def check(a, b, ans):
  if (ans == "greater"
      and data[b]["follower_count"] > data[a]["follower_count"]):
    return True
  elif (ans == "lesser"
        and data[b]["follower_count"] < data[a]["follower_count"]):
    return True
  else:
    return False


result = True
game_length = len(data)
b = random.randint(0, game_length - 1)
while (result == True):
  a = b
  while (b == a):
    b = random.randint(0, game_length - 1)
  #print(b)
  print("A: ", data[a]["name"], ", ", data[a]["description"], ", ",
        data[a]["country"])

  print(art.vs)

  print("B: ", data[b]["name"], ", ", data[b]["description"], ", ",
        data[b]["country"])
  ans = input()
  print(result)
  result = check(a, b, ans)
  if (result == False):
    print("You lose")
    print("Your Score: ", count)
  else:
    count += 1


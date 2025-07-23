name = input("Hi What is your name ?")
print(f"Hi, nice to meet you {name}")
age_input = input("What is your age ?")
age = int(age_input)
age_bot = 22
age_difference = age - age_bot
if age > 22:
  print(f"You are {age_difference} years older than me")
if age < 22:
  print(f"You are {age_difference} years younger than me")
if age == 22:
  print("You are the same age as me")
from art import logo
import random

def check_ans(guess, ans):
  if guess == ans:
    print(f"You got it! The answer was {ans}")
  elif guess > ans:
    print("Too high.")
  elif guess < ans:
    print("Too low.")

ans = random.randint(1, 100)

print(logo)
print(f'''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Pssst, the correct answer is {ans}''')
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == 'easy':
  attempt = 10
else:
  attempt = 5
# print(f"You have {attempt} attempts remaining to guess the number")

game_is_over = False

while not game_is_over:
  print(f"You have {attempt} attempts remaining to guess the number")  
  guess = int(input("Make a guess:"))
  check_ans(guess, ans)

  if guess == ans:
    break
  
  attempt -= 1
  if attempt == 0:
    print("You've run out of guesses, you lose.")
    break
  print("Guess again.")

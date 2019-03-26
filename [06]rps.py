import secrets

player = input("choose one(rock/paper/scissors): ")

variants = ['rock', 'paper', 'scissors']

computer = secrets.choice(variants)

if player == computer:
    print("computer shows: " + computer + "tie")
elif (player == 'rock' and computer != 'paper')\
    or (player == 'paper' and computer != 'scissors')\
    or (player == 'scissors' and computer != 'rock'):
    print("computer shows: " + computer + ", You win!")
else:
    print("Computer shows: " + computer + ", You lost!")

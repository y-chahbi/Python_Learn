import random

Data = {1: "✊", 2: "✋", 3: "✌"}

Parts = """===================
Rock Paper Scissors
===================
1 is for “✊” (Rock).
2 is for “✋” (Paper).
3 is for “✌” (Scissors).
Pick a number: """;

PlayerChoise = int(input(Parts));

if PlayerChoise > 3:
    PlayerChoise = 1;

ComputerChoise = int(random.randint(1, 3));

print("You chose: " + Data[PlayerChoise]);
print("CPU chose: " + Data[ComputerChoise]);

if PlayerChoise == ComputerChoise:
    print("It's a tie!");
elif (PlayerChoise - ComputerChoise) % 3 == 1:
    print("You win!")
else:
    print("Computer wins!")

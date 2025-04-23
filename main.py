import random

def play_game():
    print(" Welcome to the SI Mall!")
    print("Can you guess if it's a Profit, Loss Or no Profit?\n")

     # List of sample items
    items = ["Toy Car", "Ice cream","Notebook" "Ball", "Water Bottle"]

    for round_num in range(1, 4):
        item = random.choice(items)
        cp = random.randin(10, 100)
        sp = random.randin(10, 100)

        print(f"\nRound {round_num}: You sold a {item}!")
        print(f"Cost Price (CP): ${cp}")
        print(f"Selling price (SP): ${cp}")

        guess = input("What is it? (profit/loss/none): ").lower()

        # Check actual price
        if sp > cp:
            correct = "profit"
        elif sp < cp:
            correct = "loss"
        
        if guess == correct:
            print(" ✅Correct! Great Job")
        else:
            print(f"❌ Oops! It's actually a {correct}.")

    print("\n Game over! Thanks for playing!")

    # Start the game
    play_game
    
    




import random
import pandas as pd

# Initialize score data
score_data = {"User Wins": 0, "Computer Wins": 0, "Ties": 0}
score_df = pd.DataFrame([score_data])

# List of valid items
item_list = ["rock", "paper", "scissors"]

print("🎮 Welcome to Rock-Paper-Scissors Game!")
print("Type 'quit' anytime to end the game.\n")

# Game loop
while True:
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()

    # Check if user wants to quit
    if user_choice == "quit":
        print("\n🏁 Final Scorecard:")
        print(score_df)

        # Save score to Excel file
        score_df.to_excel("rps_score.xlsx", index=False)
        print("\n💾 Score saved successfully in 'rps_score.xlsx'")
        print("\nThanks for playing! 👋")
        break

    # Validate input
    if user_choice not in item_list:
        print("⚠️ Invalid choice! Please choose rock, paper, or scissors.\n")
        continue

    # Computer makes a choice
    comp_choice = random.choice(item_list)
    print(f"\n🖥️ Computer chose: {comp_choice}")

    # Determine the result
    if user_choice == comp_choice:
        print("It's a tie! 🤝")
        score_df.loc[0, "Ties"] += 1
    elif (
        (user_choice == "rock" and comp_choice == "scissors")
        or (user_choice == "paper" and comp_choice == "rock")
        or (user_choice == "scissors" and comp_choice == "paper")
    ):
        print("You win! 🎉")
        score_df.loc[0, "User Wins"] += 1
    else:
        print("You lose! 😢")
        score_df.loc[0, "Computer Wins"] += 1

    # Display current score
    print("\n📊 Current Score:")
    print(score_df)
    print("-" * 40)

    # Auto-save after every round (optional)
    score_df.to_excel("rps_score.xlsx", index=False)
    print("💾 Score auto-saved!\n")

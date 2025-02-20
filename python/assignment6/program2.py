import random

class Rock_paper_scissors:
    choices = ["rock", "paper", "scissors"]
    
    def __init__(self, rounds):
        self.total_rounds = rounds
        self.current_round = 1
        self.user_wins = 0
        self.computer_wins = 0
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.user_wins += 1
            return "user"
        else:
            self.computer_wins += 1
            return "computer"
    
    def has_winner(self):
        return self.user_wins > self.total_rounds // 2 or self.computer_wins > self.total_rounds // 2
    
    def play_round(self, user_choice):
        if self.current_round > self.total_rounds:
            return "Game over!"
        
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)
        
        self.current_round += 1
        return {
            "user_choice": user_choice,
            "computer_choice": computer_choice,
            "round_winner": result,
            "user_wins": self.user_wins,
            "computer_wins": self.computer_wins,
            "game_winner": "user" if self.has_winner() and self.user_wins > self.computer_wins else \
                            "computer" if self.has_winner() else None
        }
    
n=int(input("enter number of rounds you want to play"))
game = Rock_paper_scissors(n)
for i in range(n):
    print("press:")
    print("1. For rock")
    print("2. For scissors")
    print("3. For paper")
    c=int(input("enter choice:"))
    match c:
        case 1:
            result=game.play_round("rock")
        case 2:
            reuslt=game.play_round("scissors")
        case 3:
            result=game.play_round("paper")

print(result)
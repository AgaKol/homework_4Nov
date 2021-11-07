import random

from models.player import Player

class Game:
    def __init__(self):
        self.choices = {
            "paper" : "rock",
            "rock" : "scissors",
            "scissors" : "paper"
        }

    def play_game(self, player1, player2):
        winner = 0
        if self.choices[player1.choice.lower()] == player2.choice.lower():
            winner = player1
        elif self.choices[player2.choice.lower()] == player1.choice.lower():
            winner = player2
        else:
            winner = None
        return winner

    def computer(self):
        computer_choices = ["rock", "paper", "scissors"]
        computer_action = random.choice(computer_choices)
        computer = Player("Computer", computer_action)
        return computer
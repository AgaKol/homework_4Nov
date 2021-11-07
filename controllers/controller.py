from app import app
from flask import render_template, request
from models.player import Player
from models.game import Game

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/<player1_choice>/<player2_choice>")
def play_game(player1_choice, player2_choice):
    player1 = Player("Player 1", player1_choice)
    player2 = Player("Player 2", player2_choice)
    game = Game()
    winner = game.play_game(player1, player2)
    return render_template("result.html", player1 = player1, player2 = player2, winner=winner)

@app.route("/play")
def player_vs_computer():
    return render_template("play.html")

@app.route("/result", methods=["POST"])
def computer_results():
    name = request.form["name"]
    choice = request.form["choice"]
    game = Game()
    player1 = Player(name, choice)
    player2 = game.computer()
    winner = game.play_game(player1,player2)
    return render_template("result.html", player1 = player1, player2=player2, winner=winner)
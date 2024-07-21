import numpy as np
from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)
player_wins = 0
ai_wins = 0


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None


def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


def best_move(board):
    best_eval = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                eval = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    move = (i, j)
    return move


@app.route('/')
def index():
    return render_template('index.html', player_wins=player_wins, ai_wins=ai_wins)


@app.route('/move', methods=['POST'])
def move():
    global player_wins, ai_wins
    board = request.json['board']
    move = best_move(board)

    if move:
        board[move[0]][move[1]] = "O"
    winner = check_winner(board)
    if winner == "X":
        player_wins += 1
    elif winner == "O":
        ai_wins += 1

    return jsonify({'move': move, 'winner': winner, 'player_wins': player_wins, 'ai_wins': ai_wins})


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)
player_wins = 0
ai_wins = 0


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None


def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


def best_move(board):
    best_eval = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                eval = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    move = (i, j)
    return move


@app.route('/')
def index():
    return render_template('index.html', player_wins=player_wins, ai_wins=ai_wins)


@app.route('/move', methods=['POST'])
def move():
    global player_wins, ai_wins
    board = request.json['board']
    move = best_move(board)

    if move:
        board[move[0]][move[1]] = "O"
    winner = check_winner(board)
    if winner == "X":
        player_wins += 1
    elif winner == "O":
        ai_wins += 1

    return jsonify({'move': move, 'winner': winner, 'player_wins': player_wins, 'ai_wins': ai_wins})


if __name__ == '__main__':
    app.run(debug=True)

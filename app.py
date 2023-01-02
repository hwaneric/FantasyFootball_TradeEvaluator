from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Some code was borrowed from the CS50 Finance PSet

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///trade_evaluator.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Display user's team"""

    team = db.execute("SELECT name, position, trade_value FROM players WHERE id IN (SELECT player_id FROM users_players WHERE user_id = ?)", session["user_id"])   

    return render_template("homepage.html", team=team) 


@app.route("/trade", methods=["GET", "POST"])
@login_required
def trade():
    """Evaluate User's Trade"""

    if request.method == "POST":

        # Get trade values
        values = []

        values.append(db.execute("SELECT trade_value, name FROM players WHERE name = ?", request.form.get("player1")))
        values.append(db.execute("SELECT trade_value, name FROM players WHERE name = ?", request.form.get("player2")))
        values.append(db.execute("SELECT trade_value, name FROM players WHERE name = ?", request.form.get("player3")))
        values.append(db.execute("SELECT trade_value, name FROM players WHERE name = ?", request.form.get("player4")))
        values.append(db.execute("SELECT trade_value, name FROM players WHERE name = ?", request.form.get("player5")))
        values.append(db.execute("SELECT trade_value, name FROM players WHERE name = ?", request.form.get("player6")))
        
        # Validate that user submits valid player names. 
        if request.form.get("player4"):
            chosen_player = db.execute("SELECT id FROM players WHERE name = ?", request.form.get("player4"))
            if not chosen_player:
                return apology("Player in trade does not exist", 400)

        if request.form.get("player5"):
            chosen_player = db.execute("SELECT id FROM players WHERE name = ?", request.form.get("player5"))
            if not chosen_player:
                return apology("Player in trade does not exist", 400)

        if request.form.get("player6"):
            chosen_player = db.execute("SELECT id FROM players WHERE name = ?", request.form.get("player6"))
            if not chosen_player:
                return apology("Player in trade does not exist", 400)

        # Validate if users submitted at least one player on each side of the form. 
        if not values[0] and not values[1] and not values[2]:
            return apology("must trade away at least 1 player", 400)
        if not values[3] and not values[4] and not values[5]:
            return apology("must trade for at least 1 player", 400)        

        # Validate that form is filled out top to bottom and that same player is not on both sides of trade. 
        trade_for = 0
        trade_away = 0
        for i in range(3):
            if values[i]:
                trade_for += 1
            if values[i + 3]:
                trade_away += 1
        for i in range(trade_for):
            for j in range(trade_away):
                if not values[i] or not values[j+3]:
                    return apology("please fill out form from top to bottom")
                if values[i][0]["name"] == values[j + 3][0]["name"]:
                    return apology("same player cannot be on both sides of trade", 400)

        # Check if the user submitted a player in the form. If the user did not, set the player's trade value to 0. 
        null_value = [{"trade_value": 0}]
        for i in range(6):
            if not values[i]:
                values[i] = null_value
        
        # Calculate and compare trade values
        user_value = values[0][0]["trade_value"] + values[1][0]["trade_value"] + values[2][0]["trade_value"]
        opponent_value = values[3][0]["trade_value"] + values[4][0]["trade_value"] + values[5][0]["trade_value"]

        if user_value < opponent_value:
            result = "won"
        elif user_value > opponent_value:
            result = "lost"
        else:
            result = "tied"
        return render_template("result.html", result=result)

    else:
        team = db.execute("SELECT name, id FROM players WHERE id IN (SELECT player_id FROM users_players WHERE user_id = ?)", session["user_id"])   
        return render_template("trade.html", team=team)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
    

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password and confirmation align
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not align", 400)

        # Ensure username does not already exist
        usernames = db.execute("SELECT username FROM users")
        i = 0
        for name in usernames:
            if request.form.get("username") == usernames[i]["username"]:
                return apology("username already taken, please choose a new username", 400)
            i += 1

        # Enter inputted username and password hash into the database
        hash_variable = generate_password_hash(request.form.get("password"))
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", request.form.get("username"), hash_variable)

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """Allow users to add or drop players"""
    if request.method == "POST":

         # Ensure player name was submitted
        if not request.form.get("player"):
            return apology("must provide player name", 400)

        # Check player name is in database
        chosen_player = db.execute("SELECT id, position FROM players WHERE name = ?", request.form.get("player"))
        if not chosen_player:
            return apology("Player does not exist", 400)

        # Check that the player is not already on the user's team
        team = db.execute("SELECT player_id FROM users_players WHERE user_id = ?", session["user_id"])
        for i in range(len(team)):
            if chosen_player[0]["id"] == team[i]["player_id"]:
                return apology("Player already on team", 400)

        # Add player to the user's team
        db.execute("INSERT INTO users_players (user_id, player_id) VALUES (?, ?)", session["user_id"], chosen_player[0]["id"])
 
        return redirect("/")

    else:
        
        return render_template("add.html")


@app.route("/drop", methods=["GET", "POST"])
@login_required
def drop():
    """Allow users to add or drop players"""
    if request.method == "POST":

        # Ensure player name was submitted
        if not request.form.get("player"):
            return apology("must provide player name", 400)

        # Ensure player submitted is on the user's team
        chosen_player = int(request.form.get("player"))
        team = db.execute("SELECT player_id FROM users_players WHERE user_id = ?", session["user_id"])
        team_list = []
        for i in range(len(team)):
            team_list.append(team[i]["player_id"])
        if chosen_player not in team_list:
            return apology("Player not on team", 400)

        # Drop player from the user's team
        db.execute("DELETE FROM users_players WHERE user_id = ? AND player_id = ?", session["user_id"], chosen_player)

        return redirect("/")

    else:
        team = db.execute("SELECT name, id FROM players WHERE id IN (SELECT player_id FROM users_players WHERE user_id = ?)", session["user_id"])
        return render_template("drop.html", team=team)

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

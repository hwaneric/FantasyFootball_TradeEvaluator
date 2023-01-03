<h1 align="center">
    Fantasy Football Trade Evaluator
</h1>

<p align="center">
  <a href="#background">Background</a> •
  <a href="#usage">Usage</a>
</p>

## Background
This web app allows users register and log in with an account and then build a fantasy football team that they can simulate trades with. These trades are analyzed by the web app, and the user is informed if they won, lost, or tied the trade. 

This project—created in 2021—was my first ever major coding project, and it was completed as my final project for when I took Harvard's CS50. Please excuse any messy and less-than-optimal code on my first major project!


## Usage

### Installing and Running the Webapp
1. Clone the repository.
```bash
git clone git@github.com:hwaneric/FantasyFootball_TradeEvaluator.git FantasyFootballTradeEvaluator
```

2. In the folder, create a virtual environemnt called .venv to run flask.
```bash
# Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
.venv\scripts\activate
```

3. In VS Code, open the Command Palette (View > Command Palette or (⇧⌘P)). Then select the Python: Select Interpreter command. Next, select the virtual environment that starts with ```./.venv``` or ```.\.venv```.

4. Update pip in the virtual environment by running the following command in the VS Code Terminal:
```bash
python -m pip install --upgrade pip
```

5. Run the web app using flask by runnning the following command: 
```bash
flask run
```

6. Open the web app in your browser by opening the "Running on" link in the terminal.

### User Guide
Please click the register button and create a profile. You will be redirected to the log in page, where you can use your new account to log in. Once you are logged in and redirected to the homepage, traverse to the "Add Players to Team" page. Type in a players name and click the button to add the player to your team. Please note that the player's name must be formatted exactly as seen on the CBS data (link is provided at the bottom of the page for reference). CBS formats player names as first initial, period, space, last name (example: T. Brady). Please use this same format when typing in the player's name into the form. Note that the form is case sensitive. 

After adding a player, you will be redirected to the homepage, where you will be able to see your current team. If you would like, you may go to the "Drop Players from Team" page to remove players from your team. On this page, simply use the dropdown menu, which only includes players from your team, to remove players from your team. 

After forming your team, go to the "Evaluate Trades" page. On the left side, choose at least 1 and no more than 3 players to trade away using the dropdown menu. The dropdown menu will only display players on your team, so if you do not see any players in the menu or do not see a player you would like to trade away, please add this player to your team on the "Add Players to Team" page. On the right side, choose at least 1 and no more than 3 players that you would like to trade for by typing their name (again, use CBS' name formatting) in the forms. Note that, again, this form is case sensitive. Also, note that the form will return an error message if the form is not filled top down. In other words, if there is a input box that is empty above an input box that is filled, the form will return an error message. Also please note that this "Evaluate Trades" page only simulates trades, it does not actually remove or add players from your team. 

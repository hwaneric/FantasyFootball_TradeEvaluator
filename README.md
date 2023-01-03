<h1 align="center">
    Discriminology
</h1>

<p align="center">
  <a href="#background">Background</a> •
  <a href="#usage">Usage</a> •
</p>

## Background
Discriminology is a nonprofit that works to leverage technology, data, and human capital to advance the social, civic, and economic strength of Black and Brown communities by ensuring their youth have equal opportunities at success through equitable opportunities to learn. Recognized by the Roddenberry Foundation, Echoing Green, and 4.0 schools, Discriminology has developed a platform that highlights racial inequity at schools around the United States. Since the platform’s launch in 2016, Discriminology has amassed over 150,000 users and has evaluated over 90,000 schools (nearly every K-12 public school in the country) through analyzing the US Department of Education Office for Civil Rights’ data.

In the current school system, there exist racial disparities in the experiences and the treatment of Black and Brown students throughout the country. Discriminology has developed a platform that highlights racial inequity at schools around the United States by compiling quantitative data taken from the US Department of Education Office for Civil Rights’ data. However, after conducting seven focus groups with community organizations, they have found that these organizers working on racial justice and educational equity prefer qualitative narratives to quantitative data, and that personal narratives are often necessary to provide context to numerical data. Currently there are no platforms designed to explicitly capture and illustrate these stories. In Spring 2022, Tech for Social Good designed a mobile reporting tool for community members to log and report their experiences of racial inequity. This repository contains a mobile responsive web app based off those designs created last spring by T4SG. This app aims to create a mapping tool that publicly records and amplifies the lived experiences of Black and Brown communities by school and/or district.

## Usage

Take a look at our documentation [here](https://discriminologydocs.readthedocs.io/en/latest/index.html).

### Installing

1. Clone the repository.
```bash
git clone git@github.com:hcs-t4sg/hcs-t4sg-discriminology_project.git Discriminology
```

2. Change directory to the `frontend` and follow the `README.md` there.
```bash
cd frontend
```

3. In another terminal window, change directory to the `backend` and follow the `README.md` there.
```bash
cd backend
```

4. To run the scripts, change directory to the `scripts`. Download the project dependencies there.
```bash
pip install -r requirements.txt
```

### Structure
The ```scripts``` folder includes scripts to be run to populate the databases. The ```frontend``` folder contains all of the frontend related files, including the HTML pages and their styles. The ```backend``` folder is used for all server-related code that queries the databases. You will need to run code from both the ```frontend``` and ```backend``` folders to run teh entire app.





My project is a fantasy football trade analyzer. Users can add and drop players on their fantasy football team and then simulate trades with players that are on their team. These trades are analyzed by the program, and the user is informed if they won, lost, or tied the trade. 

In order to open my project, please cd into the trade_evaluator folder, use "flask run" in the terminal, and open the following link. Please click the register button and create a profile. Use this log in information to then log in. You will be directed to my website's homepage. In order to get started, please go ot the "Add Players to Team" page. Type in a players name and click the button to add the player to your team. Please note that the player's name must be formatted exactly as seen on the CBS data (link is provided at the bottom of the page for reference). CBS formats player names as first initial, period, space, last name (example: T. Brady). Please use this same format when typing in the player's name into the form. Note that the form is case sensitive. 

After adding a player, you will be redirected to the homepage, where you will be able to see your current team. If you would like, you may go to the "Drop Players from Team" page to remove players from your team. On this page, simply use the dropdown menu, which only includes players from your team, to remove players from your team. 

Finally, after making the team of your heart's content, go to the "Evaluate Trades" page. On the left side, choose at least 1 and no more than 3 players to trade away using the dropdown menu. The dropdown menu will only display players on your team, so if you do not see any players in the menu or do not see a player you would like to trade away, please add this player to your team on the "Add Players to Team" page. On the right side, choose at least 1 and no more than 3 players that you would like to trade for by typing their name (again, use CBS' name formatting) in the forms. Note that, again, this form is case sensitive. Also, note that the form will return an error message if the form is not filled top down. In other words, if there is a input box that is empty above an input box that is filled, the form will return an error message. Also please note that this "Evaluate Trades" page only simulates trades, it does not actually remove or add players from your team. 

https://www.youtube.com/watch?v=-niR3A9G4LU

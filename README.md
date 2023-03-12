# Toastmasters Club Survey Analysis

## Purpose

* The external user goal is to gain insights from the results of the survey.
* The internal user goal is to provide insights leading to action from the survey data.
* The site is targeted at Toastmasters International. It provides a way for the organisation to analyse member data including age, employment status, main goals for joining Toastmasters and level of satisfaction.
* The program runs in the Code Institute mock terminal on Heroku.

* The live version can be accessed here: https://tm-club-survey-analysis.herokuapp.com/

INSERT IMAGES OF FINISHED PROGRAM

## User Stories
* I am a Director at Toastmasters International and I want to know the main goals of members so that I can provided better resources.
* I am a Director at Toastmasters ...


## Features

DO NOT NEED IMAGES HERE

### Gets data from spreadsheets stored in Google Drive
* The survey result data for each club is stored in its own worksheet.
* The data is accessed using the Google Drive API. 
* The spreadsheet can be viewed here: https://docs.google.com/spreadsheets/d/1XsYRec63Il1tKu0qwXapBjtjuYRhDiZtlyp6HprYF3U/edit?usp=sharing

### Club selection menu 
* The user can select and view data for the club they are interested in.
* The user has two options to choose from on the club menu.
* The user selects an option by entering '1' or '2' and pressing 'Enter'.
* Invalid input such as floats, strings or numbers other than 1 or 2 will cause an error message to be printed. The user will then be presented with the club menu again and reminded to select either 1 or 2.

### Calculation selection menu
* The user can select the calculation to be performed.
* The user has two options to choose from on the club menu.
* The user selects an option by entering a number from 1 to 6 and pressing 'Enter'.
* Invalid input such as floats, strings or numbers other than 1 or 2 will cause an error message to be printed. The user will then be presented with the calculation menu again and reminded to select a number from 1 to 6.

### Calculate average age
* When the user selects 'Calculate age', the average is calculated and the result is displayed in the terminal.

### Calculate percentage employed, retired or student
* When the user selects 'Calculate percentage employed', the percentage of each is calculated and displayed in the terminal.

### Calculate main goal percentage
* When the user selects 'Calculate main goal percentage', the percentage of members with each main goal is calculated and displayed in the terminal.

### Calculate level of satisfaction
* When the user selects 'Calculate satisfaction', the percentage of members satisfied with their club experience is calculated and displayed in the terminal.

### User input validation
* User input when selecting menu options is validated.
* When input is invalid, an error message is displayed and the user is asked to try again.

### Return to club menu option
* The user is given the option to return to the club menu and select a different club.

### Exit program option
* The user is given the option to exit the program.

### Future Features

* Create a method within the 'Club' class that calculates the percentage of members that participated in the survey. 

## Data Model

### 'Club' Class
* A class named 'Club' is used. A new instance of the Club class is created for each club.

#### 'Club' Class Attributes
The Club class has the following attributes: 
* `club_name`: The name of the club.
* `num_members`: The current number of members in the club.
* `club_type`: The type of club. Clubs can be 'regular' or 'business'.
* `meetings_per_month`: The number of meetings per month.
* `data`: A list containing the data from the club's survey results worksheet.

#### 'Club' Class Methods
* `club_description()`: This method returns a description of the club including its name, type, the number of members and the number of meetings per month.
* `get_age_data()`: This method gets the age data from a club worksheet and returns it as a list of strings.
* `get_employment_data()`: This method gets the employment data from a club worksheet and returns it as a list of strings.
* `get_goal_data()`: This method gets the goal data from a club worksheet and returns it as a list of strings.
* `get_satisfaction_data()`: This method gets the satisfaction data from a club worksheet and returns it as a list of strings. 


## Algorithm

ADD FLOWCHART 

## Technology
* Heroku was used to deploy the program.
* Google Sheets was used to store the survey data.
* Google Drive API was used to facilitate access to the data in Google Sheets.
* Gitpod was used for editing.
* Github was used for storing and sharing the repository. 
* LucidChart was used to create the algorithm flowchart.

## Testing

### Code Validation
ADD VALIDATION RESULTS
* Code was passed through the [Code Institute Python Linter](https://pep8ci.herokuapp.com/).

### Test Cases

1. Open the live app. The user is shown a welcome message and club menu. The user notices that they are asked to select a club option.
2. Enter a string value. The user is shown an error message. The user notices that they must enter a number.
3. Enter a float. The user is shown an error message. The user notices that they must enter 1 or 2.
4. Enter '1'.  The user is shown a description of their selected club. The user notices the calculation menu.
5. Read the calculation menu. The user notices that they are asked to select an option. 
5. Enter a string value. The user is shown an error message. The user notices that they must enter a number.
6. Enter a float. The user is shown an error message. The user notices that they must enter a number from 1 to 6.
7. Enter '1'. The user is shown the results of the average age calculation. The user notices the calculation menu is displayed again.
8. Enter 2. The user is shown the results of the employment percentage calculation. The user notices the calculation menu is displayed again.
9. Enter 3. The user is shown the results of the goal percentage calculation. The user notices the calculation menu is displayed again.
10. Enter 4. The user is shown the results of the satisfaction percentage calculation. The user notices the calculation menu is displayed again.
11. Enter 5. The user is shown the club menu. The user notices that they are asked to select an option. 
12. Enter 2. The user is shown a description of their selected club. The user notices the calculation menu.
13. Read the calculation menu. The user notices that they are asked to select an option. 
13. Enter 6. The user is shown the 'Thank you for using this program' message. The user notices that they have the option to run the program again by clicking 'Run Program'.

### Fixed Bugs
ADD FIXED BUGS

### Remaining Bugs
ADD REMAINING BUGS

## Deployment

### Via Gitpod

1. Go to http://github.com.
2. Open the 'SiobhanP1/tm-club-survey-analysis' repository.
3. Click on 'Gitpod' to open a Gitpod workspace.
4. Enter the command `python3 run.py` in the terminal to run the program.

### Via Heroku

The program was deployed using Heroku by doing the following:

1. Go to http://github.com.
2. Open the 'SiobhanP1/tm-club-survey-analysis' repository.
3. Go to https://www.heroku.com.
4. Select 'Create app'.
5. Give the app a unique name.
6. Go to 'Settings'.
7. Click 'Reveal Config Vars'.
8. Under 'key', add 'CREDS'. Under 'value', copy and paste the content of the 'creds.json' in the repository.
9. Go to 'Add Buildpacks'. 
10. Add 'Python' and 'Save Changes'.
11. Add 'NodeJS' and 'Save Changes'.
12. Go to 'Deploy' and then 'Deployment Method'.
13. Select 'Connect to Github'.
14. Enter the repository name.
15. Select 'Manual Deploy'. 
16. Click 'Deploy'.

## Credits

* The deployment terminal was created by Code Institute.


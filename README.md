# Toastmasters Club Survey Analysis

## Purpose

* The external user goal is to gain insights from the results of the survey.
* The internal user goal is to provide insights leading to action from the survey data.
* The site is targeted at Toastmasters International. It provides a way for the organisation to analyse member data including age, employment status, main goals for joining Toastmasters and level of satisfaction.
* The program runs in the Code Institute mock terminal on Heroku.

* The live version can be accessed here: INSERT LINK
INSERT IMAGES OF FINISHED PROGRAM

## User Stories
* I am a Director at Toastmasters International and I want to know the main goals of members so that I can provided better resources.
* I am a Director at Toastmasters ...


## Features

INSERT FEATURE IMAGES

### Gets data from spreadsheets stored in Google Drive
* The survey result data for each club is stored in its own worksheet.
* The data is accessed using the Google Drive API. 

### Club selection menu 
* The user can select and view data for the club they are interested in.

### Calculation selection menu
* The user can select the calculation to be performed.

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

ADD ADDITIONAL

* Create a method within the Club class that calculates the percentage of members that participated in the survey. 

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

### Fixed Bugs
ADD FIXED BUGS

### Remaining Bugs
ADD REMAINING BUGS

## Deployment

INCLUDE HOW TO VIEW IN GITPOD?

### Via Heroku

The program was deployed using Heroku by doing the following:

ADD DEPLOYMENT STEPS

## Credits

* The deployment terminal was created by Code Institute.


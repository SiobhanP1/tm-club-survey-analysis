from pprint import pprint
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('DublinTMclubSurveyData')

dublin_worksheet = SHEET.get_worksheet(0)
dublin_data = dublin_worksheet.get_all_values()


class Club:
    """
    Toastmaster club class
    """
    def __init__(self, club_name, num_members, club_type, meetings_per_month, data):
        self.club_name = club_name
        self.num_members = num_members
        self.club_type = club_type
        self.meetings_per_month = meetings_per_month
        self.data = data

    def club_description(self):
        """
        Returns description of instance of club class.
        """
        return f"{self.club_name} Toastmasters Club is a {self.club_type} club with {self.meetings_per_month} meetings a month. There are {self.num_members} members."


def get_age_data(data):
    """
    Get age data from worksheet in form of list of integers.
    """
    print("Getting age data...")
    age_data = data.col_values(2)[1:]
    int_age_data = [int(age) for age in age_data]
    print(int_age_data)
    return int_age_data


def calculate_average(data):
    """
    Calculate average of list of integers.
    """
    print("Calculating average...")
    average = round(sum(data) / len(data))
    print(f"Average: {average}")
    print("Average successfully calculated")
    return average


def get_employment_data(data):
    """
    Get employment data from worksheet
    """
    print("Getting employment data...")
    employment_data = data.col_values(3)[1:]
    print(employment_data)
    return employment_data


def calculate_percentage_employed(data):
    """
    Calculate percentage employed, retired, student.
    """
    print("Calculating percentage employed...")
    employed = data.count('employed')
    retired = data.count('retired')
    student = data.count('student')
    percent_employed = 100 * (employed / len(data))
    percent_retired = 100 * (retired / len(data))
    percent_student = 100 * (student / len(data))
    print(f"Percentage employed: {percent_employed}%")
    print(f"Percentage students: {percent_student}%")
    print(f"Percentage retired: {percent_retired}%")
    print("Employment percentage successfully calculated")
    return f"{percent_employed}% are employed, {percent_student}% are students and {percent_retired}% are retired." 


def get_goal_data(data):
    """
    Get respondent main goal data from worksheet
    """
    print("Getting main goal data...")
    goal_data = data.col_values(4)[1:]
    print(goal_data)
    return goal_data


def calculate_percentage_each_goal(data):
    """
    Calculate percentage for each main goal.
    """
    print("Calculating main goal percentages...")
    confidence = data.count('self-confidence')
    social = data.count('social')
    speaking = data.count('public speaking')
    percent_confidence = 100 * (confidence / len(data))
    percent_social = 100 * (social / len(data))
    percent_speaking = 100 * (speaking / len(data))
    print(f"Self-confidence percentage: {percent_confidence}%")
    print(f"Social percentage: {percent_social}%")
    print(f"Public speaking percentage: {percent_speaking}%")
    print("Main goal percentages successfully calculated")
    return f"{percent_speaking}% chose public speaking, {percent_confidence}% chose self-confidence and {percent_social}% chose social." 


def get_satifaction_data(data):
    """
    Get satisfaction with club experience data from worksheet
    """
    print("Getting satisfaction data...")
    satisfied_data = data.col_values(5)[1:]
    print(satisfied_data)
    return satisfied_data


def calculate_percentage_satisfied(data):
    """
    Calculate percentage satisfied.
    """
    print("Calculating percentage satisfied...")
    satisfied = data.count('yes')
    percent_satisfied = 100 * (satisfied / len(data))
    print(f"Percentage satisfied: {percent_satisfied}%")
    print("Percentage satisfied successfully calculated")
    return percent_satisfied


def select_club():
    """
    Collect user club selection input
    """
    while True:
        print("Please select a club.\n 1. Dublin Toastmasters\n 2. London Toastmasters\n")
        selected_club_option = input("Please enter a number here: \n")
        try:
            if int(selected_club_option) == 1:
                dublin_club = Club('Dublin', 22, 'regular', 4, dublin_data)
                print(dublin_club.club_description())
                selected_club = dublin_worksheet
                return selected_club
            elif int(selected_club_option) == 2:
                london_club = Club('London', 15, 'business', 2, london_data)
                print(london_club.club_description())
                selected_club = london_worksheet
                return selected_club
            elif int(selected_club_option) != 1 and int(selected_club) != 2:
                raise ValueError
        except ValueError() as e:
            print("Please enter 1 or 2.")


def main():
    """
    Main function called when user clicks 'Run Program'.
    """
    print("Welcome to Toastmasters Club Survey Analysis\n")
    club = select_club()
    
    ages_list = get_age_data(club)
    calculate_average(ages_list)
    employment_data = get_employment_data(club)
    calculate_percentage_employed(employment_data)
    goal_data = get_goal_data(club)
    calculate_percentage_each_goal(goal_data)
    satisfied = get_satifaction_data(club)
    calculate_percentage_satisfied(satisfied)


main()
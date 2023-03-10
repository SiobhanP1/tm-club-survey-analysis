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
    print(f"Percentage employed: {percent_employed}")
    print(f"Percentage students: {percent_student}")
    print(f"Percentage retired: {percent_retired}")
    print("Employment percentage successfully calculated")
    return percent_employed 


def main():
    """
    Main function called when user clicks 'Run Program'.
    """
    dublin_club = Club('Dublin', 22, 'regular', 4, dublin_data)
    print(dublin_club.club_description())
    pprint(dublin_data)
    ages_list = get_age_data(dublin_worksheet)
    calculate_average(ages_list)
    employment_data = get_employment_data(dublin_worksheet)
    calculate_percentage_employed(employment_data)


main()
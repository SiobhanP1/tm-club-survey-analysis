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
    Get age data from worksheet 
    """
    print("Getting age data...")
    age_data = data.col_values(2)[1:]
    int_age_data = [int(age) for age in age_data]
    print(int_age_data)
    calculate_average(int_age_data)


def calculate_average(data):
    """
    Calculate average of list of integers
    """
    print("Calculating average...")
    average = round(sum(data) / len(data))
    print(f"Average: {average}")
    print("Average successfully calculated")


def main():
    """
    Main function called when user clicks 'Run Program'.
    """
    dublin_club = Club('Dublin', 22, 'regular', 4, dublin_data)
    print(dublin_club.club_description())
    pprint(dublin_data)
    get_age_data(dublin_worksheet)


main()
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

worksheet = SHEET.get_worksheet(0)
all_data = worksheet.get_all_values()
pprint(all_data)


class Club:
    """
    Toastmaster club class
    """
    def __init__(self, club_name, num_members, club_type, meetings_per_month):
        self.club_name = club_name
        self.num_members = num_members
        self.club_type = club_type
        self.meetings_per_month = meetings_per_month
   

    def club_description(self):
        """
        Returns description of instance of club class. 
        """
        return f"{self.club_name} Toastmasters Club is a {self.club_type} club with {self.meetings_per_month} meetings a month. There are {self.num_members} members."
    

    def calc_meetings_per_year(self):
        """
        Calculates the number of club meetings per year. 
        """
        return self.meetings_per_month * 12


def main():
    """
    Main function called when user clicks 'Run Program'.
    """
    dublin_club = Club('Dublin', 22, 'regular', 4)
    print(dublin_club.club_description())


main()
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
SHEET = GSPREAD_CLIENT.open('TMclubSurveyData')

dublin_worksheet = SHEET.get_worksheet(0)
london_worksheet = SHEET.get_worksheet(1)
dublin_data = dublin_worksheet.get_all_values()
london_data = london_worksheet.get_all_values()


class Club:
    """
    Toastmaster club class
    """
    def __init__(self, club_name, num_members, club_type, 
                 meetings_per_month, data):
        self.club_name = club_name
        self.num_members = num_members
        self.club_type = club_type
        self.meetings_per_month = meetings_per_month
        self.data = data

    def club_description(self):
        """
        Returns description of instance of club class.
        """
        return f"{self.club_name} Toastmasters Club is a {self.club_type} club with {self.meetings_per_month} meetings a month. There are {self.num_members} members.\n"


def get_age_data(data):
    """
    Get age data from worksheet in form of list of integers.
    """
    print("Getting age data...")
    age_data = data.col_values(2)[1:]
    int_age_data = [int(age) for age in age_data]
    return int_age_data


def calculate_average(data):
    """
    Calculate average of list of integers.
    """
    print("Calculating average...")
    average = round(sum(data) / len(data))
    print(f"Average age: {average}\n")
    return average


def get_employment_data(data):
    """
    Get employment data from worksheet
    """
    print("Getting employment data...")
    employment_data = data.col_values(3)[1:]
    return employment_data


def calculate_percentage_employed(data):
    """
    Calculate percentage employed, retired, student.
    """
    print("Calculating percentage employed...\n")
    employed = data.count('employed')
    retired = data.count('retired')
    student = data.count('student')
    percent_employed = 100 * (employed / len(data))
    percent_retired = 100 * (retired / len(data))
    percent_student = 100 * (student / len(data))
    print(f"Percentage employed: {percent_employed}%")
    print(f"Percentage students: {percent_student}%")
    print(f"Percentage retired: {percent_retired}%\n")
    return f"{percent_employed}% are employed, {percent_student}% are students and {percent_retired}% are retired." 


def get_goal_data(data):
    """
    Get respondent main goal data from worksheet
    """
    print("Getting main goal data...")
    goal_data = data.col_values(4)[1:]
    return goal_data


def calculate_percentage_each_goal(data):
    """
    Calculate percentage for each main goal.
    """
    print("Calculating main goal percentages...\n")
    confidence = data.count('self-confidence')
    social = data.count('social')
    speaking = data.count('public speaking')
    percent_confidence = 100 * (confidence / len(data))
    percent_social = 100 * (social / len(data))
    percent_speaking = 100 * (speaking / len(data))
    print(f"Self-confidence: {percent_confidence}%")
    print(f"Social: {percent_social}%")
    print(f"Public speaking: {percent_speaking}%\n")
    return f"{percent_speaking}% chose public speaking, {percent_confidence}% chose self-confidence and {percent_social}% chose social." 


def get_satifaction_data(data):
    """
    Get satisfaction with club experience data from worksheet
    """
    print("Getting satisfaction data...")
    satisfied_data = data.col_values(5)[1:]
    return satisfied_data


def calculate_percentage_satisfied(data):
    """
    Calculate percentage satisfied.
    """
    print("Calculating percentage satisfied...\n")
    satisfied = data.count('yes')
    percent_satisfied = 100 * (satisfied / len(data))
    print(f"Percentage satisfied: {percent_satisfied}%\n")
    return percent_satisfied


def print_club_menu():
    """
    Print club options menu.
    """
    print("\nPlease select a club.")
    print("1. Dublin Toastmasters")
    print("2. London Toastmasters\n")


def select_club():
    """
    Collect user club selection input
    """
    while True:
        try:
            print_club_menu()
            selected_club_option = input("Please enter a number here: \n")

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
            elif int(selected_club_option) != 1 and int(selected_club_option) != 2:
                raise ValueError(
                    f"You entered {selected_club_option}. Please enter 1 or 2."
                )
            else:
                raise TypeError(
                    f"You entered {selected_club_option}. Please enter a number."
                )
        except ValueError as e:
            print(f"\nInvalid option. {e}\n")
        except TypeError as e:
            print(f"\nInvalid option. {e}\n")


def print_calc_menu():
    """
    Prints options 1-6. 
    """
    print("Please choose an option.")
    print("1. Calculate average age of respondents.")
    print("2. Calculate percentage employed.")
    print("3. Calculate percentage having each main goal.") 
    print("4. Calculate percentage satisfied with club experience.")
    print("5. Return to club menu.")
    print("6. Exit program.\n")


def select_calculation(club):
    """
    Collect and validate user's calculation selection.
    """
    while True:
        try:
            print_calc_menu()
            calc_selection = input("Please enter a number from 1 to 6 here: \n")

            if int(calc_selection) == 1:
                ages_list = get_age_data(club)
                calculate_average(ages_list)
            elif int(calc_selection) == 2:
                employment_data = get_employment_data(club)
                calculate_percentage_employed(employment_data)
            elif int(calc_selection) == 3:
                goal_data = get_goal_data(club)
                calculate_percentage_each_goal(goal_data)
            elif int(calc_selection) == 4:
                satisfied = get_satifaction_data(club)
                calculate_percentage_satisfied(satisfied)
            elif int(calc_selection) == 5:
                main()
            elif int(calc_selection) == 6:
                break
            elif int(calc_selection) < 1 or int(calc_selection) > 6:
                raise ValueError(
                    f"You entered {calc_selection}. Please enter an integer from 1 to 6."
                )
            else:
                raise TypeError(
                    f"You entered {calc_selection}. Please enter a number from 1 to 6."
                )
        except ValueError as e:
            print(f"\nInvalid option. {e}\n")
        except TypeError as e:
            print(f"\nInvalid option. {e}\n")

    print("Thank you for using this program.")
    print("Click 'Run Program' to run it again.\n")
    return False


def main():
    """
    Main function called when user clicks 'Run Program'.
    """
    club_selection = select_club()
    select_calculation(club_selection)


if __name__ == "__main__":
    print("Welcome to Toastmasters Club Survey Analysis")
    main()
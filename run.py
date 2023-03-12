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
    Club class: Defines parameters and methods used with instances of the Club
    class. Each instance is a different club.

    Methods:
    club_description: Returns a description of the club including its
    name, number of members, type and number of meetings per month.
    """
    def __init__(self, club_name, num_members, club_type,
                 meetings_per_month, data, worksheet):
        """
        Class Parameters:
        club_name: The name of the club
        num_members: The current number of members in the club
        club_type: The club type. Clubs can be 'regular' or 'business'.
        meetings_per_month: The number of club meetings every month
        data: List of values from survey result worksheet
        worksheet: Worksheet containing survey result data
        """
        self.club_name = club_name
        self.num_members = num_members
        self.club_type = club_type
        self.meetings_per_month = meetings_per_month
        self.data = data
        self.worksheet = worksheet

    def club_description(self):
        """
        This method creates a string description of any instance of the Club
        class.

        The description includes the club name, type, number of members and
        numbers of meetings per month.

        It returns this description as a string.
        """
        return (
            f"{self.club_name} Toastmasters Club is a {self.club_type}"
            f" club with {self.meetings_per_month} meetings a month. There are"
            f" {self.num_members} members.\n"
            )

    def get_age_data(self):
        """
        This method gets the age data from a club's survey result
        worksheet.

        Parameters
        worksheet: Worksheet containing survey data.

        Returns
        It returns the ages as a list of integers.
        """
        print("Getting age data...")
        age_data = self.worksheet.col_values(2)[1:]
        int_age_data = [int(age) for age in age_data]
        return int_age_data

    def get_employment_data(self):
        """
        Gets employment data from a club's survey results worksheet.

        Parameters
        worksheet: Worksheet containing survey data.

        Returns
        Employment data as a list of strings.
        """
        print("Getting employment data...")
        employment_data = self.worksheet.col_values(3)[1:]
        return employment_data

    def get_goal_data(self):
        """
        Gets respondents' main goal data from survey results worksheet.

        Parameters
        worksheet: Worksheet containing survey data.

        Returns
        The main goal data as a list of strings.
        """
        print("Getting main goal data...")
        goal_data = self.worksheet.col_values(4)[1:]
        return goal_data

    def get_satifaction_data(self):
        """
        Gets 'satisfaction with club experience' data from a club's
        survey results worksheet. Respondents were given two options to
        choose from - 'yes' and 'no'.

        Parameters
        worksheet: Worksheet containing survey data.

        Returns
        The satisfaction data as a list of strings.
        """
        print("Getting satisfaction data...")
        satisfied_data = self.worksheet.col_values(5)[1:]
        return satisfied_data


def calculate_average(ages):
    """
    Calculates the average of a list of integers.

    Parameters
    data: The survey data from a club's survey results worksheet.

    Returns
    The average age as an integer.
    """
    print("Calculating average...")
    average = round(sum(ages) / len(ages))
    print(f"Average age: {average}\n")
    return average


def calculate_percentage_employed(data):
    """
    Calculates the percentage of members who are employed, retired
    or students, by counting the number of times each option was
    selected. Respondents were given three options to choose from -
    'employed', 'retired' or 'student'.

    Parameters
    data: The survey data from a club's survey results worksheet.

    Returns
    The percentage of respondents who are employed, the percentage
    retired and the percentage who are students.
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
    return (
        f"{percent_employed}% are employed, {percent_student}%"
        f" are students and {percent_retired}% are retired."
    )


def calculate_percentage_each_goal(data):
    """
    Calculates the percentage of respondents who selected
    each of the main goal options by counting the number of times
    each option was selected. Respondents were given three
    options to choose from - 'self-confidence', 'social' and 'public
    speaking'.

    Parameters
    data: The survey data from a club's survey results worksheet.

    Returns
    The percentage who chose public speaking, the percentage who
    chose self-confidence and the percentage who chose social.
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
    return (
        f"{percent_speaking}% chose public speaking,"
        f" {percent_confidence}% chose self-confidence and"
        f" {percent_social}% chose social."
        )


def calculate_percentage_satisfied(data):
    """
    Calculates the percentage of respondents satisfied with their
    club experience by counting the number who selected 'yes'.

    Parameters
    data: The survey data from a club's survey results worksheet.

    Returns
    The percentage of respondents who selected 'yes'.
    """
    print("Calculating percentage satisfied...\n")
    satisfied = data.count('yes')
    percent_satisfied = 100 * (satisfied / len(data))
    print(f"Percentage satisfied: {percent_satisfied}%\n")
    return percent_satisfied


def print_club_menu():
    """
    Prints the club options menu to the terminal.

    Parameters
    This function does not take any parameters.

    Returns
    Returns 'None'.
    """
    print("\nPlease select a club.")
    print("1. Dublin Toastmasters")
    print("2. London Toastmasters\n")


def print_calc_menu():
    """
    Prints the calculation options to the terminal.

    Parameters
    This function does not take any parameters.

    Returns
    Returns 'None'.
    """
    print("Please choose an option.")
    print("1. Calculate average age of respondents.")
    print("2. Calculate percentage employed.")
    print("3. Calculate percentage having each main goal.")
    print("4. Calculate percentage satisfied with club experience.")
    print("5. Return to club menu.")
    print("6. Exit program.\n")


def validate_club_option():
    """
    This function calls the print_club_menu function, then collects and
    validates user input for selecting a club option.

    Parameters
    This function does not take any parameters.

    Returns
    Returns an integer, either 1 or 2.
    """
    while True:
        try: 
            print_club_menu()
            selected_option = input("Please enter a number here: \n")
            if int(selected_option) in [1, 2]:
                return int(selected_option)
            else:
                raise ValueError(
                    f"You entered {selected_option}. Please enter 1 or 2."
                    )
        except ValueError as e:
            print(f"\n{e}\n")


def select_club(selected_club_option):
    """
    Prints a description of the selected club and returns the
    worksheet containing survey data for that club.

    Parameters
    selected_club_option: An integer representing the club
    selected by the user.

    Returns
    Returns the survey worksheet data for that club as a list of lists.
    """
    if int(selected_club_option) == 1:
        selection = dublin_club
        print(selection.club_description())
        selected_club = dublin_worksheet
        return selected_club
    elif int(selected_club_option) == 2:
        selection = london_club
        print(london_club.club_description())
        selected_club = london_worksheet
        return selected_club


def select_calculation():
    """
    Calls the print_calc_menu function, then collects and validates user
    input when the user selects a calculation option.

    Parameters
    This function does not take any parameters.

    Returns
    Returns an integer representing the selected calculation.
    """
    while True:
        try:
            print_calc_menu()
            calc_selection = input("Please enter a number from 1 to 6: \n")
            if int(calc_selection) in [1, 2, 3, 4, 5, 6]:
                return (calc_selection)
            else:
                raise ValueError(
                    f"You entered {calc_selection}. Please enter an integer "
                    "from 1 to 6."
                )
        except ValueError as e:
            print(f"\n{e}\n")


def run_calculation(calc_number, worksheet, club):
    """
    Runs the selected calculation.

    Parameters
    calc_number: an integer representing the calculation selected
    from the calculation menu.
    data: The survey data from a club's survey results worksheet.

    Returns
    Returns 'None'.
    """
    if int(calc_number) == 1:
        ages_list = club.get_age_data()
        calculate_average(ages_list)
    elif int(calc_number) == 2:
        employment_data = club.get_employment_data()
        calculate_percentage_employed(employment_data)
    elif int(calc_number) == 3:
        goal_data = club.get_goal_data()
        calculate_percentage_each_goal(goal_data)
    elif int(calc_number) == 4:
        satisfied = club.get_satifaction_data()
        calculate_percentage_satisfied(satisfied)
    elif int(calc_number) == 5:
        main()
    elif int(calc_number) == 6:
        print("Thank you for using this program.")
        print("Click 'Run Program' to run it again.\n")


dublin_club = Club('Dublin', 22, 'regular', 4, dublin_data, dublin_worksheet)
london_club = Club('London', 15, 'business', 2, london_data, london_worksheet)


def main():
    """
    Main function called when user clicks 'Run Program' and on initial
    loading of program.
    """
    club_number = validate_club_option()
    club_selection = select_club(club_number)
    if club_number == 1:
        club = dublin_club
    elif club_number == 2:
        club = london_club
    while True:
        calc_number = select_calculation()
        run_calculation(calc_number, club_selection, club)
        if int(calc_number) == 6:
            break


if __name__ == "__main__":
    print("Welcome to Toastmasters Club Survey Analysis")
    main()
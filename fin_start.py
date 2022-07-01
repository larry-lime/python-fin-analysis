from fin_analysis import *
from fin_compare import *
from fin_utils import *


class Start:
    def __init__(self) -> None:
        self.company_list = []

    def main_menu(self):
        # Menu Display
        menu_input = input(
            "\
            \n┌─Instructions────────────────────────────────────────┐\
            \n│Type the number corresponding to the desired action: │\
            \n└─────────────────────────────────────────────────────┘\
            \n1. Load companies\
            \n2. Compare companies\
            \n3. Exit Program\
            \n> "
        )

        # Read Menu Input
        if menu_input == "1":
            self.load_companies()

        elif menu_input == "2":
            self.compare_companies()

        elif menu_input == "3":
            self.exit_menu()

        else:
            self.invalid_input(self.main_menu)

    # Submenu 1
    def load_companies(self):

        # Submenu 1 Display
        submenu_input = input(
            "\
            \n┌─Instructions────────────────────────────────────────┐\
            \n│Type the number corresponding to the desired action: │\
            \n└─────────────────────────────────────────────────────┘\
            \n1. Manually input company ticker symbols\
            \n2. Read ticker symbols from tickers.csv\
            \n3. Go Back\
            \n4. Exit Program\
            \n> "
        )

        if submenu_input in ["1", "2"]:
            # Read Submenu 1 Input
            company_list = (
                self.manual_input() if submenu_input == "1" else read_tickers()
            )
            self.run_load(company_list)
            self.main_menu()

        elif submenu_input == "3":
            self.main_menu()

        elif submenu_input == "4":
            self.exit_menu()

        else:
            self.invalid_input(self.load_companies)

    def manual_input(self):

        user_input = input(
            f"\
                \n┌─Instructions────────────────────────────────────────┐\
                \n│Type the ticker of the company you wish to load      │\
                \n│                                                     │\
                \n│                        OR                           │\
                \n│                                                     │\
                \n│Type the number corresponding to the desired action: │\
                \n└─────────────────────────────────────────────────────┘\
                \nCompanies ready to load: {self.company_list}\
                \n1. Start loading company data\
                \n2. Undo last entry\
                \n3. Clear company list\
                \n4. Go Back\
                \n5. Exit Program\
                \n> "
        )

        if user_input == "1":
            return self.company_list

        elif user_input == "2":
            self.company_list.pop()

        elif user_input == "3":
            self.company_list.clear()

        elif user_input == "4":
            self.load_companies()

        elif user_input == "5":
            self.exit_menu()

        else:
            self.company_list.append(user_input.upper()) if user_input.upper() not in self.company_list else None

        print("\nCompanies ready to load:", self.company_list)
        return self.manual_input()

    def run_load(self, lst):
        for ticker in lst:
            company = Company(ticker)
            try:
                # TODO Take a look at this and refactor this
                lst = [x[0].split("/")[-1] + "/" for x in os.walk(company._parent_dir)]
                if company._dir not in lst:
                    company.import_data("annual")
                company.load_binary_data()
                company.convert_statements()
                company.convert_statistics()
                company.wacc()
                company.save_as_xslx()
                company.save_as_csv()
                company.save_as_txt()

            except Exception as e:
                error_log(e, company._parent_dir)

    # Menu Input 2
    def compare_companies(self):
        # Show companies in pwd
        lst = list_companies()
        companies = []
        print("\nThese are currently the companies you can compare:", lst)
        ticker = input(
            "\
                \nEnter the ticker of the company you wish to compare\n\
                \nType 'start' to compare company statistics\
                \nType 'all' to compare all companies\
                \nType 'stop' to stop comparing\
                \n> "
        ).upper()

        while ticker not in ["START", "STOP"]:
            if ticker == "ALL":
                companies = lst
                break
            else:
                companies.append(ticker)
                print("\nThese are currently the companies you can compare:", lst)
                print("Current companies to be compared:", companies)
                ticker = input(
                    "\nEnter the ticker of the companys you wish to compare\nType 'start' when all companies are entered\nType 'stop' to stop comparing\n> "
                ).upper()
        if ticker != "STOP":
            self.run_compare(companies)
        self.main_menu()

    def invalid_input(self, function=None):
        """
        Prints -> "Invalid Function" and calls the name of the function passed
        """
        print("Invalid input!")
        if function:
            function()

    def exit_menu(self):
        print("Program Exited!")
        exit()

    def run_compare(self, companies):
        compare = Compare(companies)
        compare.combine()
        compare.clean()
        compare.save_as_xslx()
        compare.save_as_csv()
        compare.save_as_txt()
        print("Done comparing companies!")


if __name__ == "__main__":
    print("\nWelcome to the Company Financials Analyzer!", end="")
    start = Start()
    start.main_menu()

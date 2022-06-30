from fin_analysis import *
from fin_compare import *
from fin_utils import *


def main_menu():
    # Menu Display
    menu_input = input(
        "\
        \nType the number corresponding to the desired action:\
        \n\
        \n1. Load companies\
        \n2. Compare companies\
        \n3. Exit Program\
        \n> "
    )

    # Read Menu Input
    if menu_input == "1":
        load_companies()

    elif menu_input == "2":
        compare_companies()

    elif menu_input == "3":
        exit_menu()

    else:
        print("Invalid input!")
        main_menu()


# Submenu 1
def load_companies():
    lst = []

    # Submenu 1 Display
    submenu_input = input(
        "\
        \nType the number corresponding to the desired action:\
        \n\
        \n1. Manually input company ticker symbols\
        \n2. Read ticker symbols from tickers.csv\
        \n3. Exit Program\
        \n> "
    )

    if submenu_input in ["1", "2"]:
        # Read Submenu 1 Input
        lst = manual_input(lst) if submenu_input == "1" else read_tickers()
        run_load(lst)
        main_menu()

    elif submenu_input == "3":
        main_menu()

    else:
        print("Ivalid Input!")
        load_companies()


def manual_input(lst):
    while True:
        ticker = input("Enter the ticker of a company you wish to load: ").upper()
        if ticker == "START":
            return lst
        lst.append(ticker)
        print("\nCompanies ready to load:", lst)
        print("Type 'start' to load new companies")


def run_load(lst):
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
def compare_companies():
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
        run_compare(companies)
    main_menu()


# Menu Input 3
def exit_menu():
    print("Program Exited!")


def run_compare(companies):
    compare = Compare(companies)
    compare.combine()
    compare.clean()
    compare.save_as_xslx()
    compare.save_as_csv()
    compare.save_as_txt()
    print("Done comparing companies!")


if __name__ == "__main__":
    print("\nWelcome to the Company Financials Analyzer!", end="")
    main_menu()

# Brett Potts - INFOTC 4401 Final Project

# This program uses a module to pull stock data from Yahoo! Finance.
# The GitHub page for the module is listed below.

# Must use 'pip install yfinance' to install the module so the program will work
# Please note that the columns printed when viewing a stock price may be cut off when run in IDLE. Running it in the Windows command prompt shows the full columns.
# I've included screenshots of each function of the program in the zip file.

# Sources I used for info on the yfinance module:
#       https://pypi.org/project/yfinance
#       https://github.com/ranaroussi/yfinance

import yfinance


def printMenu():
    print("\nWelcome to Brett's Python Stock Program!\n")
    print("1. View stock prices\n2. Show earnings\n3. Add a ticker to your portfolio\n4. View portfolio\n5. Quit")


runMenu = True
while runMenu:  # run program until user quits

    printMenu()
    choice = input("\nPlease select an option (1, 2, 3, 4, or 5): ")

    if choice == '1':  # prices

        # get stock ticker from the user
        tckr = input("Please enter a stock ticker (example: MSFT, TSLA, SONY): ")
        stock = yfinance.Ticker(tckr)

        # get period of time from the user
        # history period formats: 1d 1mo 1y
        prd = input(
            "Please enter the period of time for which you would like to see prices (example: 5d = days, 1mo = 1 month, 7y = 7 years. Any deviation from this formatting will just print the most recent price info.): ")
        hist = stock.history(period=prd)

        print(hist)
        print("\n")

    if choice == '2':  # earnings

        # get stock ticker from the user
        tckr = input("Please enter a stock ticker (example: MSFT, TSLA, SONY): ")
        stock = yfinance.Ticker(tckr)

        earns = stock.earnings

        # print an error if the ticker doesn't exist
        earns_str = str(earns)
        empty = "Empty"
        if empty in earns_str:
            print("\nStock ticker not found. Please try another.")
        else:
            print(earns)

    if choice == '3':  # add ticker to portfolio

        # get stock ticker from the user
        tckr = input("Please enter a stock ticker (example: MSFT, TSLA, SONY): ")

        # write ticker to myPortfolio.txt file, create file if it doesn't exist
        portfolio = open("myPortfolio.txt", "a")
        portfolio.write(tckr)
        portfolio.write("\n")
        portfolio.close()

        print(
            "\nTicker added to portfolio. Please note than entering the ticker incorrectly will result in no data when viewing portfolio.")

    if choice == '4':  # view portfolio

        # read tickers into a list from user's portfolio file
        portfolio = open("myPortfolio.txt", "r")
        tckrs = portfolio.readlines()

        # remove whitespace
        tckrs = [x.strip() for x in tckrs]

        # print 1 day price of each ticker in list
        for each in tckrs:
            stock = yfinance.Ticker(each)
            hist = stock.history(period="1d")
            print(each)
            print("\n")
            print(hist)
            print("\n")

    if choice == '5':  # quit
        runMenu = False

    if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
        print("Invalid choice. Try again.")

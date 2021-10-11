import yfinance as yf
import datetime


def main(symbol):
    try:
        ticker = yf.Ticker(symbol)
        todays_data = ticker.history(period='2d')

        if 'Empty DataFrame' in str(todays_data):
            raise Exception('Invalid symbol')

        company_name = ticker.info['longName']
        today = todays_data['Close'].iloc[-1]
        yest = todays_data['Close'].iloc[-2]
        change = today - yest
        percentage_change = (today - yest) / yest * 100

        print("Today:", datetime.datetime.today())
        print(company_name)
        print("today: $", str(round(today, 2)))
        print("change: $", str(round(change, 2)))
        print("percentage: ", str(round(percentage_change, 2)), "%")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    symbol = input("Please enter a symbol: ")
    main(symbol)

#Stock Portfolio Tracker Task2
# 1. Open a text file named "portfolio_report.txt" in write mode.
# 2. If the file does not exist:
#       - create a new file.
# 3. If the file already exists:
#       - remove old contents.
#       - write new contents.
# 4. Create a file object using the with statement.
# 5. Write report title into the file.
# 6. Add blank lines after the title for better formatting.
# 7. Loop through each item in the portfolio list.
# 8. Write each portfolio item on a new line.
# 9. After all items are written:
#       - write the total investment value.
# 10. Use an f-string to display the investment value.
# 11. Automatically close the file when the with block ends.
# 12. Display a success message to the user.
#Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300,
    "AMZN": 200
}
print("Available Stocks:")
for stock,price in stock_prices.items():
    print(f"{stock}: ${price}")
n = int(input("How many different stocks do you own?"))
total_investment = 0
portfolio = []
for i in range(n):
    stock_name = input("Enter Stock Name: ").upper()
    if stock_name in stock_prices:
        quantity = int(input(f"How many shares of {stock_name} do you own? "))
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        portfolio.append(f"{stock_name}: {quantity} shares, Investment: ${investment}")
    else:
        print("Stock not found!")
print("\nYour Portfolio:")
for item in portfolio:
    print(item)
print(f"\nTotal Investment: ${total_investment}")

#Save to file
with open("portfolio_report.txt", "w") as file:
    file.write("StockPortfolio Report: \n")
    for item in portfolio:
        file.write(item + "\n")
    file.write(f"\nTotal Investment: ${total_investment}\n")
print("Report saved successfully in portfolio_report.txt")

# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 170,
    "MSFT": 420
}

portfolio = {}
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

while True:

    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid quantity.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    investment = price * quantity

    print(
        stock,
        "| Quantity:", quantity,
        "| Price: $", price,
        "| Investment: $", investment
    )

    total_investment += investment

print("\nTotal Investment Value: $", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:

    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=======================\n")

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        investment = price * quantity

        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${price} | Investment: ${investment}\n"
        )

    file.write("\nTotal Investment Value: $" + str(total_investment))

print("\nPortfolio saved successfully to portfolio.txt")
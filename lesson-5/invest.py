def invest(amount, rate, years):
    for i in range(1, years + 1):
        amount = round(amount * (1 + rate), 2)
        print(f"year {i}: ${amount}")
amount = float(input("Enter the initial amount of investment: "))
years = int(input("Enter the number of years to calculate: "))
rate = float(input("Enter the interest rate (as a percentage, e.g. 5 for 5%): ")) / 100
invest(amount, rate, years)

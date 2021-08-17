def invest(amount, rate, years):
    """Calculate investments"""
    for i in range(years):
        amount = amount * (1.0 + rate)
        print(f"year {i + 1}: ${amount:.2f}")


invest(100, .05, 4)
# FX Rates
fx = {"US-Dollar": 1.10,
      "Kandaische Dollar": 1.10,
      "Schweizer Franken": 1.10,
      "Bitcoin": 0.00012}

# Sell function
def sell(euro_amount,currency):
    fx_rate = fx.get(currency)
    fx_amount = 1.1 * euro_amount * fx_rate
    return fx_amount

# buy function
def buy(currency_amount,currency):
    fx_rate = fx.get(currency)
    euro_amount = 1.1 * currency_amount/fx_rate
    return euro_amount

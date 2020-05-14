# FX Rates
fx = {"US-Dollar": 1.25,
      "Kandaische Dollar": 1.52,
      "Schweizer Franken": 1.30,
      "Bitcoin": 0.00012}

# Sell function
def sell(euro_amount,currency):
    fx_rate = fx.get(currency)
    fx_amount = 0.9 * euro_amount * fx_rate
    return fx_amount

# buy function
def buy(currency_amount,currency):
    fx_rate = fx.get(currency)
    euro_amount = 0.9 * currency_amount/fx_rate
    return euro_amount

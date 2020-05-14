fx = {"US-Dollar": 1.20,
      "Kandaische Dollar": 1.52,
      "Schweizer Franken": 1.05,
      "Bitcoin": 0.00012}

def sell(euro_amount,currency):
    fx_rate = fx.get(currency)
    fx_amount = euro_amount * fx_rate
    return fx_amount
tea_prices = {
    "masala chai": 25,
    "simple chai":10,
    "ginger chai": 100
}

prices_usd = {tea:price / 80 for tea, price in tea_prices.items()}

print(prices_usd)
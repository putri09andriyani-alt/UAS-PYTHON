def validate_price(price):
    try:
        return float(price)
    except:
        return None

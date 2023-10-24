def excluding_vat_price(price):
    if price:
        return round(price/1.15,2)
    else:
        return -1

# P decimal number
# R decimal of the original price, given the total of price + VAT
# E 115.00 -> 100.00
# P VAT is 15%, can find the original price by price/1.15, then round to 2 decimals
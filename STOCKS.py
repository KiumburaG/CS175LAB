##STOCKS##
#number of shares: 2,000
#cost per share(purchasesd): $40.00
#stockbrokeer commission: 3% of what he paid for stock

###TWO WEEKS LATER
#number of shares sold: 2,000
#cost per share(sold): $42.75
#stockbrokeer commission: 3% of what he recieved for stock


commision_purchased = float(input("Enter commission rate percentage (ex 0.03) on stock purchase: "))
commision_sold = float(input("Enter commission rate percentage (ex 0.03) on stock sale: "))
num_shares_purchased = float(input("Enter number of shares purchased: "))
num_shares_sold = float(input("Enter number of shares sold: "))
cost_per_share_purchased = float(input("Enter purchased price per share: "))
cost_per_share_sold = float(input("Enter sell price per share: "))

amount_purchased = num_shares_purchased * cost_per_share_purchased
commission_purchased = amount_purchased * commision_purchased
amount_sold = num_shares_sold * cost_per_share_sold
commission_sale = amount_sold * commision_sold
profit = amount_sold - amount_purchased - commission_purchased - commission_sale

print('')
print('Amount paid for the stock: $', amount_purchased)
print('Commission paid on the purchase: $', commission_purchased)
print('Amount the stock sold for: $', amount_sold)
print('Commision paid on the sale: $', commission_sale)
print('Profit (or loss if negative): $', profit)

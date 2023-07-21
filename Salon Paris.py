#Data from Salon Paris


#the names of the cuts offered at Salon Paris
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# the price of each hairstyle in the hairstyles list.
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# the number of purchases for each hairstyle type in the last week.
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Each index in hairstyles corresponds to an associated index in prices and last_week.

# Average price of a cut 
total_price = 0

for price in prices:
  total_price += price

average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)

#Average price is more expensive than expected! 
#Cutting all prices by 5 pounds
new_prices = [price - 5 for price in prices]
print(new_prices)

#Revenue brought in last week
total_revenue = 0

for i in range(len(hairstyles)): 
  total_revenue += (prices[i] * last_week[i])
print("Total Revenue last week: ", total_revenue)

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)


#Advertise all cuts under 30 pounds
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)





 
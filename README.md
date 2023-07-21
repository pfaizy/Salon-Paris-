# Salon Paris 
This is a project I made when I was a data analyst at Salon Paris. I wanted to show and utuilise my knowledge of loops.  
It was my job to go through the lists of data that had been collected in the past couple of weeks, and  calculate some important metrics that Salon Paris can use to plan out the operation of the business for the rest of the month. 

The data I was given was: 
hairstyles: the names of the cuts offered at Carly’s Clippers.
prices: the price of each hairstyle in the hairstyles list.
last_week: the number of purchases for each hairstyle type in the last week.

I organise this data into lists so the manipulation of data could be easier.Each index in hairstyles corresponds to an associated index in prices and last_week.

The first step was to calculate what the average price of a cut was. I looped through the prices list and added each price to the variable total_price.
After my loop, I created a variable called average_price that is the total_price divided by the number of prices.
I got the number of prices by using the len() function. 
I printed the value of average_price so the output looked like: 
Average Haircut Price: <average_price>

The average price was much more expensive than the manager wanted and so I cut all the prices by £5.00.
I used a list comprehension to make a list called new_prices, which had each element in prices minus 5.

Another task I was given was to make sure that Salon Paris was a profitable endeavor. 
First I wanted to know how much revenue was brought in last week.
I used a for loop to create a variable i that goes from 0 to len(hairstyles) by using range()
I then added the product of prices[i] and last_week[i] (to total_revenue at each step.
After my loop, I printed the value of total_revenue so the output looked like: 
Total Revenue: <total_revenue>

The last part of the project was to advertise all of the haircuts at Salon Paris that are under 30 pounds. 
I did this by using a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.
I used range() in your list comprehension to make i go from 0 to len(new_prices) - 1.

Overall this whole project was really enjoyable. I used my knowledge of loops in Python, to help make the data analysis easier, as the data was in the forms of lists. 


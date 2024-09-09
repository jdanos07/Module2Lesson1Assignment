# Line 3-8 is train of thought 1

# intial_investment = 10000
#interest_rate = 0.07
#roi = intial_investment * interest_rate
#year1_balance = roi + intial_investment

#print(year1_balance)

# Line 12-21 is train of thought 2

#account_balance = 10000
#interest_rate = 0.07

#Account balance after year 1
#account_balance += (interest_rate * account_balance)
#print(account_balance)

#Account balance after year 2 assuming 0 withdrawls or depsosits
#account_balance += (interest_rate * account_balance)
#print(account_balance)

# Line 25-40 is train of thought 3

intial_invenstment = 10000
interest_rate = 0.07
annual_roi = interest_rate + 1
number_of_growth_years = 1

#year 1 balance
#account_balance = intial_invenstment * annual_roi
#print(account_balance) 

#year 2 balance
#account_balance = account_balance * annual_roi
#print(account_balance) 

#year 3 balance
#account_balance = account_balance * annual_roi
#print(account_balance) 


# Line 45-46 is train of thought 4
# with some Google assistance for the proper formula.

final_balance = (intial_invenstment * ((annual_roi)**(number_of_growth_years)))
print(final_balance)


#I knew there was an equation for compound growth interest.
#I just had to goolge it. But I wanted to rack my brain
#a few times before I did so. 

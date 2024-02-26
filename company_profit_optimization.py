from scipy.optimize import minimize

#* Example situation:
#*
#* A company is considering of getting new machinery for their company in the future.
#* The old machinery profits them 4000€ per day.
#* Every day that the machinery runs it profits 1€ less than the day before.
#* A new machinery would make them 4100€ per day.
#* The new machinery would make everyday 0.5€ less than the day before after the installation.
#* Installing the new machinery will take 30 days and so the company will lose 30 days of profit.
#* The company is wondering when is the best time to get the new machinery to make the most profit
#* in the following 5 years.
#* The earliest they can get the new machinery is after a year.

      
old_machinery_profit = 4000
new_machinery_profit = 4100
old_profit_loss = 1
new_profit_loss = 0.5

days_for_installation = 30
days_min = 365
days_max = 1825


# x1 is the days old machinery runs for
# x2 is the days new machinery runs for
# lets return negative number from the function so the minimize works as "maximize"
def objective(x):
    x1 = x[0]
    x2 = x[1]
            #By calculating average and multiblying it with the days old machine is online we get he profit it makes
    return -((old_machinery_profit + old_machinery_profit - x1 * old_profit_loss)/2 * x1  +  
            #Same for new machine
            ((new_machinery_profit + new_machinery_profit-(x2 - days_for_installation)*new_profit_loss)/2) * (x2 - days_for_installation) -
                # We subtract the profit that is loss while they are changing the old machine to new one
            (old_machinery_profit-x1*old_profit_loss + old_machinery_profit - (x1 + days_for_installation)*old_profit_loss)/2 * days_for_installation)


#The amount of days company wants to see the best results
def equality_constraint(x):
    x1 = x[0]
    x2 = x[1]
    return x1 + x2 - days_max

#The earliest the company would get new machinery
def inequality_constraint1(x):
    x1 = x[0]
    x2 = x[1]
    return -x1 + -x2 + days_max

bounds_x1 = (days_min,days_max)
bounds_x2 = (days_min,days_max)

bounds = [bounds_x1,bounds_x2]

constraint1 = {"type": "ineq", "fun": inequality_constraint1}
constraint2 = {"type": "eq", "fun": equality_constraint}

constraint = [constraint1,constraint2]

x0 = [700,1125]

result = minimize(objective,x0,method = "SLSQP", bounds= bounds, constraints=constraint)

print(result)

print(f"Maximun profit : {-result.fun}.")
print(f"Optimal solution : {result.x}.")
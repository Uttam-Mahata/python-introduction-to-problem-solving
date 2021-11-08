"""
Write a Python program to calculate the amount 
payable if money has been lent on simple interest. Principal or money lent = P, Rate of interest = R% 
per annum and Time = T years. Then Simple Interest 
(SI) = (P x R x T)/ 100. 
 Amount payable = Principal + SI. 
 P, R and T are given as input to the program.
"""
principal_amount = int(input("Enter the principal amount : "))
p = principal_amount
rate_of_interest = float(input("Enter the rate of interest : "))
r = rate_of_interest
t = float(input("Enter the time for which the interest will be given(Enter the time in years) : "))
interest = float((p*r*t)/100)
payable_amount = interest + p
print('Payable amount is : ', payable_amount)

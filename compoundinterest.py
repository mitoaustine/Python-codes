def comp_interest(p,r,t):
    ci=p*(1+r/100)*t
    return ci
p=float(input("enter the initial principal :"))
r=float(input("enter the interest rate :"))
t=float(input("enter the number of time periods elapsed :"))
print("The compound interest is",comp_interest(p,r,t))
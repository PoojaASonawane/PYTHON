basics = int(input("Enter basic salary"))

# To calulate Gross Salary


if basics <= 10000:
    hra = basics * 0.2
    da = basics * 0.
elif basics <= 20000:
    hra = basics * 0.25
    da = basics * 0.9
elif basics > 20000 :
    hra = basics * 0.3
    da = basics * 0.95

grosssalary = basics + hra + da
print("Gross Salary is",grosssalary)
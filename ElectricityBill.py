euc = int(input("Enter electricity unit charges"))

if euc <= 50:
    rs = euc * 0.50
elif euc > 50 and euc <= 150:
    rs = euc * 0.75
elif euc > 150 and euc <= 250:
    rs = euc * 1.20
elif euc > 250:
    rs = euc * 1.50

totalbill = rs + rs*0.2
print("Total Electricity Bill",totalbill)


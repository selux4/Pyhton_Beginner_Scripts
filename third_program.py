"""
COMP.CS.100 The second Python program
Crearter: Firuze Selin Arslan
Student ID Number: 150930868
"""
input_line = input("Enter the amount of the study benefits: ")
benefit = float(input_line)
raised_benefit1 = benefit * 1.0117
raised_benefit2 = benefit * 1.0235368900000001
print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be", raised_benefit1, "euros")
print("and if there was another index raise, the study")
print("benefits would be as much as" ,raised_benefit2, "euros")

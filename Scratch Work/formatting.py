cost1 = 3.07
tax1 = round(cost1 * 0.06, 2)
total1 = cost1 + tax1

print(f"Cost:  ${cost1:5.2f}")
print(f"Tax:    {tax1:5.2f}")
print(f"-------------")
print(f"Total: ${total1:5.2f}")

cost2 = 5.07
tax2 = round(cost2 * 0.06, 2)
total2 = cost2 + tax2

print()
print(f"Cost:  ${cost2:5.2f}")
print(f"Tax:    {tax2:5.2f}")
print(f"-------------")
print(f"Total: ${total2:5.2f}")

print()
grand_total = total1 + total2
print(f"Grand total: ${grand_total:5.2f}")

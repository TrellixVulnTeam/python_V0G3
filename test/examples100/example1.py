import sys
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1] 
profit = int(raw_input("profix = "));
award = 0
for index in range(0, 6):
    if (profit > arr[index]):
        award += (profit - arr[index]) * rat[index]
        profit = arr[index]
print award


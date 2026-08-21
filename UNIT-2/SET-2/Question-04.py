rang = int(input("Enter range of the series: "))
sum = 1
for i in range(1,rang+1):
    sum += (1/i)
print(f"Sum of the series to your given range is {sum}")
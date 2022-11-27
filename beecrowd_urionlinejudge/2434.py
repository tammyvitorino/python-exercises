n = input().split()

days = int(n[0])
balance = int(n[1])

minor_balance = balance

for i in range(days):
    balance = balance + int(input())
    if balance < minor_balance:
        minor_balance = balance

print(minor_balance)
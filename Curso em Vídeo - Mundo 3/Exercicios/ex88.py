from random import randint
from time import sleep
totalTickets = []
actualTicket = []
i = 0

print("=" * 45)
print(f"{'TICKETS FOR LOTERY':^45}")
print("=" * 45)
numTickets = int(input("=> How many tickets you want? "))
print("=" * 45)

while i < numTickets:
    for c in range(6):
        num = randint(1, 60)
        if num not in actualTicket:
            actualTicket.append(num)

    actualTicket.sort()
    totalTickets.append(actualTicket[:])
    actualTicket.clear()
    i += 1

for pos, ticket in enumerate(totalTickets):
    print(f"Ticket N°{pos + 1} -> {ticket}")
    sleep(0.5)

print(f"{'GOOD LUCK!':=^45}")

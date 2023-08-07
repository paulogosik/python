numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
option = int(input("=> Type a number between 0 and 20: "))

while option < 0 or option > 20:
    option = int(input("=> Try again! Type a number between 0 and 20: "))
    
print(f"----------------------")
print(f"=> You typed the number {numbers[option]}")
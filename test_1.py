"""
The program is trying to determine which payment option is better between the two available options.
The first option is $100 per day for 10 days. The second option is $1 a day with the doubling effect each day for 10 days.
The pay rate will be calculated by two functions. The function option1 will calculate the amount for the first option. The
function option2 will calculate the amount for the second option.

The function option1 will print out $100 times 10 days.
The function option2 will loop through 10 times, doubling and adding to the total amount each time.

If the amount is equal, then we print out "Option 1 and Option 2 pays the same".
If option 1 is better, then we print out "Option 1 is better".
If option 2 is better, then we print out "Option 2 is better".
"""

"""
# Option1 
    return 100 * 10

# Option2
    amount = 1
    list1 = []
    loop 10 times 
        add amount to list1
        amount *= 2
    sum = sum of all items in loop  
    return sum

# main 
var1 = option1
var2 = option2

if var1 = var2
    "Option 1 and Option 2 pays the same"
if var1 > var2 
    "Option 1 is better"
else 
    "Option 2 is better"

run main function
"""

def option1():
    return 100 * 10

def option2():
    amount = 1
    list1 = []
    for i in range(0, 10):
        list1.append(amount)
        amount *= 2 
    total = sum(list1)
    return total

def main(): 
    answer = ""
    var1 = option1()
    var2 = option2()
    if var1 == var2:
        answer = "Option 1 and Option 2 pays the same"
    if var1 > var2:
        answer = "Option 1 is better"
    else:
        answer = "Option 2 is better"
    print(answer)

main()
#try:
#    print(5/0)
#except ZeroDivisionError:
#    print("You can't divide by zero")

print("Give me two numbers, and I'll divide them")
print("Enter 'q' to quit.")

while True:
    first_number = raw_input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = raw_input("Second number: ")
    #if second_number == 'q':
    #    break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can'y divide by 0!")
    else: 
        print(answer)

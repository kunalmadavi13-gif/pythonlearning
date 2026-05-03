def even_number(number):
    for i in range(1,number):
        if i %2 == 0:
            print(f"even numbers: {i}")

def odd_number(number):
    for i in range(1,number):
        if i %2 != 0:
            print(f"odd numbers: {i}")

num = int(input("Enter range from which you want odd number: "))
odd_number(num)
even_number(num)




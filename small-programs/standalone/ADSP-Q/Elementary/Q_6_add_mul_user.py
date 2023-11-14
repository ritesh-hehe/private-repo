# Write a program that asks the user for a number n and gives them the possibility to choose between
# computing the sum and computing the product of 1,…,n.

def compute_sum(n: int) -> int:
    sumNow = 0
    for i in range(1, n+1):
        sumNow += i
    return sumNow


def compute_pdt(n: int) -> int:
    pdtNow = 1
    for i in range(1, n+1):
        pdtNow *= i
    return pdtNow


number = int(input("Enter the value of n: "))
print("Press 1 to find sum till n")
print("Press 2 to find product till n")
query = int(input("Enter choice: "))

match(query):
    case 1:
        print(f"The value of sum till {number} is: {compute_sum(number)}")
    case 2:
        print(f"The value of product till {number} is: {compute_pdt(number)}")
    case default:
        print("Invalid Input")

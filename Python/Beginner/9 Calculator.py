def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operators={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

ch="n"

while ch=="n":
    print("\n"*100)
    ch = "y"

    n1 = float(input("What's the first number?: "))

    def display(n1):
        for oper in operators:
            print(oper)
        op = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        ans = operators[f"{op}"](n1, n2)
        print(f"{n1} + {n2} = {ans}")
        ch = input(f"Type 'y' to continue calculating with {ans}, or type 'n' tp start a new calculation: ")
        n1 = ans
        return ch, n1

    while ch == "y":
        ch,n1=display(n1)

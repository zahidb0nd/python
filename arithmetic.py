def add(a,b):
    return a+b

def sub(a,b):
    return a-b 

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return "error: division by zero is not allowed"
    return a/b 

def main():
    
    a = int(input("Enter the value of a:\n"))
    b = int(input("Enter the value of b:\n"))
    
    add_result=add(a,b)
    sub_result=sub(a,b)
    mul_result=mul(a,b)
    div_result=div(a,b)
    
    print(f"Addition result: {add_result}")
    print(f"Subtraction result: {sub_result}")
    print(f"Multiplication result: {mul_result}")
    print(f"Division result: {div_result}")



if __name__=="__main__":
    main()

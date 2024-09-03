def trapezium(base1, base2, height):
    area = 0.5*(base1+base2)*height
    return area

def main():
    base1 = float(input("Enter the value of base1:\n"))
    base2 = float(input("Enter the value of base2:\n"))
    height = float(input("Enter the value of height:\n"))

    area = trapezium(base1, base2, height)
    print(f"The area of trapezium is {area}")

if __name__=="__main__":
    main()

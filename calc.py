def plus(x: float, y: float) -> float:
    return x+y

def main():
    check = 1
    print("Welcome to calculator")
    while check >= 1:
        print("0: exit, 1: plus")
        check = int(input())
        if check == 1:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", plus(x,y))
        elif check > 1:
            print("Unsupported")
        else:
            print("Thank you")

if __name__ == "__main__":
    main()

    #소수점 연산이 가능하도록 코드 수정
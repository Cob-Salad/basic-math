

def add(x: float, y: float) -> float:
    return x + y

def multiply(x: float, y: float) -> float:
    return x * y

def square(x: float) -> float:
    z = multiply(x, x)
    return z

def add_square(x: float, y: float) -> float:
    a = square(x)
    b = square(y)
    c = add(a, b)
    return c


def main():
    print(add(5, 6))
    print(multiply(5, 5))
    print(square(2))
    print(add_square(2, 3))

if __name__ == "__main__":
    main()    

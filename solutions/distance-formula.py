import math

def main():
    # test the formula a bit
    d1 = distance(-2, 1, 1, 5)
    print(f"(-2,1) to (1,5) => {d1}")
    d2 = distance(-2, -3, -4, 4)
    print(f"(-2,-3) to (-4,4) => {d2}")
    print(f"(2,-3) to (-1,-2) => {distance(2, -3, -1, -2)}")
    print(f"(4,5) to (4,5) => {distance(4, 5, 4, 5)}")

def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    # Calculate the distance using the distance formula
    # d = sqrt((x2-x1)^2 + (y2-y1)^2)
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if __name__ == "__main__":
    main()
"""간단한 사칙연산 계산기."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(a, op, b):
    if op not in OPERATIONS:
        raise ValueError(f"지원하지 않는 연산자입니다: {op}")
    return OPERATIONS[op](a, b)


def main():
    print("계산기 (예: 3 + 4, 종료: q)")
    while True:
        line = input("> ").strip()
        if line.lower() == "q":
            break
        try:
            a, op, b = line.split()
            print(calculate(float(a), op, float(b)))
        except ValueError as e:
            print(f"오류: {e}")


if __name__ == "__main__":
    main()

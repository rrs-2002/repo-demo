def do_add(a: int, b: int) -> int:
    return a + b
    
def do_subtract(a: int, b: int) -> int:
    return a - b

def do_multiply(a: int, b: int) -> int:
    return a * b

def do_divide(a: int, b: int) -> float:
    if b == 0:
        return 0
    return a / b
def sqrt(x: int) -> float:
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    if x == 0:
        return 0.0
    guess = x / 2.0
    while True:
        new_guess = (guess + x / guess) / 2.0
        if abs(new_guess - guess) < 1e-10:
            return new_guess
        guess = new_guess

PENDING = 0
STORED = 20
SALLED = 0

def buy(qty: int) -> int:
    global STORED, PENDING, SALLED
    if qty > STORED:
        raise Exception("No items in storage")
    STORED -= qty
    SALLED += qty
    return STORED, PENDING, SALLED

def liquidate(qty: int) -> int:
    global STORED, PENDING, SALLED
    if qty > PENDING:
        raise Exception("Not enough items reserved")
    PENDING -= qty
    SALLED += qty
    return STORED, PENDING, SALLED

def reserve(qty: int) -> int:
    global STORED, PENDING, SALLED
    if qty > STORED:
        raise Exception("Not enough items in storage")
    STORED -= qty
    PENDING += qty
    return STORED, PENDING, SALLED

def store(qty: int) -> int:
    global STORED, PENDING, SALLED
    STORED += qty
    return STORED, PENDING, SALLED


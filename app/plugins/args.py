from decimal import Decimal, InvalidOperation
from typing import List, Tuple
# 
def parse_two_decimal_args(args: List[str]) -> Tuple[Decimal, Decimal]:
    if len(args) != 2:
        raise ValueError("Usage: command <number1> <number2>")
    
    try:
        num1 = Decimal(args[0])
        num2 = Decimal(args[1])
        return num1, num2
    except InvalidOperation:
        raise ValueError("Invalid number format")
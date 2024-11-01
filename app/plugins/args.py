from decimal import Decimal, InvalidOperation
import logging
from typing import List, Tuple
# 
def get_args(args: List[str]) -> Tuple[Decimal, Decimal]:
    if len(args) != 2:
        logging.warning(f"Invalid number of arguments: {args}")
        raise ValueError("Usage: command <number1> <number2>")
    
    try:
        num1 = Decimal(args[0])
        num2 = Decimal(args[1])
        return num1, num2
    except InvalidOperation:
        logging.error(f"Invalid number format: {args}")
        raise ValueError("Invalid number format")
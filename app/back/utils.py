from typing import Final
from re import fullmatch


def in_rect(p_x: int, p_y: int, r_x: int, r_y: int, r_w: int, r_h: int) -> bool:
    # Menu Bar takes 20 pixels
    MBAR_MARGIN: Final[int] = 20

    if p_x in range(r_x, r_x + r_w) and \
       p_y in range(
        MBAR_MARGIN + r_y, MBAR_MARGIN + r_y + r_h
    ):
        return True
    else:
        return False


def is_valid_psw(password: str) -> bool:
    """
    (?=^.{8,}$) -- at least 8 symbols
    ((?=.*\d)|(?=.*\W+)) -- 0 or more symbols and 1 digit or 1 or more non-digital non-latin letter symbols
    (?![.\n]) -- no \n or . before string
    (?=.*[A-Z]) -- any Capital latin letter after string
    (?=.*[a-z]) -- any small latin letter after string
    .*$ -- one or more symbols before the end of string
    """
    pattern = '(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
    return fullmatch(pattern, password) is not None

from typing import Final


def in_rect(p_x: int, p_y: int, r_x: int, r_y: int, r_w: int, r_h: int):
    # Menu Bar takes 20 pixels
    MBAR_MARGIN: Final[int] = 20

    if p_x in range(r_x, r_x + r_w) and \
       p_y in range(
        MBAR_MARGIN + r_y, MBAR_MARGIN + r_y + r_h
    ):
        return True
    else:
        return False

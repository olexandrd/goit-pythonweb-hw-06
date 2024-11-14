from my_select import (
    select_1,
    select_2,
    select_3,
    select_4,
    select_5,
    select_6,
    select_7,
    select_8,
    select_9,
    select_10,
)

from connect import Session

if __name__ == "__main__":
    with Session() as s:
        select_1(s)
        select_2(s)
        select_3(s)
        select_4(s)
        select_5(s)
        select_6(s, 2)
        select_7(s, 1, "Biology")
        select_8(s)
        select_9(s, 2)
        select_10(s, 1, 1)

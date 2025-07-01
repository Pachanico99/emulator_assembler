
include "math.asm"

main:

    ; sqrt
    Push 25
    Call sqrt
    Mov bx, 1
    Mov cx, 2
    int 1


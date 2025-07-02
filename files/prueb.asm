
include "math.asm"

main:

    Push 10     ; dividendo
    Push 3    ; divisor
    Call dividir
    Mov bx, 1
    Mov cx, 1
    Int 1

    Push 10     ; dividendo
    Push 2    ; divisor
    Call dividir
    Mov bx, 1
    Mov cx, 2
    Int 1

    Push 10
    Push 0
    Call dividir
    Mov bx, 1
    Mov cx, 3
    Int 1

    Push 5
    Push 10
    Call dividir
    Mov bx, 1
    Mov cx, 4
    Int 1

    push 1
    call restar
    mov bx, 4
    mov cx, 1
    int 1

    push 16
    call restar
    mov bx, 4
    mov cx, 2
    int 1

    push 8
    call restar
    mov bx, 4
    mov cx, 3
    int 1

    push 5
    push 2
    call restar
    mov bx, 4
    mov cx, 4
    int 1

    push 10
    call sqrt
    mov bx, 2
    mov cx, 1
    int 1

    push 16
    call sqrt
    mov bx, 2
    mov cx, 2
    int 1

    push 8
    call sqrt
    mov bx, 2
    mov cx, 3
    int 1

    push 3
    call sqrt
    mov bx, 2
    mov cx, 4
    int 1

    push 5
    push 2
    call multiplicar
    mov bx, 3
    mov cx, 1
    int 1

    push 3
    push 2
    call multiplicar
    mov bx, 3
    mov cx, 2
    int 1

    push 1
    push 2
    call multiplicar
    mov bx, 3
    mov cx, 3
    int 1

    push 0
    push 2
    call multiplicar
    mov bx, 3
    mov cx, 4
    int 1

    push 1
    push 5
    call sumar
    mov bx, 5
    mov cx, 1
    int 1

    push 3
    push 2
    call sumar
    mov bx, 5
    mov cx, 2
    int 1

    push 1
    push 2
    call sumar
    mov bx, 5
    mov cx, 3
    int 1

    push 0
    push 2
    call sumar
    mov bx, 5
    mov cx, 4
    int 1
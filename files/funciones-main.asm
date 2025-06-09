include "funciones-suma.asm"
include "funciones-resta.asm"

main:
        push 5
    push 7

    call sumar
    dec ax
    
    ; Resultado en AX

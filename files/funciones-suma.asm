;include 'funciones-resta.asm' ; Hola


sumar:

    pop bx       ; Retorno
    pop cx       ; 7
    pop dx       ; 5

    push bx      ; Guardamos de nuevo el retorno

    add cx, dx   ; cx = cx + dx
    mov ax, cx   ; resultado en AX

    ret

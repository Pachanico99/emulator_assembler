; math.asm
; Libreria para hacer operaciones matematicas basicas (suma, resta, multiplicacion y division)

    ; --- SUMAR ---
    sumar:
        Pop aux
        Pop bx     ; op1
        Pop ax     ; op2
        Push aux
        Add ax, bx
        Ret



    ; --- RESTAR ---
    restar:
        Pop aux
        Pop bx     ; op1
        Pop ax     ; op2
        Push aux

        restar_loop:
            Cmp 0, bx
            Jnz restar_dec
            Ret

        restar_dec:
            Dec ax
            Dec bx
            Jmp restar_loop


    ; --- MULTIPLICAR ---
    multiplicar:
        Pop aux        ; dirección de retorno
        Pop bx         ; op1 (valor a sumar)
        Pop cx         ; op2 (cantidad de veces)
        Push aux       ; restauramos ret

        ; si op1 == 0 o op2 == 0 → resultado = 0
        Cmp 0, bx
        Jnz multiplicar_check_op2
        Mov ax, 0
        Ret

        multiplicar_check_op2:
            Cmp 0, cx
            Jnz multiplicar_inicio
            Mov ax, 0
            Ret

        multiplicar_inicio:
            Mov ax, 0      ; acumulador arranca en 0

        multiplicar_loop:
            Cmp 0, cx      ; si cx > 0 → saltamos
            Jnz multiplicar_sumar
            Ret

        multiplicar_sumar:
            Push ax
            Push bx
            Call sumar     ; ax = ax + bx
            Dec cx
            Jmp multiplicar_loop



    ; --- RAIZ CUADRADA --- no funca de momento
    sqrt:
        Pop aux
        Pop bx         ; número del cual sacar raíz
        Push aux

        ; si bx == 0 → raíz = 0
        Cmp 0, bx
        Jnz sqrt_iniciar
        Mov ax, 0
        Ret

        sqrt_iniciar:
            Mov cx, 0         ; cx = candidato a raíz
            Mov dx, bx        ; dx = número original

        sqrt_loop:
            Inc cx            ; aumenta el valor del radicando

            Push cx           ; guardar valor de cx original
            Push cx           ; op2
            Push cx           ; op1
            Call multiplicar

            Pop cx            ; restaurar cx original

            Cmp dx, ax
            Jnz sqrt_fin      ; si ax > dx → cortar
            Jmp sqrt_loop

        sqrt_fin:
            Dec cx
            Mov ax, cx        ; raíz entera más cercana
            Ret

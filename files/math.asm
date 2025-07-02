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
    Pop bx             ; número del cual sacar raíz
    Push aux

    ; si bx == 0 → raíz = 0
    Cmp 0, bx
    Je sqrt_es_cero
    Jmp sqrt_iniciar

    sqrt_es_cero:
        Mov ax, 0
        Ret

    sqrt_iniciar:
        Mov cx, 0       ; candidato a raíz
        Mov dx, bx      ; guardar valor original

    sqrt_loop:
        Inc cx          ; cx++

        ; calcular cx * cx → resultado queda en ax
        Push cx
        Push cx
        Push cx
        Call multiplicar

        Pop cx

        ; comparar resultado (ax) con bx (dx)
        Cmp ax, dx
        Je sqrt_fin_eq     ; si ax == dx → terminamos
        Jg sqrt_fin     ; si ax > dx → terminamos
        Jmp sqrt_loop

    sqrt_fin_eq:
        Mov ax, cx
        Ret

    sqrt_fin:
        Dec cx          ; retroceder uno porque se pasó
        Mov ax, cx
        Ret



    ; --- DIVIDIR ---
    dividir:
    Pop aux
    Pop cx         ; divisor
    Pop bx         ; dividendo
    Push aux

    Cmp cx, 0
    Je division_error

    Mov dx, bx     ; dx = resto
    Mov ax, 0      ; ax = cociente

division_loop:
    Cmp dx, cx
    Jl division_fin

    Push ax
    Push dx
    Push cx
    Call restar

    Mov dx, ax
    Pop ax
    Inc ax
    Jmp division_loop

division_fin:
    Ret

division_error:
    Mov ax, 0
    Mov dx, bx
    Ret
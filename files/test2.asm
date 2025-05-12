; Este es un archivo de ejemplo limpio para testear el ensamblador.
# Permite probar comentarios, líneas vacías, etiquetas e instrucciones.

    ; Línea con solo comentario y espacios iniciales
   mov ax, 10    # Cargar el valor 10 en el registro ax
   mov bx, 2    ; Cargar el valor 20 en el registro bx

main:      ; Esta es la etiqueta de inicio del programa
    mov ax, 10    # Cargar el valor 10 en el registro ax
    mov bx, 2    ; Cargar el valor 20 en el registro bx

    # Sección de suma
add_section:
    add ax, bx    ; Sumar bx a ax (ax = 30)

    inc ax        ; Incrementar ax (ax = 31)

; Línea vacía intencional


    loop_start:     ; Etiqueta para un bucle simple (nombre único)
        dec   ax # Decrementar bx
        dec  bx # Decrementar bx
        cmp bx, 0 ; Comparar bx con cero
        jnz loop_start ; Saltar a 'loop_start' si bx no es cero

    mov cx, ax    ; Mover el resultado final (31) a cx


    ; Probar un salto simple
some_label: ; Esta etiqueta es única ahora
    jmp end_program ; Saltar al final

    ; Alguna otra instrucción si es necesario después de la etiqueta 'some_label' antes del salto.
    ; mov dx, 99 # Por ejemplo, esta instrucción


end_program: # Etiqueta de fin del programa principal
    ; Fin del código.

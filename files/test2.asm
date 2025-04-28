; Este es un archivo de ejemplo limpio para testear el ensamblador.
# Permite probar comentarios, líneas vacías, etiquetas e instrucciones.

    ; Línea con solo comentario y espacios iniciales
   mov R0, 10    # Cargar el valor 10 en el registro R0
	mov R1, 20    ; Cargar el valor 20 en el registro R1

main:      ; Esta es la etiqueta de inicio del programa
    mov R0, 10    # Cargar el valor 10 en el registro R0
    mov R1, 20    ; Cargar el valor 20 en el registro R1

    # Sección de suma
add_section:
    add R0, R1    ; Sumar R1 a R0 (R0 = 30)

    inc R0        ; Incrementar R0 (R0 = 31)

; Línea vacía intencional


    loop_start:     ; Etiqueta para un bucle simple (nombre único)
        dec R1    # Decrementar R1
        cmp R1, 0 ; Comparar R1 con cero
        jnz loop_start ; Saltar a 'loop_start' si R1 no es cero

    mov R2, R0    ; Mover el resultado final (31) a R2


    ; Probar un salto simple
some_label: ; Esta etiqueta es única ahora
    jmp end_program ; Saltar al final

    ; Alguna otra instrucción si es necesario después de la etiqueta 'some_label' antes del salto.
    ; mov R3, 99 # Por ejemplo, esta instrucción


end_program: # Etiqueta de fin del programa principal
    ; Fin del código.
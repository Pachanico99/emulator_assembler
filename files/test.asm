; Este es un archivo de ejemplo para testear el ensamblador.
# Permite probar comentarios, líneas vacías, etiquetas e instrucciones.

    ; Línea con solo comentario y espacios iniciales

start:      ; Esta es la etiqueta de inicio del programa
    mov R0, 10   # Cargar el valor 10 en el registro R0
    mov R1, 20   ; Cargar el valor 20 en el registro R1

    # Sección de suma
add_section:
    add R0, R1   ; Sumar R1 a R0 (R0 = 30)

    inc R0       ; Incrementar R0 (R0 = 31)

; Línea vacía intencional


    loop:        ; Etiqueta para un bucle simple
        dec R1   # Decrementar R1
        cmp R1, 0 ; Comparar R1 con cero
        jnz loop ; Saltar a 'loop' si R1 no es cero

    mov R2, R0   ; Mover el resultado final (31) a R2


    ; Probar una etiqueta duplicada (debería causar un error)
some_label:
    jmp end_program ; Saltar al final

some_label: ; Esta etiqueta está duplicada - ¡ERROR ESPERADO!
    mov R3, 99  # Esta instrucción no debería ser procesada si hay error de etiqueta

end_program: # Etiqueta de fin
    ; Fin del código.
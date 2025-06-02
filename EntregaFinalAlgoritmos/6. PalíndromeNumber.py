def is_palindrome(self, x: int) -> bool:
    # Los números negativos no son palíndromos
    if x < 0:
        return False

    original = x
    reversed_num = 0

    # Revertir el número
    while x != 0:
        digit = x % 10
        # Verificar desbordamiento antes de multiplicar
        if reversed_num > (2**31 - 1) // 10 or (reversed_num == (2**31 - 1) // 10 and digit > 7):
            return False  # Si hay desbordamiento, no es un palíndromo válido
        reversed_num = reversed_num * 10 + digit  #Construye el numero revertido multiplicado
        x //= 10

    # Comparar el número original con el revertido
    return original == reversed_num

#Este codigo es Big-O Log de n, O(log n)

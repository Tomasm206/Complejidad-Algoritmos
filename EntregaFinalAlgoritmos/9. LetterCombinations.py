def letterCombinations(digits):
    # Mapeo de dígitos a letras
    digit_to_letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    # Lista para almacenar las combinaciones
    combinations = []

    # Función de backtracking
    def backtrack(index, current_combination):
        # Si la combinación actual tiene la misma longitud que los dígitos, agregarla a las combinaciones
        if len(current_combination) == len(digits):
            combinations.append("".join(current_combination))
            return

        # Obtener las letras correspondientes al dígito actual
        current_digit = digits[index]
        letters = digit_to_letters[current_digit]

        # Recorrer cada letra y construir la combinación
        for letter in letters:
            current_combination.append(letter)  # Agregar la letra a la combinación actual
            backtrack(index + 1, current_combination)  # Llamar recursivamente para el siguiente dígito
            current_combination.pop()  # Eliminar la última letra (backtracking)

    # Si hay dígitos, iniciar el backtracking
    if digits:
        backtrack(0, [])

    return combinations


#Este codigo es Big-O de m elevado a la n.
#O(m^n)  m es el número máximo de letras por dígito y n es la longitud de los digitos
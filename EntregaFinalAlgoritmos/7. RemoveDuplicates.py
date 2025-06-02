def removeDuplicates(nums):
    # Si el arreglo está vacío, no hay nada que hacer
    if not nums:
        return 0

    # Puntero para colocar elementos únicos
    k = 1

    # Recorrer el arreglo desde el segundo elemento
    for i in range(1, len(nums)):
        # Si el elemento actual es diferente al anterior, es único
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]  # Colocarlo en la posición k
            k += 1  # Incrementar el puntero k

    # Devolver el número de elementos únicos
    return k


#Este codigo es Big-O de n, O(n)
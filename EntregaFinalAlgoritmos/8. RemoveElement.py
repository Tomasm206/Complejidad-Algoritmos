def removeElement(nums, val):
    # Puntero para colocar elementos que no son iguales a val
    k = 0

    # Recorrer el arreglo
    for i in range(len(nums)):
        # Si el elemento actual no es igual a val, colocarlo en la posición k
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1  # Incrementar el puntero k

    # Devolver el número de elementos que no son iguales a val
    return k


#Este codigo es Big-O de n, O(n)
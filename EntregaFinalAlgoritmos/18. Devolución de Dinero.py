def min_coins(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if amount == 0:
            break
        if coin <= amount:
            count += amount // coin
            amount %= coin
    return count if amount == 0 else -1

# Ejemplo de uso
if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    amount = int(input("Ingrese la cantidad de dinero: "))
    result = min_coins(coins, amount)
    if result != -1:
        print(f"Se necesitan {result} monedas.")
    else:
        print("No es posible hacer el cambio con las monedas disponibles.")
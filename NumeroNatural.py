def obtener_numero_natural():

    while True:
        try:
            numero = int(input("Ingrese un número natural: "))
            if numero < 1:
                raise ValueError("El número debe ser mayor que cero.")
            return numero
        except ValueError as e:
            print(f"Error: {e}. Por favor, intente nuevamente.")


def calcular_divisores(numero):

    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores


def main():

    print("Bienvenido a la calculadora de divisores.")

    numero = obtener_numero_natural()

    divisores = calcular_divisores(numero)

    print(f"Los divisores de {numero} son: {divisores}")


if __name__ == '__main__':
    main()
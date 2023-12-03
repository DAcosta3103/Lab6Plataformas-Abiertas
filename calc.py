# Primero se crea una función para solicitar la información del usuario
def get_user_input():
    try:
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operation = input("Elija una operacion (+, -, *, /) o escriba 'exit' para salir: ") #Se pregunta al usuario qué operación desea
        return num1, num2, operation
    except ValueError:
        print("Input invalido. Por favor ingrese numeros.") #Se ingresa un caracter no autorizaeo
        return get_user_input()

# Esta función se encarga de ejecutar una operación matemática basada en la entrada del usuario.
def ejecutar_operacion(user_input, callback):
    num1, num2, operation = user_input
    try:
        result = callback(num1, num2)
    except Exception as e:
        result = f"Error: {e}"

    print("Resultado:", result)



# Esta es la función main, la cual maneja el flujo de la calculadora.
def main():
    operations = {
        '+': lambda x, y: x + y, #Función lambda para la suma
        '-': lambda x, y: x - y, #Función lambda para la resta
        '*': lambda x, y: x * y, #Función lambda para la multiplicación
        '/': lambda x, y: x / y if y != 0 else "Error: División por cero" #Función lambda para la división, tomando en cuenta indeterminación num/0
    }
    # Mantiene un bucle que solicita constantemente la entrada del usuario, ejecuta la operación seleccionada y muestra el resultado. 
    while True:
        user_input = get_user_input()
        if user_input[2].lower() == 'exit': # Se posibilita la interrupción del bucle si el usuario ingresa "exit"
            print("Salir.")
            break

        print("\nCalculando...")
        if user_input[2] in operations:
            ejecutar_operacion(user_input, operations[user_input[2]])
        else:
            print("Operación inválida.")

if __name__ == "__main__":
    main()

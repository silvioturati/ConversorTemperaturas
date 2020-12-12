"""
Programa em Python para converter temperatura em Celsius para Kelvin e Fahrenheit
"""

from helpers import celsius_to_kelvin, celsius_to_fahrenheit

if __name__ == '__main__':
    print("* Conversor de Temperaturas *")
    while True:
        temperatura_celsius = input("\nDigite o valor da temperatura em Celsius ou SAIR para encerrar: ")
        try:
            if temperatura_celsius.lower() != "sair":
                print(f"\nA temperatura {temperatura_celsius} em Celsius é igual a {celsius_to_kelvin(float(temperatura_celsius))} em kelvin")
                print(f"A temperatura {temperatura_celsius} em Celsius é igual a {celsius_to_fahrenheit(float(temperatura_celsius))} em Fahrenjeit")
            else:
                print("\nObrigado por usar nosso sistema, até a próxima!")
                break
        except ValueError:
            print(f"\nVocê digitou algo errado. Tente de novo.")
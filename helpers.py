def celsius_to_kelvin(temperatura_celsius):
    """
    Função para converter temperatura em celsius para Kelvin
    :param temperatura_celsius:
    :return: temperatura_kelvin
    Fórmula: C + 273.15
    """
    temperatura_kelvin = temperatura_celsius + 273.15
    return temperatura_kelvin

def celsius_to_fahrenheit(temperatura_celsius):
    """
    Função para converter temperatura de celcius para fahrenheit
    :param temperatura_celsius:
    :return: temperatura_fahrenheit
    Fórmula: (C * (9/5))+32
    """
    temperatura_fahrenheit = (temperatura_celsius * (9/5))+32
    return temperatura_fahrenheit
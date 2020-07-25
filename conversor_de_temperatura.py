continuar = "s"

while continuar == "s":
    termometro = str(input("Para qual a medida de temperatura deseja converter: Fahrenheit[F] ou Celsius[C]? "))
    temperatura = float(input("Qual a temperatura atual? "))

    if termometro == "C" or termometro == "c" or termometro == "Celsius" or termometro == "celsius":
        conversao = (temperatura - 32)/1.8
        print(f"A medida em Fahrenheit é: {conversao}")

    if termometro == "F" or termometro == "f" or termometro == "Fahrenheit" or termometro == "fahrenheit":
        conversao = (((9/5) * temperatura) + 32)
        print(f"A medida em Celsius é: {conversao}")

    continuar = str(input("Deseja continar convertendo as temperaturas? "))
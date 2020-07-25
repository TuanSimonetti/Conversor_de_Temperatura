termometro = str(input("Qual a medida de temperatura deseja escolhar: Fahrenheit[F] ou Celsius[C]? "))
temperatura = float(input("Qual a temperatura atual? "))

if termometro == "F":
    conversao = (temperatura-32)/1.8
    print(f"A medida em Fahrenheit é: {conversao}")

if termometro == "C":
    conversao = (1.8*temperatura)+32
    print(f"A medida em Celsius é: {conversao}")
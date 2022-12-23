print("\nSeja bem vindo! Esse programa é um conversor de temperaturas!\n\nFunciona da seguinte maneira:")
print("Você indicará DE qual temperatura PARA qual temperatura respectivamente.")

print("\n(C) = Celsius | (K) = Kelvin | (F) = Fahrenheit")
inicio = input("Informe DE qual temperatura você quer converter: ")
fim = input("Informe PARA qual temperatura você quer converter: ")

# de Kelvin para Celsius
if (inicio == "k" or inicio == "K") & (fim == "c" or fim == "C"):
    k = float(input("\nInforme o valor em Kelvin: "))
    print(f"{k-273:.2f}°C.\n")

# de Kelvin para Fahrenheit
elif (inicio == "k" or inicio == "K") & (fim == "f" or fim == "F"):
    k = float(input("\nInforme o valor em Kelvin: "))
    print(f"{(k-273)*1.8+32:.2f}°F.\n")

# de Celsius para Kelvin
elif (inicio == "c" or inicio == "C") & (fim == "k" or fim == "K"):
    c = float(input("\nInforme o valor em Celsius: "))
    print(f"{c+273:.2f}°K.\n")

# de Celsius para Fahrenheit
elif (inicio == "c" or inicio == "C") & (fim == "f" or fim == "F"):
    c = float(input("\nInforme o valor em Celsius: "))
    print(f"{c*1.8+32:.2f}°F.\n")

# de Fahrenheit para Celsius
elif (inicio == "f" or inicio == "F") & (fim == "c" or fim == "C"):
    f = float(input("\nInforme o valor em Fahrenheit: "))
    print(f"{(f-32)/1.8:.2f}°C.\n")

# de Fahrenheit para Kelvin
elif (inicio == "f" or inicio == "F") & (fim == "k" or fim == "K"):
    f = float(input("\nInforme o valor em Fahrenheit: "))
    print(f"{(f-32)*5/9+273:.2f}°K.\n")

else:
    print("\nTECLA INVÁLIDA!\n")

#Mede o IMC o Mostra se e gordo
peso = float(input('Qual a sua altura?(Kg) '))
altura = float(input('Qual o seu peso?(m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'O seu IMC é {imc:.2f} está abaixo de 18.5, Você está ABAIXO DO PESO ideal')
elif 18.5 <= imc < 25.:
    print(f'O seu IMC é {imc:.2f} está IDEAL ao peso e altura')
elif 25 <= imc < 30:
    print(f'O seu IMC é {imc:.2f} está indicando SOBREPESO')
elif 30 <= imc < 40:
    print(f'O seu IMC é {imc:.2f} está indicando OBESIDADE')
elif imc >= 40:
    print(f'O seu imc é {imc}, Você Está com OBESIDADE Mórbida')
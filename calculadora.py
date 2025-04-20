print("BEM VINDO A CALCULADORA MÁGICA")
operacao  = input("Qual operação matemática deseja fazer: + (Soma) , - (Subtração), / (Divisão) ou * (Multiplicação)")
itemA = 0 
itemB = 0
if operacao  ==  "+"  or   operacao == "soma" or operacao == "Soma":
    itemA = int(input("digite o primeiro valor :"))
    itemB = int(input("digite o segundo valor :"))
    print(f"o resultado desta operação é :   {itemA + itemB}" )
elif operacao == "-" or   operacao == "subtração" or operacao == "Subtração":
    itemA = int(input("digite o primeiro valor :"))
    itemB = int(input("digite o segundo valor :"))
    print(f"o resultado desta operação é :  {itemA - itemB}" )
elif operacao == "/" or   operacao == "divisão" or  operacao == "divisão":
    itemA = int(input("digite o primeiro valor :"))
    itemB = int(input("digite o segundo valor :"))
    print(f"o resultado desta operação é :  {itemA / itemB}" )
else:
    itemA = int(input("digite o primeiro valor :"))
    itemB = int(input("digite o segundo valor :"))
    print(f"o resultado desta operação é :   {itemA * itemB}" )

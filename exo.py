import sys

argument = sys.argv

if len(argument) >2 or len(argument) == 1 or not argument[1].isdigit():
    print("Tu ne me la mettras pas à l'envers")
    exit()

if int(argument[1]) % 2 == 0:
    print("pair")
else:
    print("impair")
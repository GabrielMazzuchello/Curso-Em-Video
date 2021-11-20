from colorama import Fore
from colorama import Style

vetinpar = []
vetpar = []

for c in range(1, 51):
    if c % 2 == 0:
        vetinpar.append(c)
    else:
        vetpar.append(c)

print('Os numeros ímpares são: {}{}{}'.format(Fore.LIGHTRED_EX, vetinpar, Style.RESET_ALL))
print('Os numeros pares são: {}{}{}'.format(Fore.LIGHTGREEN_EX, vetinpar, Style.RESET_ALL))

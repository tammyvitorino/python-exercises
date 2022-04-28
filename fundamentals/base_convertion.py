"""
A conversão de números inteiros para diferentes bases é uma operação realizada
frequentemente em computação. Por exemplo, no dia a dia estamos habituados a trabalhar
com números na base decimal. Entretanto, o computador opera na base binária. Enquanto,
eventualmente, a inspeção visual do conteúdo da memória do computador é feita na base octal
ou hexadecimal.

Faça um programa que, dados valores inteiros na base decimal, escreva na saída padrão cada
valor convertido para as bases 2 a 9.

Seu programa deve conter um subprograma recursivo que respeite o seguinte cabeçalho, tendo
como retorno o valor convertido:
def converte(numDecimal, base):

Entrada
A entrada é composta por várias linhas vindas da entrada padrão, cada uma contando um valor
inteiro , representado na base decimal. A última linha contém o valor , que não
deve ser processado.

Saída
Uma linha deve ser emitida na saída padrão para cada valor decimal dado como entrada. Essa
linha deve conter as oito representações do número, uma para cada base, separados por um
espaço em branco. As conversões devem ser apresentadas
"""


def convert(numDecimal, base):
    x = (numDecimal % base)
    if (numDecimal < base):
        return int(str(x))
    else:
        return int(str(convert(int(numDecimal / base), base)) + str(x))


decimal_numbers = []

x = int(input())
while (x != -1):
    decimal_numbers.append(x)
    x = int(input())

for number in decimal_numbers:
    converted_list = []
    for i in range(2, 10):
        converted_list.append(convert(number, i))
    print(' '.join(str(x) for x in converted_list))

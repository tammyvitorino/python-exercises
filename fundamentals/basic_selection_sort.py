"""
Selection Sort é um algoritmo de ordenação baseado em se passar sempre o menor valor do
vetor de posições para a primeira posição, depois o de segundo menor valor para a segunda
posição, e assim é feito sucessivamente com os ( ) elementos restantes, até os últimos
dois elementos.

Implemente um programa que recebe um vetor de números de ponto flutuante (float)
desordenado e o ordene utilizando Selection Sort (definido acima). Especificamente, seu
programa deverá:

a) O programa principal deve ativar um subprograma que solicita ao usuário, via entrada
padrão, o tamanho do vetor, gera o conteúdo desse vetor aleatoriamente e retorna o vetor
gerado. Sugestão: utilize a função random.random(), disponível na API, que retorna um
número entre 0.0 e 1.0.

b) Em seguida, o programa principal deve escrever na saída padrão o vetor gerado.

c) Após a escrita, o programa principal deve ativar um subprograma que recebe um vetor de
números de ponto flutuante e os ordene utilizando Selection Sort.

d) Por fim, o programa principal deve escrever na saída padrão o vetor ordenado.
"""
import random


def get_vector():
    array_size = int(input('Informe o tamanho do vetor:'))
    array = []
    for i in range(array_size):
        array.append(random.random())
    return array

def selection_sort(array):
    for i in range(len(array) - 1):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]

    return array


array = get_vector()

print('Vetor obtido:', array)
print('Vetor ordenado:', selection_sort(array))

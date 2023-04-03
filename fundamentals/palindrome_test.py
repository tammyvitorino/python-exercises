"""
Palíndromos são palavras, frases, números ou outras sequências de símbolos que se leem da
mesma maneira da direita para a esquerda ou da esquerda para a direita. Por exemplo, a frase:

“Socorram-me, subi no ônibus em Marrocos”

é um palíndromo, pois a leitura de trás para frente é:

“socorraM me subinô on ibus em-marrocoS”

Para isso, são desconsiderados os espaços em branco, pontuação, acentuação e caixa alta e
baixa dos caracteres.
Escreva um programa que contenha uma função recursiva que indique se o texto informado é ou
não é um palíndromo. Tal função deve receber pelo menos um parâmetro: o texto a ser analisado;
e retornar o valor lógico correspondente.
Entrada
A entrada é composta por várias linhas, cada uma contando um texto a ser analisado. A última
linha é composta apenas pela palavra “fim” e não deve ser processada.
É garantido que as frases não contenham pontuação nem caracteres especiais ou acentuados.
Contudo, o texto pode conter espaços em branco e caracteres alfanuméricos. Os caracteres
podem estar em caixa alta ou baixa, não havendo distinção entre eles.
Saída
Para cada frase lida, escreva “é palíndromo” ou “não é palíndromo”, conforme o caso.
"""

def get_text():
 return input().replace(" ","").lower()

text = get_text()

while text != 'fim':
  reverse_text = ''
  
  for i in range(0, len(text)):
    reverse_text = text[i] + reverse_text
  
  if reverse_text == text:
    print('é palindromo')
  else:
    print('nao é palíndromo')

  text = get_text()
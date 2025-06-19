import sympy as sp
import numpy as np

def Posicao_por_Letra(letra):

    alfabeto = "zabcdefghijklmnopqrstuvwxy"
    return(alfabeto.find(letra))

def Letra_Por_Posicao(numero):

    alfabeto = "zabcdefghijklmnopqrstuvwxy"

    return(alfabeto[numero])

A = np.array([[7, 3, 5], [2, 6, 3], [8, 9 ,5]])

print("Matriz Chave:\n{}".format(A))

def cifraHill(texto, matriz_chave):

    codigo = ""

    valorDecimal = np.empty([3, 1], dtype=int)

    valorCodificado = np.empty([3,1], dtype=int)

    cont = 0

    tresLetras = False

    for indice in range(0, len(texto)):

          tresLetras = False

          if(cont == 0):
              valorEncontrado = Posicao_por_Letra(texto[indice])
              valorDecimal[0][0] = valorEncontrado;

          if(cont == 1):
              valorEncontrado = Posicao_por_Letra(texto[indice])
              valorDecimal[1][0] = valorEncontrado

          if(cont == 2):
              valorEncontrado = Posicao_por_Letra(texto[indice])
              valorDecimal[2][0] = valorEncontrado

          if(cont == 2):

              valorCodificado = np.dot(matriz_chave, valorDecimal);


              if(valorCodificado[0][0] > 25):
                valorCodificado[0][0] = (valorCodificado[0][0] % 26)

              if(valorCodificado[1][0] > 25):
                valorCodificado[1][0] = (valorCodificado[1][0] % 26)

              if(valorCodificado[2][0] > 25):
                valorCodificado[2][0] = (valorCodificado[2][0] % 26)

              letra_codificada1 = str(Letra_Por_Posicao(valorCodificado[0][0]))
              letra_codificada2 = str(Letra_Por_Posicao(valorCodificado[1][0]))
              letra_codificada3 = str(Letra_Por_Posicao(valorCodificado[2][0]))

              codigo += letra_codificada1
              codigo += letra_codificada2
              codigo += letra_codificada3

              tresLetras = True
              cont = 0

          if tresLetras == False:
              cont += 1

    codigo = codigo[len(codigo) - len(texto): len(codigo)]

    return "Resultado: " + codigo

quantidade_novas_letras = 0

def inserirTexto():
  global quantidade_novas_letras
  texto = " "
  texto = str(input("Digite um texto para ser criptografado: "))
  texto = texto.replace(" ", "")
  texto = texto.lower()

  quantidade_novas_letras = 0
  while(len(texto) % 3 != 0):
    letra = chr(97 + quantidade_novas_letras)
    texto += letra
    quantidade_novas_letras += 1

  print("Seu texto é: {}".format(texto))
  return texto

#Esta função serve para remover os caracteres adicionados durante a criptografia.

def removerResto(texto):
  global quantidade_novas_letras
  texto_corrijido = " "

  if quantidade_novas_letras == 1:
      texto_corrijido = texto[:-1]

  if quantidade_novas_letras == 2:
      texto_corrijido = texto[:-2]

  return texto_corrijido

texto = inserirTexto()

// Texto Criptografado:
cifraHill(texto, A)

Descriptografia

determinante = (((A[0][0] * A[1][1] * A[2][2]) +
                 (A[0][1] * A[1][2] * A[2][0]) +
                 (A[0][2] * A[1][0] * A[2][1])) -
                ((A[0][2] * A[1][1] * A[2][0]) +
                 (A[0][1] * A[1][0] * A[2][2]) +
                 (A[0][0] * A[1][2] * A[2][1])))


residuo = determinante % 26
print("{}".format(residuo))

// a.a^{-1} = 1 (mod 26)
// residuo x receproco = 1(mod 26)
// logo, como o residuo é 17 o reciproco é 23

// logo, como o residuo é 17 o reciproco é 23**

// 17 x 23 = 391 = 1 (mod 26)

reciproco = 23

descriptografia = np.array([
    [
        (A[1][1] * A[2][2] - A[1][2] * A[2][1]),
        -(A[1][0] * A[2][2] - A[1][2] * A[2][0]),
        (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    ],
    [
        -(A[0][1] * A[2][2] - A[0][2] * A[2][1]),
        (A[0][0] * A[2][2] - A[0][2] * A[2][0]),
        -(A[0][0] * A[2][1] - A[0][1] * A[2][0])
    ],
    [
        (A[0][1] * A[1][2] - A[0][2] * A[1][1]),
        -(A[0][0] * A[1][2] - A[0][2] * A[1][0]),
        (A[0][0] * A[1][1] - A[0][1] * A[1][0])
    ]
])

descriptografia = np.transpose(descriptografia)

descriptografia *= reciproco
descriptografia %= 26

print("{}".format(descriptografia))

cifra = "uwzvubxcwaepojauwnnpi"

// Texto Descriptografado

removerResto(cifraHill(cifra,descriptografia))

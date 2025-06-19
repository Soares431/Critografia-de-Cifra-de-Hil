# Cifra de Hill com Python

Este projeto implementa a cifração e descriptografia baseada no método de **Cifra de Hill**. Ele utiliza álgebra linear para manipular matrizes e converter texto para uma forma criptografada.

## Características

* **Cifração**:

  * Transforma o texto original em blocos de 3 letras.
  * Cada bloco é multiplicado por uma matriz chave.
  * Os valores resultantes são ajustados com módulo $26$ para manter os resultados dentro do alfabeto.

* **Descriptografia**:

  * Calcula o inverso modular da matriz chave.
  * Reverte o processo de cifração para recuperar o texto original.

## Requisitos

* Python 3.7 ou superior
* Bibliotecas: `numpy`, `sympy`

## Estrutura do Código

### Funções Principais

#### `cifraHill(texto, matriz_chave)`

Realiza a cifração de um texto.

* **Entrada**: Um texto (string) e a matriz chave.
* **Saída**: Texto cifrado.
* **Processo**:

  * Divide o texto em blocos de 3 letras.
  * Converte cada letra em um valor numérico (posição no alfabeto).
  * Multiplica o vetor resultante pela matriz chave.
  * Aplica módulo $26$ nos valores resultantes.
  * Retorna o texto cifrado como string.

#### `removerResto(texto)`

Remove caracteres extras adicionados durante a cifração para ajustar o tamanho do texto.

* **Entrada**: Texto cifrado.
* **Saída**: Texto original sem os caracteres extras.

### Funções Auxiliares

#### `Posicao_por_Letra(letra)`

Retorna a posição de uma letra no alfabeto (baseado em uma string ajustada: "zabcdefghijklmnopqrstuvwxy").

* **Entrada**: Uma letra (string).
* **Saída**: Posição correspondente (inteiro).

#### `Letra_Por_Posicao(numero)`

Retorna a letra correspondente a uma posição no alfabeto ajustado.

* **Entrada**: Posição (inteiro).
* **Saída**: Letra (string).

### Partes Comentadas

#### Determinante e Recíproco Modular

* O determinante da matriz chave é calculado utilizando a fórmula:

  ```
  determinante = (((A[0][0] * A[1][1] * A[2][2]) +
                   (A[0][1] * A[1][2] * A[2][0]) +
                   (A[0][2] * A[1][0] * A[2][1])) -
                  ((A[0][2] * A[1][1] * A[2][0]) +
                   (A[0][1] * A[1][0] * A[2][2]) +
                   (A[0][0] * A[1][2] * A[2][1])))
  ```
* O resultado é ajustado com o módulo $26$:

  ```
  residuo = determinante % 26
  ```
* O recíproco modular é calculado para encontrar o inverso do determinante em relação a $26$:

  ```
  reciproco = 23  # pois 17 \times 23 \equiv 1 \pmod{26}
  ```

#### Construção da Matriz Inversa

* A matriz inversa é calculada usando os cofactores e ajustada com o recíproco modular:

  ```
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
  ```

* Essa matriz inversa é usada para decodificar o texto cifrado.

## Exemplo

**Entrada:**

```text
Texto original: "seguranca"
```

**Saída:**

```text
Texto criptografado: "uwzvubxcwa"
Texto descriptografado: "seguranca"
```

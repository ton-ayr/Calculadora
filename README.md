# Calculadora :abacus:

Este é um projeto de calculadora simples desenvolvida utilizando Python e a biblioteca `Tkinter` para criar uma interface gráfica. 
A calculadora suporta operações básicas (como soma, subtração, multiplicação, divisão) e funções matemáticas avançadas (como seno, cosseno, tangente, logaritmo, raiz quadrada e potência).

## Funcionalidades

- **Operações Básicas:**
  - Soma (`+`)
  - Subtração (`-`)
  - Multiplicação (`×`)
  - Divisão (`÷`)

- **Funções Avançadas:**
  - Raiz quadrada (`√`)
  - Potência (`x²`)
  - Seno (`sen()`)
  - Cosseno (`cos()`)
  - Tangente (`tg()`)
  - Logaritmo base 10 (`log10()`)
  - Pi (`pi()`)
  - Percentual (`%`)

- **Operações:**
  - Histórico das operações realizadas
  - Limpeza do display com a função `clear`
  - Exibição do resultado com o botão `=`

## Pré-requisitos

- Python 3.x
- Tkinter (geralmente incluído por padrão nas distribuições Python)

## Como Executar
   **Executar o Código:**
   - Salve o código em um arquivo Python (por exemplo, `calculadora.py`);
   - Execute o código no terminal ou ambiente de desenvolvimento de sua escolha.

## Explicação do Código

### Classe `Calculadora`

Esta classe define a lógica da calculadora e lida com as operações e o display. Ela contém os seguintes métodos:

- **Métodos de operação:**

  - `Soma`, `Subtracao`, `Multiplicacao`, `Divisao` realizam as operações matemáticas simples e atualiza o display;
  - Funções como `Raiz_Quadrada`, `Seno`, `Cosseno` e `tangente`, aplicam funções trigonométricas e atualizam o display.

- **Método de exibição:**

`atualizar_display`: Atualiza o display com o histórico e o valor atual de entrada.

- **Método de cálculo:**

  - `Igual`: Realiza o cálculo final de acordo com a operação selecionada e exibe o resultado.

### Classe `Botao`
Cria os botões da interface gráfica, associando cada um a uma função.

### Classe Célula
Esta classe armazena os números e os sinais das operações matemáticas. Ela possui métodos que realizam as operações básicas e retornam os resultados.

### Interface Gráfica

  - Utiliza o `Tkinter` para criar uma interface simples e funcional;
  - A tela é dividida em uma matriz de botões que permite ao usuário interagir com a calculadora.

### Melhorias Futuras

  - Melhorar front da interface gráfica;
  - Histórico de cálculo;
  - Reconhecer valores de entrada do teclado;
  - Criar executável.

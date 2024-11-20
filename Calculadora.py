from tkinter import *
import itertools
import math


class Calculadora():
    def __init__(self, raiz):
        self.input_ = "0"
        self.historico = ""  # Histórico das operações
        self.raiz = raiz
        self.display = Label(raiz, text=self.input_, font=("Comic Sans MS", "48", "bold"), anchor="e", bg="white")
        self.display.grid(row=1, column=1, columnspan=6, sticky=W + E + N + S)

        self.soma = Celula()

        def novo_botao(text, row, column, function):
            return Botao(raiz, text, row, column, function)

        def input_numero(numero):
            return lambda: self.Numero(numero)

        buttons = {}

        numbers_positions = list(itertools.product([3, 4, 5], [2, 3, 4]))
        for numero in range(1, 10):
            buttons.update({str(numero): (*numbers_positions[numero - 1], input_numero(numero))})

        buttons.update({"0": (5, 2, input_numero(0))})

        buttons.update({
            "pi()": (2, 1, self.Pi),
            "x²": (2, 2, self.Pow),
            "log10()": (2, 3, self.Log10),
            "%": (2, 4, self.Percentual),
            "raiz()": (2, 5, self.Raiz_Quadrada),
            "clear": (2, 6, self.clear_),
            "sen()": (3, 1, self.Seno),
            "cos()": (4, 1, self.Cosseno),
            "tg()": (5, 1, self.Tangente),
            "+": (3, 5, self.Soma),
            "-": (4, 5, self.Subtracao),
            "*": (5, 5, self.Multiplicacao),
            "/": (6, 5, self.Divisao),
            "=": (6, 6, self.Igual)
        })

        for button in buttons.keys():
            novo_botao(button, *buttons[button])

    def atualizar_display(self):
        """Atualiza o display com o histórico e o input atual."""
        self.display.config(text=f"{self.historico}{self.input_}")

    def clear_(self):
        """Limpa o histórico e o valor atual."""
        self.input_ = "0"
        self.historico = ""
        self.atualizar_display()

    def Raiz_Quadrada(self):
        temporario = math.sqrt(float(self.input_))
        self.input_ = str(temporario)
        self.historico += f"√({self.input_})"
        self.atualizar_display()

    def Seno(self):
        temporario = ((float(self.input_)) * 2 * math.pi) / 360
        self.input_ = str(math.sin(temporario))
        self.historico += f"sen({self.input_})"
        self.atualizar_display()

    def Cosseno(self):
        temporario = ((float(self.input_)) * 2 * math.pi) / 360
        self.input_ = str(math.cos(temporario))
        self.historico += f"cos({self.input_})"
        self.atualizar_display()

    def Tangente(self):
        temporario = ((float(self.input_)) * 2 * math.pi) / 360
        self.input_ = str(math.tan(temporario))
        self.historico += f"tan({self.input_})"
        self.atualizar_display()

    def Log10(self):
        try:
            temporario = math.log10(float(self.input_))
            self.input_ = str(temporario)
            self.historico += f"log({self.input_})"
        except ValueError:
            self.input_ = "Erro"
        self.atualizar_display()

    def Pi(self):
        self.input_ = str(math.pi)
        self.historico += f"{math.pi}"
        self.atualizar_display()

    def Pow(self):
        self.input_ = str(math.pow(float(self.input_), 2))
        self.historico += f"({self.input_})²"
        self.atualizar_display()

    def Percentual(self):
        self.input_ = str(float(self.input_) / 100)
        self.historico += f"({self.input_})%"
        self.atualizar_display()

    def Igual(self):
        """Calcula o resultado com base no histórico."""
        self.soma._numero_B = self.input_
        operacao = {
            "soma": self.soma.soma,
            "subtracao": self.soma.subtracao,
            "multiplicacao": self.soma.multiplicacao,
            "divisao": self.soma.divisao
        }
        v = operacao.get(self.soma._sinal, lambda: "Erro")()
        self.historico = ""  # Limpa o histórico ao exibir o resultado
        self.input_ = str(v)
        self.atualizar_display()

    def Soma(self):
        self.historico += f"{self.input_} + "
        self.soma._numero_A = self.input_
        self.soma._sinal = "soma"
        self.input_ = "0"
        self.atualizar_display()

    def Multiplicacao(self):
        self.historico += f"{self.input_} × "
        self.soma._numero_A = self.input_
        self.soma._sinal = "multiplicacao"
        self.input_ = "0"
        self.atualizar_display()

    def Divisao(self):
        self.historico += f"{self.input_} ÷ "
        self.soma._numero_A = self.input_
        self.soma._sinal = "divisao"
        self.input_ = "0"
        self.atualizar_display()

    def Subtracao(self):
        self.historico += f"{self.input_} - "
        self.soma._numero_A = self.input_
        self.soma._sinal = "subtracao"
        self.input_ = "0"
        self.atualizar_display()

    def Numero(self, numero):
        if self.input_ == "0":
            self.input_ = str(numero)
        else:
            self.input_ += str(numero)
        self.atualizar_display()


class Botao():
    def __init__(self, frame, text_botao, linha, coluna, comando):
        self.button = Button(frame, text=text_botao, fg="black", bg="grey", command=comando,
                             font=("Comic Sans MS", "20", "bold"))
        self.button["width"] = 5
        self.button["height"] = 1
        self.button.grid(row=linha, column=coluna)


class Celula():
    def __init__(self):
        self._numero_A = None
        self._numero_B = None
        self._sinal = None

    def soma(self):
        return float(self._numero_A) + float(self._numero_B)

    def subtracao(self):
        return float(self._numero_A) - float(self._numero_B)

    def multiplicacao(self):
        return float(self._numero_A) * float(self._numero_B)

    def divisao(self):
        try:
            return float(self._numero_A) / float(self._numero_B)
        except ZeroDivisionError:
            return "Erro"


raiz = Tk()
raiz.title("Calculadora")
raiz.geometry("570x452")
m = Calculadora(raiz)
raiz.mainloop()

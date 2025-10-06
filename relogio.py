from tkinter import *
from time import strftime

# função para atualizar o relógio
def atualizar_relogio():
    horario_atual = strftime("%H:%M:%S %p")
    rotulo_relogio.config(text=horario_atual)
    rotulo_relogio.after(1000, atualizar_relogio)

# criação da janela principal
janela = Tk()
janela.title('Relógio Digital Teles Draws')

#criação do rótulo para exibir o relógio
rotulo_relogio = Label(
    janela,
    font=("Ariel", 40, "bold"),
    background="black",
    foreground="orange"
)

# posiciona o rótulo no centro da janela
rotulo_relogio.pack(anchor="center")

# inicia a atualização do relógio
atualizar_relogio()

# inicia o loop principal da interface gráfica
janela.mainloop()

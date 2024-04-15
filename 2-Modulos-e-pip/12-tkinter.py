import tkinter as tk

# 1 - Criando a janela
window = tk.Tk()
window.geometry("300x150")
window.title("Gerenciador de Frases")

# 2 - Adicionando o Frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 - Adicionando o label
label = tk.Label(frame, text="Hello, World")
label.pack(fill='x', expand=True)

# 4 Adicionando o input text
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 - Funçao para alterar o texto da Label
def click():
    label.config(text=frase_inp.get())#.get para pegar o conteudo de frase_inp

# 6 - Adicionando botao
button = tk.Button(frame, text='Enviar', command=click) # comand=click - quando clicar em enviar ira chamar a funçao click, pegando o text da label e alterando com base no valor que foi digitado
button.pack()

window.mainloop()

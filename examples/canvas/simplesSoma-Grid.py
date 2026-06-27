from tkinter import *
#from tkinter import ttk

def calcular():
    try:
        # Captura os valores digitados nos campos de texto
        n1 = float(txt_num1.get())
        n2 = float(txt_num2.get())
        soma = n1 + n2
        
        # Formata o resultado para exibir sem .0 se for inteiro
        if soma.is_integer():
            lbl_resultado.config(text=f"{int(soma)}", fg="blue")
        else:
            lbl_resultado.config(text=f"{soma}", fg="blue")
            
    except ValueError:
        # Tratamento de erro caso o input não seja numérico
        lbl_resultado.config(text="Erro: Digite apenas números!", fg="red")


# 1. Configuração da janela principal
janela = Tk()
janela.title("Calculadora de Soma")
janela.geometry("300x180")

# 2. Frame para conter widgets arranjados com layout grid
frame = Frame(janela)
frame.pack(pady=30)

# 3. Botão de ação (Linha 3)
btn_calcular = Button(janela, text="Calcular Soma", command=calcular)
btn_calcular.pack()

# 4. Criação e posicionamento dos 3 pares de widgets usando o Grid

# Par 1: Primeiro Número (Linha 0)
lbl_num1 = Label(frame, text="Primeiro Número:")
lbl_num1.grid(row=0, column=0)
txt_num1 = Entry(frame)
txt_num1.grid(row=0, column=1)

# Par 2: Segundo Número (Linha 1)
lbl_num2 = Label(frame, text="Segundo Número:")
lbl_num2.grid(row=1, column=0)
txt_num2 = Entry(frame)
txt_num2.grid(row=1, column=1)

# Par 3: Resultado da Soma (Linha 2)
lbl_res = Label(frame, text="Resultado:")
lbl_res.grid(row=2, column=0)
lbl_resultado = Label(frame, text="0", font=("Arial", 10, "bold"))
lbl_resultado.grid(row=2, column=1)

# Executa o loop principal da interface gráfica
janela.mainloop()

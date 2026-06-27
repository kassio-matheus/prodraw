import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Exemplo de Desenho com Canvas")

# Cria o componente Canvas (largura: 400px, altura: 300px)
canvas = tk.Canvas(janela, width=400, height=300, bg="white")
canvas.pack(padx=10, pady=10)

# 1. Desenha uma linha (x1, y1, x2, y2)
canvas.create_line(20, 20, 380, 50, fill="black", width=2)

# 2. Desenha um retângulo (x1, y1, x2, y2)
canvas.create_rectangle(50, 60, 150, 160, fill="lightblue", outline="blue", width=3)

# 3. Desenha um círculo/oval dentro de um limite (x1, y1, x2, y2)
canvas.create_oval(230, 60, 330, 160, fill="lightgreen", outline="green", width=3)

# 4. Desenha um polígono/triângulo passando os pontos (x1, y1, x2, y2, x3, y3)
canvas.create_polygon(200, 200, 100, 280, 300, 280, fill="coral", outline="darkred")

# 5. Adiciona um texto no Canvas (x, y)
canvas.create_text(200, 130, text="Tkinter Canvas", font=("Arial", 14, "bold"), fill="purple")

# Executa o loop principal da aplicação
janela.mainloop()

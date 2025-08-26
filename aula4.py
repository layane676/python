import tkinter as tk
from tkinter import messagebox

def verificar_nota():
    nota_texto = entry_nota.get()
    try:
        nota = float(nota_texto)
        if nota == 10:
            resultado = "Parabéns nota máxima!!"
        elif 9 <= nota < 10:
            resultado = "Quase perfeito!!"
        elif 7 <= nota < 9:
            resultado = "Aprovado!!"
        elif 4.5 <= nota < 7:
            resultado = "Recuperação!!"
        elif 0 <= nota < 4.5:
            resultado = "Reprovado!!"
        else:
            resultado = "Nota inválida!"
        messagebox.showinfo("Resultado", f"Situação: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido.")

# Interface gráfica
root = tk.Tk()
root.title("Verificador de Nota")
root.configure(bg="#E0D5E4")  # Cor de fundo

label = tk.Label(root, text="Digite a nota:", font=("Arial", 14), fg="#680F91", bg="#ccaeda")
label.pack()

entry_nota = tk.Entry(root, font=("Arial", 12), width=10)
entry_nota.pack()

btn_verificar = tk.Button(root, text="Verificar", command=verificar_nota, bg="#4c0861", fg="white", font=("Arial", 12))
btn_verificar.pack(pady=10)

root.mainloop()

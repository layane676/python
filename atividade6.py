
# for i in range(8, 15, 2):
#     print(i)

# for letra in "Python":
#     print("letra",letra)

# alunos=["João", "Maria", "Pedro"]
# print(len(alunos))


# usuarios=["admin","usuario", "convidado" , "funcionario"]
# print("Tem ",len(usuarios) ," usuários cadastrados.")
# for i in range(len(usuarios)):
#     print("Usuário", i+1, ":", usuarios[i])

# for i in range(1001, 1005):
#     print("ID do usuário", i)

# senha="654321"
# for i in range(len(senha)):
#     print("Caractere", i+1, ":", senha[i])


# senha=(input("Digite a senha: "))

# if len(senha) == 8:
#     print("Senha válida")
# else:
#     print("Senha inválida, necessita ter 8 caracteres.")

# correta="abc@123"
# senha=(input("Digite a senha: "))

# if len(senha) == 8:
#     if senha==correta:
#         print("Bem-vindo!!")
#     else:
#         print("Senha incorreta.")

# else:
#     print("Senha inválida, necessita ter 8 caracteres.")

# import tkinter as tk
# from tkinter import messagebox

# def senha_correta():
#     correta="abc@123"
#     senha=(input("Digite a senha: "))
    
#     if len(senha) == 8:
#         if senha==correta:
#             print("Bem-vindo!!")
#         else: 
#             print("Senha incorreta.")
#     else:
#         print("Senha inválida, necessita ter 8 caracteres.")

# root = tk.Tk()
# root.title("Verificador de Senha")
# root.configure(bg="#baf3ba")  # Cor de fundo

import tkinter as tk
from tkinter import messagebox

def senha_correta():
    correta = "abcd@123"
    senha = entry_senha.get()
    
    if len(senha) == 8:
        if senha == correta:
            messagebox.showinfo("Resultado", "Bem-vindo!!")
        else: 
            messagebox.showerror("Resultado", "Senha incorreta.")
    else:
        messagebox.showerror("Resultado", "Senha inválida, necessita ter 8 caracteres.")

root = tk.Tk()
root.title("Verificador de Senha")
root.configure(bg="#baf3ba")  # Cor de fundo

label = tk.Label(root, text="Digite a senha:", font=("Arial", 14), bg="#baf3ba")
label.pack()

entry_senha = tk.Entry(root, font=("Arial", 12), show="*")
entry_senha.pack()

btn_verificar = tk.Button(root, text="Verificar", command=senha_correta, font=("Arial", 12), bg="#2e7d32", fg="white")
btn_verificar.pack(pady=10)

root.mainloop()
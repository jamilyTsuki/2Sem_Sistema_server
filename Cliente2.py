import socket
import tkinter as tk
from tkinter import messagebox


def conectar_ao_servidor():
    mensagem = campo_texto.get().strip()
    if not mensagem:
        messagebox.showwarning("Mensagem vazia", "Digite uma mensagem antes de enviar.")
        return

    try:
        with socket.create_connection(("127.0.0.1", 5000), timeout=5) as cliente:
            nome_remetente = nome.get().strip() or "Visitante"
            cliente.sendall(f"{nome_remetente}: {mensagem}\n".encode("utf-8"))
        campo_texto.delete(0, tk.END)
        messagebox.showinfo("Enviado", "Sua mensagem foi enviada ao servidor.")
    except OSError as erro:
        messagebox.showerror("Erro", f"Não foi possível conectar ao servidor: {erro}")


janela = tk.Tk()
janela.title("Cliente de mensagens")
janela.geometry("360x250")
janela.resizable(False, False)

tk.Label(janela, text="Enviar mensagem ao servidor", font=("Arial", 12, "bold")).pack(pady=(18, 10))
tk.Label(janela, text="Seu nome").pack()
nome = tk.Entry(janela, width=32, font=("Arial", 11))
nome.insert(0, "Visitante")
nome.pack(pady=(3, 8))

tk.Label(janela, text="Mensagem").pack()
campo_texto = tk.Entry(janela, width=32, font=("Arial", 11))
campo_texto.pack(pady=(3, 8))
campo_texto.bind("<Return>", lambda evento: conectar_ao_servidor())

botao = tk.Button(
    janela,
    text="Conectar e enviar",
    command=conectar_ao_servidor,
    bg="#16803c",
    fg="white",
    font=("Arial", 11, "bold"),
)
botao.pack(pady=12)

janela.mainloop()

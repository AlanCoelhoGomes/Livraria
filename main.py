import tkinter as tk
from tkinter import messagebox

class GerenciadorBiblioteca:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gerenciamento de Biblioteca")
        self.master.geometry("400x400")
        self.master.config(bg='#708090')

        self.livros = []
        self.lista_emprestimos = []

        # Rótulos
        self.login_label = tk.Label(self.master, text="Sistema de Gerenciamento de Biblioteca", font=("Helvetica", 16), bg='#708090', fg='white')
        self.login_label.pack()
        self.username_label = tk.Label(self.master, text="Nome de usuário", font=("Helvetica", 12), bg='#708090', fg='white')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.username_entry.pack()
        self.password_label = tk.Label(self.master, text="Senha", font=("Helvetica", 12), bg='#708090', fg='white')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, font=("Helvetica", 12), show="*")
        self.password_entry.pack()

        # Login
        self.login_button = tk.Button(self.master, text="Entrar", command=self.login, font=("Helvetica", 12))
        self.login_button.pack()

        # Registrar
        self.register_button = tk.Button(self.master, text="Registrar", command=self.registrar, font=("Helvetica", 12))
        self.register_button.pack()

        self.username = ""
        self.password = ""
        self.bibliotecarios = []

    def login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        for bibliotecario in self.bibliotecarios:
            if self.username == bibliotecario[0] and self.password == bibliotecario[1]:
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.login_label.destroy()
                self.username_label.destroy()
                self.username_entry.destroy()
                self.password_label.destroy()
                self.password_entry.destroy()
                self.login_button.destroy()
                self.register_button.destroy()
                self.tela_gerenciamento_biblioteca()
                return
        messagebox.showerror("Erro", "Nome de usuário ou senha inválido")

    def registrar(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.bibliotecarios.append([self.username, self.password])
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def tela_gerenciamento_biblioteca(self):
        self.add_book_label = tk.Label(self.master, text="Adicionar Livro", font=("Helvetica", 16), bg='#708090', fg='white')
        self.add_book_label.pack()
        self.add_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.add_book_entry.pack()
        self.add_book_button = tk.Button(self.master, text="Adicionar Livro", command=self.adicionar_livro, font=("Helvetica", 12))
        self.add_book_button.pack()
        self.remove_book_label = tk.Label(self.master, text="Remover Livro", font=("Helvetica", 16), bg='#708090', fg='white')
        self.remove_book_label.pack()
        self.remove_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.remove_book_entry.pack()
        self.remove_book_button = tk.Button(self.master, text="Remover Livro", command=self.remover_livro, font=("Helvetica", 12))
        self.remove_book_button.pack()
        self.issue_book_label = tk.Label(self.master, text="Emprestar Livro", font=("Helvetica", 16), bg='#708090', fg='white')
        self.issue_book_label.pack()
        self.issue_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.issue_book_entry.pack()
        self.issue_book_button = tk.Button(self.master, text="Emprestar Livro", command=self.emprestar_livro, font=("Helvetica", 12))
        self.issue_book_button.pack()
        self.view_books_button = tk.Button(self.master, text="Ver Livros", command=self.ver_livros, font=("Helvetica", 12))
        self.view_books_button.pack()

    def adicionar_livro(self):
        livro = self.add_book_entry.get()
        self.livros.append(livro)
        messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!")
        self.add_book_entry.delete(0, tk.END)

    def remover_livro(self):
        livro = self.remove_book_entry.get()
        if livro in self.livros:
            self.livros.remove(livro)
            messagebox.showinfo("Sucesso", "Livro removido com sucesso!")
        else:
            messagebox.showerror("Erro", "Livro não encontrado")
        self.remove_book_entry.delete(0, tk.END)

    def emprestar_livro(self):
        livro = self.issue_book_entry.get()
        if livro in self.livros:
            self.lista_emprestimos.append(livro)
            self.livros.remove(livro)
            messagebox.showinfo("Sucesso", "Livro emprestado com sucesso")
        else:
            messagebox.showerror("Erro", "Livro não encontrado")
        self.issue_book_entry.delete(0, tk.END)

    def ver_livros(self):
        mensagem = "\n".join(self.livros)
        messagebox.showinfo("Livros", mensagem)

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorBiblioteca(root)
    root.mainloop()

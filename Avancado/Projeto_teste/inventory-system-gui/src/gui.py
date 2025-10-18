import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os
import sys

# We'll import the product list and functions
from controle_vendas import produtos, cadastrar_produto, listar_produtos, vender_produto

class InventoryGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Controle de Estoque")
        self.master.geometry("600x400")
        self.master.resizable(False, False)
        
        # Load image (assuming generic.png exists)
        try:
            # Handle path whether run from src directory or project root
            if getattr(sys, 'frozen', False):
                # Running as executable
                base_path = sys._MEIPASS
            else:
                # Running as script
                base_path = os.path.dirname(os.path.abspath(__file__))
                
            image_path = os.path.join(os.path.dirname(base_path), "assets", "generic.png")
            self.img = ImageTk.PhotoImage(Image.open(image_path).resize((100, 100)))
        except Exception as e:
            print(f"Could not load image: {e}")
            self.img = None

        # Create a container for all frames
        self.container = tk.Frame(master)
        self.container.pack(fill="both", expand=True)
        
        # Create all frames
        self.frames = {}
        
        for F in (HomeFrame, CadastrarFrame, VenderFrame, ListarFrame):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Configure grid
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Start with home frame
        self.show_frame(HomeFrame)
    
    def show_frame(self, frame_class):
        """Raise the selected frame to the top"""
        frame = self.frames[frame_class]
        frame.tkraise()


class HomeFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Title and welcome message
        title_label = tk.Label(self, text="Sistema de Controle de Estoque", font=("Arial", 18, "bold"))
        title_label.pack(pady=20)
        
        welcome_label = tk.Label(self, text="Bem-vindo ao sistema! Selecione uma opção:", font=("Arial", 12))
        welcome_label.pack(pady=10)
        
        # Display image if available
        if controller.img:
            img_label = tk.Label(self, image=controller.img)
            img_label.pack(pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)
        
        # Buttons
        cadastrar_btn = tk.Button(button_frame, text="Cadastrar Produto", 
                                  command=lambda: controller.show_frame(CadastrarFrame),
                                  width=20, height=2, bg="#4CAF50", fg="white", font=("Arial", 11))
        cadastrar_btn.grid(row=0, column=0, padx=10, pady=10)
        
        vender_btn = tk.Button(button_frame, text="Vender Produto", 
                              command=lambda: controller.show_frame(VenderFrame),
                              width=20, height=2, bg="#2196F3", fg="white", font=("Arial", 11))
        vender_btn.grid(row=0, column=1, padx=10, pady=10)
        
        listar_btn = tk.Button(button_frame, text="Listar Produtos", 
                              command=lambda: self.update_and_show_listar(),
                              width=20, height=2, bg="#FF9800", fg="white", font=("Arial", 11))
        listar_btn.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        quit_btn = tk.Button(self, text="Sair", command=self.master.quit,
                           width=10, height=1, bg="#F44336", fg="white")
        quit_btn.pack(side="bottom", pady=20)
    
    def update_and_show_listar(self):
        # Update product list before showing
        self.controller.frames[ListarFrame].update_product_list()
        self.controller.show_frame(ListarFrame)


class CadastrarFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Title
        title_label = tk.Label(self, text="Cadastrar Produto", font=("Arial", 16, "bold"))
        title_label.pack(pady=20)
        
        # Form frame
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)
        
        # Labels and entries
        tk.Label(form_frame, text="Nome:", font=("Arial", 12)).grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.nome_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(form_frame, text="Preço:", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.preco_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.preco_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(form_frame, text="Quantidade:", font=("Arial", 12)).grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.quantidade_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.quantidade_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)
        
        cadastrar_btn = tk.Button(button_frame, text="Cadastrar", 
                                  command=self.cadastrar,
                                  width=15, height=2, bg="#4CAF50", fg="white")
        cadastrar_btn.grid(row=0, column=0, padx=10)
        
        voltar_btn = tk.Button(button_frame, text="Voltar", 
                               command=lambda: controller.show_frame(HomeFrame),
                               width=15, height=2, bg="#F44336", fg="white")
        voltar_btn.grid(row=0, column=1, padx=10)
    
    def cadastrar(self):
        try:
            nome = self.nome_entry.get()
            preco = float(self.preco_entry.get())
            quantidade = int(self.quantidade_entry.get())
            
            if nome and preco >= 0 and quantidade >= 0:
                # Create product dictionary and add to list
                produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
                produtos.append(produto)
                
                messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
                
                # Clear entries
                self.nome_entry.delete(0, tk.END)
                self.preco_entry.delete(0, tk.END)
                self.quantidade_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
        except ValueError:
            messagebox.showerror("Erro", "Preço e quantidade devem ser números.")


class VenderFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Title
        title_label = tk.Label(self, text="Vender Produto", font=("Arial", 16, "bold"))
        title_label.pack(pady=20)
        
        # Form frame
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)
        
        # Labels and entries
        tk.Label(form_frame, text="Nome do produto:", font=("Arial", 12)).grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.nome_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(form_frame, text="Quantidade:", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.quantidade_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.quantidade_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)
        
        vender_btn = tk.Button(button_frame, text="Vender", 
                              command=self.vender,
                              width=15, height=2, bg="#2196F3", fg="white")
        vender_btn.grid(row=0, column=0, padx=10)
        
        voltar_btn = tk.Button(button_frame, text="Voltar", 
                              command=lambda: controller.show_frame(HomeFrame),
                              width=15, height=2, bg="#F44336", fg="white")
        voltar_btn.grid(row=0, column=1, padx=10)
    
    def vender(self):
        nome = self.nome_entry.get()
        try:
            quantidade = int(self.quantidade_entry.get())
            
            if not nome or quantidade <= 0:
                messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
                return
            
            # Find product and update stock
            for p in produtos:
                if p["nome"].lower() == nome.lower():
                    if p["quantidade"] >= quantidade:
                        p["quantidade"] -= quantidade
                        messagebox.showinfo("Sucesso", "Venda realizada com sucesso!")
                        
                        # Clear entries
                        self.nome_entry.delete(0, tk.END)
                        self.quantidade_entry.delete(0, tk.END)
                    else:
                        messagebox.showerror("Erro", "Estoque insuficiente!")
                    return
            
            messagebox.showerror("Erro", "Produto não encontrado!")
            
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número inteiro.")


class ListarFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Title
        title_label = tk.Label(self, text="Lista de Produtos", font=("Arial", 16, "bold"))
        title_label.pack(pady=20)
        
        # Frame for listbox and scrollbar
        list_frame = tk.Frame(self)
        list_frame.pack(pady=10, fill="both", expand=True, padx=20)
        
        # Create scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")
        
        # Create listbox
        self.products_listbox = tk.Listbox(list_frame, font=("Arial", 12), width=50, height=10,
                                        yscrollcommand=scrollbar.set)
        self.products_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.products_listbox.yview)
        
        # Back button
        voltar_btn = tk.Button(self, text="Voltar", 
                              command=lambda: controller.show_frame(HomeFrame),
                              width=15, height=2, bg="#F44336", fg="white")
        voltar_btn.pack(pady=20)
    
    def update_product_list(self):
        """Update the listbox with current products"""
        self.products_listbox.delete(0, tk.END)
        
        if len(produtos) == 0:
            self.products_listbox.insert(tk.END, "Não há produtos cadastrados.")
        else:
            for p in produtos:
                self.products_listbox.insert(
                    tk.END, 
                    f"{p['nome']} - R${p['preco']:.2f} - Estoque: {p['quantidade']}"
                )
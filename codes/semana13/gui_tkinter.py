"""
Semana 13: Interface Gráfica com Tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox

class JogadorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema RPG")
        self.root.geometry("400x500")
        
        # Dados do jogador
        self.nome = "Aragorn"
        self.nivel = 5
        self.hp = 100
        self.hp_max = 150
        self.exp = 250
        
        self.criar_interface()
    
    def criar_interface(self):
        # Frame de Status
        frame_status = ttk.LabelFrame(self.root, text="Status do Jogador", padding=10)
        frame_status.pack(fill="x", padx=10, pady=10)
        
        ttk.Label(frame_status, text=f"Nome: {self.nome}").pack(anchor="w")
        ttk.Label(frame_status, text=f"Nível: {self.nivel}").pack(anchor="w")
        
        self.label_hp = ttk.Label(frame_status, text=f"HP: {self.hp}/{self.hp_max}")
        self.label_hp.pack(anchor="w")
        
        # Barra de HP
        self.progress_hp = ttk.Progressbar(
            frame_status, length=300, mode='determinate',
            maximum=self.hp_max, value=self.hp
        )
        self.progress_hp.pack(pady=5)
        
        # Inventário
        frame_inv = ttk.LabelFrame(self.root, text="Inventário", padding=10)
        frame_inv.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.lista_itens = tk.Listbox(frame_inv, height=8)
        self.lista_itens.pack(fill="both", expand=True)
        self.lista_itens.insert("end", "Espada Longa")
        self.lista_itens.insert("end", "Escudo de Ferro")
        self.lista_itens.insert("end", "Poção de Vida x3")
        
        # Botões de Ação
        frame_acoes = ttk.Frame(self.root)
        frame_acoes.pack(fill="x", padx=10, pady=10)
        
        ttk.Button(frame_acoes, text="⚔️ Atacar", 
                  command=self.atacar).pack(side="left", padx=5)
        ttk.Button(frame_acoes, text="❤️ Usar Poção", 
                  command=self.usar_pocao).pack(side="left", padx=5)
        ttk.Button(frame_acoes, text="📊 Status", 
                  command=self.mostrar_status).pack(side="left", padx=5)
    
    def atacar(self):
        dano = 20
        self.hp -= dano
        self.atualizar_hp()
        messagebox.showinfo("Combate", f"Você recebeu {dano} de dano!")
    
    def usar_pocao(self):
        cura = 30
        self.hp = min(self.hp + cura, self.hp_max)
        self.atualizar_hp()
        messagebox.showinfo("Cura", f"Você recuperou {cura} HP!")
    
    def atualizar_hp(self):
        self.label_hp.config(text=f"HP: {self.hp}/{self.hp_max}")
        self.progress_hp['value'] = self.hp
    
    def mostrar_status(self):
        status = f"Nome: {self.nome}\nNível: {self.nivel}\n"
        status += f"HP: {self.hp}/{self.hp_max}\nEXP: {self.exp}"
        messagebox.showinfo("Status Completo", status)

if __name__ == "__main__":
    root = tk.Tk()
    app = JogadorGUI(root)
    root.mainloop()

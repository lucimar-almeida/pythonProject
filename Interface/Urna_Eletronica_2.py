from time import sleep
from tkinter import CENTER
import customtkinter as ctk


# Configurações de interface
ctk.set_appearance_mode("System")  # Modos: "System" (padrão), "Dark", "Light"q
app = ctk.CTk()
app.title('Urna Eletronica')
app.geometry('1000x800')

# criação de funções e funcionalidades
def validar_login():
    cpf = campo_cpf.get()
    titulo = campo_titulo.get()
    # Aqui você pode adicionar a lógica de validação do CPF e Título de Eleitor
    if cpf == "1" and titulo == "1":
        resultado_login.configure(text='Login bem-sucedido!', text_color="green")
        #sleep(1)
        tela_votacao(app)
    else:
        resultado_login.configure(text="CPF ou Título de Eleitor inválido.", text_color="red")
        
        
def voto_prefeito(app, campo_prefeito, resultado_voto):
    voto = campo_prefeito.get()
    # Aqui você pode adicionar a lógica de validação do voto
    if voto == "10":
        resultado_voto.configure(text="Voto computado para Ademir da Guia", text_color="green")
    elif voto == "20":
        resultado_voto.configure(text="Voto computado para João Gois", text_color="green")
    else:
        resultado_voto.configure(text="Voto inválido", text_color="red")


def voto_vereador(app, campo_vereador, resultado_voto):
    voto = campo_vereador.get()
    # Aqui você pode adicionar a lógica de validação do voto
    if voto == "100":
        resultado_voto.configure(text="Voto computado para Maria Silva", text_color="green")
    elif voto == "200":
        resultado_voto.configure(text="Voto computado para Carlos Souza", text_color="green")
    else:
        resultado_voto.configure(text="Voto inválido", text_color="red")


# Criação dos campos

# Tela de login
# label
label_cpf = ctk.CTkLabel(app,text='CPF:')
label_cpf.pack(pady=10)
# entry
campo_cpf = ctk.CTkEntry(app,placeholder_text='Digite seu CPF', width=200, height=25, border_width=2, corner_radius=10, justify=CENTER)
campo_cpf.pack(pady=10)
# label
label_titulo = ctk.CTkLabel(app,text='Título de Eleitor:')
label_titulo.pack(padx=20, pady=10)
# entry
campo_titulo = ctk.CTkEntry(app,placeholder_text='Digite seu título de eleitor', width=200, height=25, border_width=2, corner_radius=10, justify=CENTER)
campo_titulo.pack(pady=10)
# button
button = ctk.CTkButton(app,text='Entrar',command=validar_login)
button.pack(pady=20)
# feedback de login
resultado_login=ctk.CTkLabel(app,text ='')
resultado_login.pack(pady=10)

# Tela de votação
def tela_votacao(app): 
    # Limpar a tela atual
    for widget in app.winfo_children():
        widget.destroy()
    # Chamar a função da tela de votação
    app.title('Urna Eletronica - Votação')
    # label
    label_prefeito = ctk.CTkLabel(app,text='voto para prefeito:')
    label_prefeito.pack(pady=10)
    # entry
    campo_prefeito = ctk.CTkEntry(app,placeholder_text='N° do candidato', width=200, height=25, border_width=2, corner_radius=10, justify=CENTER)
    campo_prefeito.pack(pady=10)
    # button
    button_voto = ctk.CTkButton(app,text='Votar',command=lambda: voto_prefeito(app, campo_prefeito, resultado_voto))
    button_voto.pack(pady=20)
    # feedback de login
    resultado_voto=ctk.CTkLabel(app,text ='')
    resultado_voto.pack(pady=10)
    
    sleep(1)
    
     # Limpar a tela atual
    for widget in app.winfo_children():
        widget.destroy()
    # Chamar a função da tela de votação
    app.title('Urna Eletronica - Votação')
    # label
    label_vereador = ctk.CTkLabel(app,text='voto para vereador:')
    label_vereador.pack(pady=10)
    # entry
    campo_vereador = ctk.CTkEntry(app,placeholder_text='N° do candidato', width=200, height=25, border_width=2, corner_radius=10, justify=CENTER)
    campo_vereador.pack(pady=10)
    # button
    button_voto = ctk.CTkButton(app,text='Votar',command=lambda: voto_vereador(app, campo_vereador, resultado_voto))
    button_voto.pack(pady=20)
    # feedback de login
    resultado_voto=ctk.CTkLabel(app,text ='')
    resultado_voto.pack(pady=10)

# Iniciar aplicação
app.mainloop()
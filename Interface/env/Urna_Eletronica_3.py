from tkinter import CENTER
import customtkinter as ctk
import Urna_Eletronica_2 as urna2


# Configurações de interface
ctk.set_appearance_mode("System")  # Modos: "System" (padrão), "Dark", "Light"q
app = ctk.CTk()
app.title('Urna Eletronica')
app.geometry('1000x800')

# criação de funções e funcionalidades
def validar_login():
    cpf = urna2.campo_cpf.get()
    titulo = urna2.campo_titulo.get()
    # Aqui você pode adicionar a lógica de validação do CPF e Título de Eleitor
    if cpf == "012345678910" and titulo == "12345678910":
        urna2.resultado_login.configure(text='Login bem-sucedido!', text_color="green")
    else:
        urna2.resultado_login.configure(text="CPF ou Título de Eleitor inválido.", text_color="red")
        
        
        
        
        
        

# Iniciar aplicação
app.mainloop()
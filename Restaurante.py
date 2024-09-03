from PIL import Image
import customtkinter
from tkinter import messagebox

janelao = customtkinter.CTk()
janelao.configure(bg='#2E2E2E')
janelao.title("Restaurante do Ederson")
janelao.geometry("900x900")
janelao.maxsize(900,900)
janelao.minsize(900,900)
customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")

#------------------------------------------------------------------------------------------------
#Frame Tela Login 
tela_login = customtkinter.CTkFrame(janelao)
tela_login.pack(fill="both", expand = True)

#------------------------------------------------------------------------------------------------

#FUNÇÕES
#def pra gerar um quadrado com cor
def quadro(master, width, height, cor, posx, posy):
    customtkinter.CTkFrame(
        master=master,
        width=width,
        height=height,
        fg_color=cor
        ).place(relx= posx, rely=posy, anchor="center")
 
#def pra gerar um texto 
def texto(master,texto, cor_do_texto, fonte, tamanho, cor, posx, posy):
    customtkinter.CTkLabel(
        master=master,
        text = texto,
        text_color = cor_do_texto,
        font = (fonte, tamanho, "bold"),
        bg_color= cor
        ).place(relx= posx, rely=posy, anchor="center")
    
#def pra janela de aviso personalizada    
def janela_aviso_bom(titulo, texto):
    aviso = customtkinter.CTk()
    aviso.title(titulo)
    aviso.geometry("300x150")
    aviso.eval('tk::PlaceWindow . right')
    aviso.resizable(False, False)
    aviso.configure(bg_color="#272e36")

    aviso_label = customtkinter.CTkLabel(aviso, text=texto, wraplength=250, text_color="white")
    aviso_label.place(relx=0.5, rely=0.3, anchor='center')

    def fechar_janela_aviso():
        aviso.destroy()
        tela_login.pack_forget()
        tela_menu.pack(fill="both", expand = True)

    botao_ok = customtkinter.CTkButton(aviso, text="OK", fg_color="#424f5c", hover_color="#0a6638", command=fechar_janela_aviso)
    botao_ok.place(relx=0.5, rely=0.7, anchor='center')

    aviso.mainloop()

def janela_aviso_ruim(titulo, texto):
    aviso = customtkinter.CTk()
    aviso.title(titulo)
    aviso.geometry("300x150")
    aviso.eval('tk::PlaceWindow . right')
    aviso.resizable(False, False)
    aviso.configure(bg_color="#272e36")

    aviso_label = customtkinter.CTkLabel(aviso, text=texto, wraplength=250, text_color="white")
    aviso_label.place(relx=0.5, rely=0.3, anchor='center')

    def fechar_janela_aviso():
        aviso.destroy()
        tela_login.pack(fill="both", expand = True)

    botao_ok = customtkinter.CTkButton(aviso, text="OK", fg_color="#424f5c", hover_color="#0a6638", command=fechar_janela_aviso)
    botao_ok.place(relx=0.5, rely=0.7, anchor='center')

    aviso.mainloop()
    
#def função botão "Entrar"
def funcao_botao():
    login = entrada_login.get()
    senha = entrada_senha.get()
    senha_de_novo = entrada_confirmar_senha.get()

    if login == "" or senha == "" or senha_de_novo == "":
        janela_aviso_ruim("Aviso", "Campo não preenchido, confira os campos de cadastro e tente novamente.")
    elif login == senha:
        janela_aviso_ruim("Aviso","O login e a senha não podem ser iguais.")
    elif senha != senha_de_novo:
        janela_aviso_ruim("Aviso","Senhas não coincidem.")
    else:
        janela_aviso_bom("Aviso","Sucesso! Clique em 'OK' para visualizar o menu.")
       
#------------------------------------------------------------------------------------------------

#Layout Tela Login 
quadro(tela_login, 800, 720, "#272e36", 0.5,0.5)

foto1 = customtkinter.CTkImage(
    light_image=Image.open("food.jpeg"),
    size=(801,209)
)
foto1_label = customtkinter.CTkLabel(tela_login, image=foto1, text="")
foto1_label.place(relx=0.5, rely=0.79, anchor='center')

texto(tela_login, "Éderson Restaurant", "white", ("Courier New"), 35, "#272e36", 0.5, 0.2)
texto(tela_login, "Olá, seja bem-vindo(a)!", "white", ("Arial"), 15, "#272e36", 0.5, 0.28)
texto(tela_login, "Efetue o login para realizar seu pedido:", "white", ("Arial"), 15, "#272e36", 0.5, 0.33)

texto(tela_login, "Login:", "white", ("Arial"), 13, "#272e36", 0.35, 0.4)
entrada_login = customtkinter.CTkEntry(
    tela_login, 
    width=200,
    height=30,
    fg_color= "#424f5c",
    text_color = "#b6babf",
    placeholder_text="Digite seu login",
    placeholder_text_color= "#b6babf"
    )
entrada_login.place(relx=0.55, rely=0.4, anchor='center')

texto(tela_login,"Senha: ", "white", ("Arial"), 13, "#272e36", 0.35, 0.45)
entrada_senha = customtkinter.CTkEntry(
    tela_login, 
    width=200,
    height=30,
    fg_color= "#424f5c",
    text_color = "#b6babf",
    show = "*",
    placeholder_text="Digite sua senha",
    placeholder_text_color= "#b6babf"
    )
entrada_senha.place(relx=0.55, rely=0.45, anchor='center')

texto(tela_login, "Confirme a", "white", ("Arial"), 12, "#272e36", 0.35, 0.5)
texto(tela_login,"Senha:", "white", ("Arial"), 12, "#272e36", 0.35, 0.53)
entrada_confirmar_senha = customtkinter.CTkEntry(
    tela_login, 
    width=200,
    height=30,
    fg_color= "#424f5c",
    text_color = "#b6babf",
    show = "*",
    placeholder_text="Confirme a senha",
    placeholder_text_color= "#b6babf"
    )
entrada_confirmar_senha.place(relx=0.55, rely=0.51, anchor='center')

botao_cadastrar = customtkinter.CTkButton(
    tela_login,
    text = "Entrar",
    text_color = "white",
    font = ("Arial", 12, "bold"),
    bg_color= "#424f5c",
    command= funcao_botao
    ).place(relx=0.5, rely=0.6, anchor="center")


#------------------------------------------------------------------------------------------------

#Tela Menu

tela_menu = customtkinter.CTkFrame(janelao)
quadro(tela_menu, 800, 720, "#272e36", 0.5, 0.5)
texto(tela_menu, "Éderson Restaurant", "white", ("Courier New"), 30, "#272e36", 0.5, 0.14)

foto2 = customtkinter.CTkImage(
    light_image=Image.open("tela-menu.png"),
    size=(700,620)
)
foto2_label = customtkinter.CTkLabel(tela_menu, image=foto2, text="")
foto2_label.place(relx=0.5, rely=0.52, anchor='center')

#Funções botões menu

def botao_entradas():
        tela_menu.pack_forget()
        tela_entradas.pack(fill="both", expand = True)


botao_entradas = customtkinter.CTkButton(
    tela_menu,
    text = "Entradas",
    text_color = "white",
    font = ("Arial", 15, "bold"),
    hover_color= "#768ea6",
    bg_color= '#4d5d6e',
    fg_color= "#4d5d6e",
    command= botao_entradas
    ).place(relx=0.24, rely=0.47, anchor="center")

botao_principal = customtkinter.CTkButton(
    tela_menu,
    text = "Pratos Principais",
    text_color = "white",
    font = ("Arial", 15, "bold"),
    hover_color= "#768ea6",
    bg_color= '#4d5d6e',
    fg_color= "#4d5d6e",
    command= funcao_botao
    ).place(relx=0.5, rely=0.47, anchor="center")

botao_sobremesa = customtkinter.CTkButton(
    tela_menu,
    text = "Sobremesas",
    text_color = "white",
    font = ("Arial", 15, "bold"),
    hover_color= "#768ea6",
    bg_color= '#4d5d6e',
    fg_color= "#4d5d6e",
    command= funcao_botao
    ).place(relx=0.76, rely=0.47, anchor="center")

botao_chefe = customtkinter.CTkButton(
    tela_menu,
    text = "Menu do Chefe",
    text_color = "white",
    font = ("Arial", 15, "bold"),
    hover_color= "#768ea6",
    bg_color= '#4d5d6e',
    fg_color= "#4d5d6e",
    command= funcao_botao
    ).place(relx=0.24, rely=0.78, anchor="center")

botao_bebidas = customtkinter.CTkButton(
    tela_menu,
    text = "Bebidas",
    text_color = "white",
    font = ("Arial", 15, "bold"),
    hover_color= "#768ea6",
    bg_color= '#4d5d6e',
    fg_color= "#4d5d6e",
    command= funcao_botao
    ).place(relx=0.5, rely=0.78, anchor="center")

botao_bebialcool = customtkinter.CTkButton(
    tela_menu,
    text = "Bebidas Alcoólicas",
    text_color = "white",
    font = ("Arial", 15, "bold"),
    hover_color= "#768ea6",
    bg_color= '#4d5d6e',
    fg_color= "#4d5d6e",
    command= funcao_botao
    ).place(relx=0.76, rely=0.78, anchor="center")

#------------------------------------------------------------------------------------------------

tela_entradas = customtkinter.CTkFrame(janelao)
quadro(tela_entradas, 800, 720, "#272e36", 0.5, 0.5)
texto(tela_entradas, "Éderson Restaurant", "white", ("Courier New"), 30, "#272e36", 0.5, 0.14)

foto3 = customtkinter.CTkImage(
    light_image=Image.open("tela_entradas.png"),
    size=(700,620)
)
foto3_label = customtkinter.CTkLabel(tela_entradas, image=foto3, text="")
foto3_label.place(relx=0.5, rely=0.52, anchor='center')

janelao.mainloop()

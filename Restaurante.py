from PIL import Image
import customtkinter
from tkinter import messagebox

janelao = customtkinter.CTk()
janelao.configure(bg='#2E2E2E')
janelao.title("Restaurante do Ederson")
janelao.geometry("900x900")
janelao.maxsize(900,900)
janelao.minsize(900,900)
janelao._set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#def pra trocar tela
def trocar_janela():
    tela_login.pack_forget()
    tela_menu.pack(fill="both", expand = True)


#frame Janela 1 = Login 
tela_login = customtkinter.CTkFrame(janelao)
tela_login.pack(fill="both", expand = True)

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
        fg_color= cor
        ).place(relx= posx, rely=posy, anchor="center")

#def função botão "Entrar"
def funcao_botao():
    global entrada_login, entrada_senha, entrada_confirmar_senha
    login = entrada_login.get()
    senha = entrada_senha.get()
    senha_de_novo = entrada_confirmar_senha.get()

    if login == "" or senha == "" or senha_de_novo == "":
        messagebox.showwarning("ATENÇÃO!", "Campo não preenchido, confira os campos de cadastro e tente novamente.")
    elif login == senha:
        messagebox.showwarning("ATENÇÃO!","O login e a senha nao podem ser iguais.")
    elif senha != senha_de_novo:
        messagebox.showwarning("ATENÇÃO!", "Senhas não coincidem!!")
    else:
       messagebox.showwarning("SUCESSO!","Cadastro Realizado com Sucesso!")
       trocar_janela()


def botao_clicar():
    funcao_botao()

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

texto(tela_login, "Login:", "white", ("Arial"), 15, "#272e36", 0.35, 0.4)
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

texto(tela_login,"Senha: ", "white", ("Arial"), 15, "#272e36", 0.35, 0.45)
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

texto(tela_login, "Confirme a", "white", ("Arial"), 14, "#272e36", 0.35, 0.5)
texto(tela_login,"Senha:", "white", ("Arial"), 14, "#272e36", 0.35, 0.53)
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
entrada_confirmar_senha.place(relx=0.55, rely=0.5, anchor='center')

botao_cadastrar = customtkinter.CTkButton(
    tela_login,
    text = "Entrar",
    text_color = "white",
    font = ("Arial", 12, "bold"),
    fg_color= "#424f5c",
    command= botao_clicar
    ).place(relx= 0.5, rely=0.6, anchor="center")

tela_menu = customtkinter.CTkFrame(janelao)

quadro(tela_menu, 800, 720, "#272e36", 0.5, 0.5)
texto(tela_menu, "Éderson Restaurant", "white", ("Courier New"), 35, "#272e36", 0.5, 0.16)

janelao.mainloop()

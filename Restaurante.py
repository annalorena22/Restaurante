from PIL import Image
import customtkinter

janelao = customtkinter.CTk()
janelao.configure(bg='#2E2E2E')
janelao.title("Restaurante do Ederson")
janelao.geometry("1080x1024")
janelao.maxsize(1080,1024)
janelao.minsize(1080,1024)

def quadro(width, height, cor, posx, posy):
    customtkinter.CTkFrame(
        master=janelao,
        width=width,
        height=height,
        fg_color=cor
        ).place(relx= posx, rely=posy, anchor="center")
    
quadro(1000, 820, "#FF6E40", 0.5,0.5)

def texto(texto, cor_do_texto, fonte, tamanho, cor, posx, posy, tipo_letra):
    customtkinter.CTkLabel(
        master=janelao,
        text = texto,
        text_color = cor_do_texto,
        font = (fonte, tamanho, tipo_letra),
        fg_color= cor
        ).place(relx= posx, rely=posy, anchor="center")
    
texto("Restaurante do Éderson", "white", ("Arial"), 35, "bold", "#FF6E40", 0.5, 0.2)
texto("Efetue o login para realizar seu pedido:", "black", ("Arial"), 15, "normal", "#FF6E40", 0.8, 0.33)

texto("Login:", "black", ("Arial"), 15, "bold", "#FF6E40", 0.7, 0.4)
entrada_login = customtkinter.CTkEntry(
    janelao, 
    width=200,
    height=30,
    fg_color= "#FF8A65",
    placeholder_text="Digite seu login",
    placeholder_text_color= "#424242"
    )
entrada_login.place(relx=0.82, rely=0.4, anchor='center')

texto("Senha:", "black", ("Arial"), 15, "bold", "#FF6E40", 0.7, 0.5)
entrada_senha = customtkinter.CTkEntry(
    janelao, 
    width=200,
    height=30,
    fg_color= "#FF8A65",
    placeholder_text="Digite sua senha",
    placeholder_text_color= "#424242"
    )
entrada_senha.place(relx=0.82, rely=0.5, anchor='center')

foto1 = customtkinter.CTkImage(
    light_image=Image.open("hamburguer-inicio.jpg"),
    size=(668,375)
)
foto1_label = customtkinter.CTkLabel(janelao, image=foto1, text="")
foto1_label.place(relx=0.35, rely=0.5, anchor='center')


janelao.mainloop()

# arrumar cor da borda do entry;
# arrumar negrito de alguns textos;
# arrumar risquinho no login;
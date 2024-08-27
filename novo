from PIL import Image
import customtkinter

janelao = customtkinter.CTk()
janelao.configure(bg='#2E2E2E')
janelao.title("Restaurante do Ederson")
janelao.geometry("1024x720")

def quadro(width, height, cor, posx, posy):
    customtkinter.CTkFrame(
        master=janelao,
        width=width,
        height=height,
        fg_color=cor
        ).place(relx= posx, rely=posy, anchor="center")
    
quadro(600, 700, "#ffdede", 0.5,0.5)

def texto(texto, cor_do_texto, fonte, tamanho, cor, posx, posy):
    customtkinter.CTkLabel(
        master=janelao,
        text = texto,
        text_color = cor_do_texto,
        font = (fonte, tamanho),
        fg_color= cor
        ).place(relx= posx, rely=posy, anchor="center")
    
texto("Restaurante do Éderson", "black", ("Arial bold"), 20, "#ffdede", 0.5, 0.1)
texto("Efetue o login para realizar seu pedido:", "black", ("Arial"), 15, "#ffdede", 0.34, 0.2)
texto("Login:", "black", ("Arial"), 15, "#ffdede", 0.34, 0.3)
texto("Senha:", "black", ("Arial"), 15, "#ffdede", 0.34, 0.4)


janelao.mainloop()
from tkinter import *

class Tela:

    def __init__(self, master):

        #Imagens
        cab = PhotoImage(file="cab.png")
        self.img = Label(janela, image=cab)
        self.img.cab = cab
        self.img.place(x=0,y=0)

        #rod = PhotoImage(file="rod.png")
        #self.img2 = Label(janela, image=rod)
        #self.img2.rod = rod
        #self.img2.place(x=0,y=500)


        #Usuario
        self.lb_usuario = Label(janela, text="Usuário:")
        self.lb_usuario["font"] = ("Lucida", "27")
        self.lb_usuario.place(x=170,y=120)

        self.usuarioE = Entry(janela)
        self.usuarioE["font"] = ("Lucida", "27")
        self.usuarioE.config(bg="grey")
        self.usuarioE.place(x=310,y=120, width=290)

        #Senha
        self.lb_senha = Label(janela, text="Senha:")
        self.lb_senha["font"] = ("Lucida", "27")
        self.lb_senha.place(x=190,y=212)

        self.senhaE = Entry(janela, show="*")
        self.senhaE["font"] = ("Lucida", "27")
        self.senhaE.config(bg="grey")
        self.senhaE.place(x=310,y=212, width=290)

        #Botões
        self.bt_acessar = Button(janela, text="Acessar")
        self.bt_acessar["font"] = ("Lucida", "19")
        self.bt_acessar.config(bg="#1C1C1C", foreground="white")
        self.bt_acessar.place(x=350,y=290, width=180)

        self.bt_criar = Button(janela, text="Criar uma nova conta")
        self.bt_criar["font"] = ("Lucida", "19")
        self.bt_criar.config(bg="silver", foreground="red")
        self.bt_criar.place(x=270,y=380, width=320)
        self.bt_criar.bind("<Button-1>", self.criar_conta)

    def criar_conta(self, event):

        self.lb_usuario.config(text="Novo usuário:")
        self.lb_usuario.place(x=80,y=120)

        self.lb_senha.config(text="Nova senha:")
        self.lb_senha.place(x=100,y=212)

        self.bt_criar.place_forget()
        self.bt_acessar.place_forget()

        self.bt_registrar = Button(janela, text="Cadastrar")
        self.bt_registrar["font"] = ("Lucida", "19")
        self.bt_registrar.config(bg="darkgreen", foreground="white")   
        self.bt_registrar.place(x=350,y=290, width=180)

        self.bt_voltar = Button(janela, text="Voltar")
        self.bt_voltar["font"] = ("Lucida", "14")
        self.bt_voltar.config(bg="black", foreground="white")   
        self.bt_voltar.place(x=5,y=410, width=130)
        self.bt_voltar.bind("<Button-1>", self.voltar)

    def voltar(self, event):

        self.bt_registrar.place_forget()
        self.bt_voltar.place_forget()
        
        self.lb_usuario.config(text="Usuário:")
        self.lb_usuario["font"] = ("Lucida", "27")
        self.lb_usuario.place(x=170,y=120)

        self.lb_senha.config(text="Senha:")
        self.lb_senha["font"] = ("Lucida", "27")
        self.lb_senha.place(x=190,y=212)
        
        self.bt_acessar.place(x=350,y=290, width=180)
        self.bt_criar.place(x=270,y=380, width=320)
        

        

janela = Tk()
Tela(janela)
janela.geometry("800x450+200+100")
janela.title("CJ Systems - Login")
janela.mainloop()

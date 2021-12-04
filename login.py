from tkinter import *
import DataBase
from tkinter import messagebox

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
        self.bt_acessar.bind("<Button-1>", self.logar)

        self.bt_criar = Button(janela, text="Criar uma nova conta")
        self.bt_criar["font"] = ("Lucida", "19")
        self.bt_criar.config(bg="silver", foreground="red")
        self.bt_criar.place(x=270,y=380, width=320)
        self.bt_criar.bind("<Button-1>", self.criar_conta)

    def logar(self, event):

        u = self.usuarioE.get()
        s = self.senhaE.get()

        DataBase.cursor.execute("""
        SELECT * FROM Users
        WHERE Usuario = ? and Senha = ?
        """, [u, s])

        verifica = DataBase.cursor.fetchone()

        try:
            if(u in verifica) and (s in verifica):

                self.senhaE.delete(0, "end")
                self.usuarioE.delete(0, "end")
                janela2 = Tk()

                self.lb = Label(janela2, text="root@debian:~$")
                self.lb["font"] = ("Lucida console", "18")
                self.lb.config(bg="black", foreground="white")
                self.lb.place(x=5, y=10)

                self.linuxE = Entry(janela2)
                self.linuxE["font"] = ("Lucida console", "18")
                self.linuxE.config(bg="black", foreground="limegreen")
                self.linuxE.place(x=220, y=10, width=640)

                self.p1 = Label(janela2, text="Digite o comando para ir \n\npara a raiz do sistema")
                self.p1["font"] = ("Lucida console", "27")
                self.p1.config(bg="#1C1C1C", foreground="RED")
                self.p1.place(x=160, y=300)

                

                self.bt_enter = Button(janela2, text=">")
                self.bt_enter["font"] = ("Lucida console", "18")
                self.bt_enter.config(bg="green", foreground="white")
                self.bt_enter.place(x=865, y=10, width=30, height=30)
                self.bt_enter.bind("<Button-1>", self.comandos)

                
                janela2.config(bg="black")
                janela2.geometry("900x450+200+100")
                janela2.resizable(width=False, height=False)
                janela2.mainloop()

                

                
        except:
            
            messagebox.showerror("Erro ao acessar", "Usuário ou senha inválidos.")
            self.senhaE.delete(0, "end")
            self.usuarioE.delete(0, "end")

    
        
        
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
        self.bt_registrar.bind("<Button-1>", self.registrar_usuario)

        self.bt_voltar = Button(janela, text="Voltar")
        self.bt_voltar["font"] = ("Lucida", "14")
        self.bt_voltar.config(bg="black", foreground="white")   
        self.bt_voltar.place(x=5,y=410, width=130)
        self.bt_voltar.bind("<Button-1>", self.voltar)

    def registrar_usuario(self, event):

        u = self.usuarioE.get()
        s = self.senhaE.get()

        if(u) == "" or (s) == "":
            self.usuarioE.config(bg="#FF6347")
            self.senhaE.config(bg="#FF6347")
            messagebox.showwarning("Dados inválidos", "Nenhum campo pode ficar em branco.")
            self.senhaE.config(bg="grey")
            self.usuarioE.config(bg="grey")
            
        else:

            DataBase.cursor.execute("""
                SELECT * FROM Users
                WHERE Usuario == ?
                """, [u])

            try:
                
                consulta = DataBase.cursor.fetchone()    
                if(u in consulta):
                    messagebox.showerror("Dados existentes", "Esse nome de usuário já está sendo utilizado.")
                    self.usuarioE.delete(0, "end")

            except:
                
                
                DataBase.cursor.execute("""
                INSERT INTO Users(Usuario, Senha) VALUES(?,?)
                """, (u,s))

                DataBase.con.commit()
                self.usuarioE.config(bg="#00FA9A")
                self.senhaE.config(bg="#00FA9A")
                messagebox.showinfo("Dados registrados", "Conta criada com sucesso.")
                self.usuarioE.delete(0, "end")
                self.senhaE.delete(0, "end")
                self.usuarioE.config(bg="grey")
                self.senhaE.config(bg="grey")
            
           
            

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

        self.senhaE.delete(0, "end")
        self.usuarioE.delete(0, "end")
        

        

janela = Tk()
Tela(janela)
janela.geometry("800x450+200+100")
janela.title("CJ Systems - Login")
janela.resizable(width=False, height=False)
janela.mainloop()

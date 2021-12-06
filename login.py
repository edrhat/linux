from tkinter import *
import DataBase
from tkinter import messagebox
import time

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


                self.img.place_forget()

            
            
                self.lb_usuario.place_forget()

        
                self.usuarioE.place_forget()

        
                self.lb_senha.place_forget()

        
                self.senhaE.place_forget()

        
                self.bt_acessar.place_forget()
        

           
                self.bt_criar.place_forget()
                messagebox.showinfo("TESTE DE DESEMPENHO", "Bem-vindo {}".format(u))
    
                self.lb = Label(janela, text="root@debian:~$")
                self.lb["font"] = ("Lucida console", "18")
                self.lb.config(bg="black", foreground="white")
                self.lb.place(x=5, y=10)

                self.linuxE = Entry(janela)
                self.linuxE["font"] = ("Lucida console", "18")
                self.linuxE.config(bg="black", foreground="limegreen")
                self.linuxE.place(x=220, y=10, width=640)

                self.p1 = Label(janela, text="Digite o comando para ir \n\npara a raiz do sistema")
                self.p1["font"] = ("Lucida console", "27")
                self.p1.config(bg="#1C1C1C", foreground="RED")
                self.p1.place(x=160, y=300)

                

                self.bt_enter = Button(janela, text=">")
                self.bt_enter["font"] = ("Lucida console", "18")
                self.bt_enter.config(bg="green", foreground="white")
                self.bt_enter.place(x=865, y=10, width=30, height=30)
                self.bt_enter.bind("<Button-1>", self.comando1)

                
                janela.config(bg="black")
                janela.geometry("900x450+200+100")
                janela.resizable(width=False, height=False)
                janela.title("Debian Server")
                janela.mainloop()
                
        except:
            messagebox.showwarning("Dados inexistente","Usuário ou senha incorretos.")

    def comando1(self, event):

        c = self.linuxE.get()
        u = self.usuarioE.get()
        if(c) == "cd /":
            
            self.linuxE.delete(0, "end")
            self.p1.place_forget()
            self.p1 = Label(janela, text="Crie um diretório com o nome de\n\n 'Hardware'")
            self.p1.config(bg="#1C1C1C", foreground="yellow")
            self.p1["font"] = ("Lucida console", "27")
            self.p1.place(x=100, y=300)

            self.bt_enter.place_forget()
            self.bt_enter = Button(janela, text=">")
            self.bt_enter["font"] = ("Lucida console", "18")
            self.bt_enter.config(bg="green", foreground="white")
            self.bt_enter.place(x=865, y=10, width=30, height=30)
            self.bt_enter.bind("<Button-1>", self.comando2)
            
        else:
         
            
            self.linuxE.config(bg="black")
            
            

    def comando2(self, event):

        c = self.linuxE.get()
        if(c) == "mkdir Hardware":
            #messagebox.showinfo("Comando correto", "CONTINUE ASSIM.")
            self.linuxE.delete(0, "end")
            self.p1.place_forget()
            self.p1 = Label(janela, text="Acesse o diretório 'Hardware'")
            self.p1.config(bg="#1C1C1C", foreground="limegreen")
            self.p1["font"] = ("Lucida console", "27")
            self.p1.place(x=100, y=300)

            self.bt_enter.place_forget()
            self.bt_enter = Button(janela, text=">")
            self.bt_enter["font"] = ("Lucida console", "18")
            self.bt_enter.config(bg="green", foreground="white")
            self.bt_enter.place(x=865, y=10, width=30, height=30)
            self.bt_enter.bind("<Button-1>", self.comando3)

    def comando3(self, event):

        c = self.linuxE.get()
        if(c) == "cd Hardware":
            #messagebox.showinfo("Comando correto", "DESSE JEITO NEM A NASA AGUENTA.")
            self.linuxE.delete(0, "end")
            self.p1.place_forget()
            self.p1 = Label(janela, text="Liste os  arquivos e diretórios.")
            self.p1.config(bg="#1C1C1C", foreground="lightblue")
            self.p1["font"] = ("Lucida console", "27")
            self.p1.place(x=100, y=300)

            self.bt_enter.place_forget()
            self.bt_enter = Button(janela, text=">")
            self.bt_enter["font"] = ("Lucida console", "18")
            self.bt_enter.config(bg="green", foreground="white")
            self.bt_enter.place(x=865, y=10, width=30, height=30)
            self.bt_enter.bind("<Button-1>", self.comando4)

    

    def comando4(self, event):

        c = self.linuxE.get()
        if(c) == "ls":
            #messagebox.showinfo("Comando correto", "ESTÃO DIZENDO QUE ZUCKERBERG É UM BEBEZINHO PERTO DE VOCÊ.")
            self.linuxE.delete(0, "end")
            self.p1.place_forget()
            self.p1 = Label(janela, text="Crie um arquivo de texto com \n\n o nome de microcamp")
            self.p1.config(bg="#1C1C1C", foreground="brown")
            self.p1["font"] = ("Lucida console", "27")
            self.p1.place(x=100, y=300)

            self.bt_enter.place_forget()
            self.bt_enter = Button(janela, text=">")
            self.bt_enter["font"] = ("Lucida console", "18")
            self.bt_enter.config(bg="green", foreground="white")
            self.bt_enter.place(x=865, y=10, width=30, height=30)
            self.bt_enter.bind("<Button-1>", self.comando5)

    def comando5(self, event):

        c = self.linuxE.get()
        if(c) == "touch microcamp.txt":
            #messagebox.showinfo("Comando correto", "OS INTEGRANTES DO 'ANONYMOUS' GRITARAM VIIXIIIII.")
            self.linuxE.delete(0, "end")
            self.p1.place_forget()
            self.p1 = Label(janela, text="Exclua o arquivo microcamp.txt")
            self.p1.config(bg="#1C1C1C", foreground="purple")
            self.p1["font"] = ("Lucida console", "27")
            self.p1.place(x=100, y=300)

            self.bt_enter.place_forget()
            self.bt_enter = Button(janela, text=">")
            self.bt_enter["font"] = ("Lucida console", "18")
            self.bt_enter.config(bg="green", foreground="white")
            self.bt_enter.place(x=865, y=10, width=30, height=30)
            self.bt_enter.bind("<Button-1>", self.comando6)

    def comando6(self, event):

        c = self.linuxE.get()
        if(c) == "rm microcamp.txt":
            #messagebox.showinfo("Comando correto", "E JESUS ORDENOU: ABRAM-SE OS TERMINAIS.")
            self.linuxE.delete(0, "end")
            self.p1.place_forget()
            self.p1 = Label(janela, text="Volte um diretório")
            self.p1.config(bg="#1C1C1C", foreground="pink")
            self.p1["font"] = ("Lucida console", "27")
            self.p1.place(x=100, y=300)

            self.bt_enter.place_forget()
            self.bt_enter = Button(janela, text=">")
            self.bt_enter["font"] = ("Lucida console", "18")
            self.bt_enter.config(bg="green", foreground="white")
            self.bt_enter.place(x=865, y=10, width=30, height=30)
            self.bt_enter.bind("<Button-1>", self.comando7)

    def comando7(self, event):

        c = self.linuxE.get()
        if(c) == "cd ..":
            #messagebox.showinfo("Comando correto", "O PENTÁGONO ESTÁ DE OLHO.")
            self.linuxE.delete(0, "end")
            self.p1.place_forget()
            self.p1 = Label(janela, text="Exclua o diretório 'Hardware'")
            self.p1.config(bg="#1C1C1C", foreground="lightgrey")
            self.p1["font"] = ("Lucida console", "27")
            self.p1.place(x=100, y=300)

            self.bt_enter.place_forget()
            self.bt_enter = Button(janela, text=">")
            self.bt_enter["font"] = ("Lucida console", "18")
            self.bt_enter.config(bg="green", foreground="white")
            self.bt_enter.place(x=865, y=10, width=30, height=30)
            self.bt_enter.bind("<Button-1>", self.comando8)

    def comando8(self, event):

        c = self.linuxE.get()
        if(c) == "rm -r Hardware":
            #messagebox.showinfo("Comando correto", "O PENTÁGONO ESTÁ DE OLHO.")
            self.linuxE.delete(0, "end")
            self.p1.place_forget()
            self.p1 = Label(janela, text="Crie um usuário com o nome de 'suporte'")
            self.p1.config(bg="#1C1C1C", foreground="red")
            self.p1["font"] = ("Lucida console", "27")
            self.p1.place(x=10, y=300)

            self.bt_enter.place_forget()
            self.bt_enter = Button(janela, text=">")
            self.bt_enter["font"] = ("Lucida console", "18")
            self.bt_enter.config(bg="green", foreground="white")
            self.bt_enter.place(x=865, y=10, width=30, height=30)
            self.bt_enter.bind("<Button-1>", self.comando9)

    def comando9(self, event):

        c = self.linuxE.get()
        if(c) == "adduser suporte":
            messagebox.showinfo("Comando correto", "Usuário criado com sucesso.")
          
            self.linuxE.delete(0, "end")
            self.p1.place_forget()
            self.p1 = Label(janela, text="Logue como usuário 'suporte'")
            self.p1.config(bg="#1C1C1C", foreground="lightgrey")
            self.p1["font"] = ("Lucida console", "27")
            self.p1.place(x=10, y=300)

            self.bt_enter.place_forget()
            self.bt_enter = Button(janela, text=">")
            self.bt_enter["font"] = ("Lucida console", "18")
            self.bt_enter.config(bg="green", foreground="white")
            self.bt_enter.place(x=865, y=10, width=30, height=30)
            self.bt_enter.bind("<Button-1>", self.comando10)

    def comando10(self, event):

        c = self.linuxE.get()
        if(c) == "su suporte":
            #messagebox.showinfo("Comando correto", "Logado como 'suporte'")

            self.lb.place_forget()
            self.lb = Label(janela, text="suporte@debian:~$")
            self.lb["font"] = ("Lucida console", "18")
            self.lb.config(bg="black", foreground="lightblue")
            self.lb.place(x=5, y=10)

            self.linuxE.delete(0, "end")
            self.p1.place_forget()
            self.p1 = Label(janela, text="Acesse a pasta pessoal do usuário \n\n'suporte'")
            self.p1.config(bg="#1C1C1C", foreground="lightgrey")
            self.p1["font"] = ("Lucida console", "27")
            self.p1.place(x=10, y=300)

            self.linuxE.place_forget()
            self.linuxE = Entry(janela)
            self.linuxE["font"] = ("Lucida console", "18")
            self.linuxE.config(bg="black", foreground="limegreen")
            self.linuxE.place(x=260, y=10, width=570)
            
            self.bt_enter.place_forget()
            self.bt_enter = Button(janela, text=">")
            self.bt_enter["font"] = ("Lucida console", "18")
            self.bt_enter.config(bg="green", foreground="white")
            self.bt_enter.place(x=865, y=10, width=30, height=30)
            self.bt_enter.bind("<Button-1>", self.comando11)

    def comando11(self, event):

        c = self.linuxE.get()
        if(c) == "cd /home/suporte":
            #messagebox.showinfo("Comando correto", "Logado como 'suporte'")

            self.lb.place_forget()
            self.lb = Label(janela, text="suporte@debian:/home/suporte")
            self.lb["font"] = ("Lucida console", "18")
            self.lb.config(bg="black", foreground="lightblue")
            self.lb.place(x=5, y=10)

            self.linuxE.delete(0, "end")
            self.p1.place_forget()
            self.p1 = Label(janela, text="Logue como usuário 'root'")
            self.p1.config(bg="#1C1C1C", foreground="lightgrey")
            self.p1["font"] = ("Lucida console", "27")
            self.p1.place(x=40, y=300)

            self.linuxE.place(x=400, y=10, width=480)

            self.bt_enter.place_forget()
            self.bt_enter = Button(janela, text=">")
            self.bt_enter["font"] = ("Lucida console", "18")
            self.bt_enter.config(bg="green", foreground="white")
            self.bt_enter.place(x=865, y=10, width=30, height=30)
            self.bt_enter.bind("<Button-1>", self.comando12)

    def comando12(self, event):

        c = self.linuxE.get()
        if(c) == "su root" or (c) == "sudo su":
            #messagebox.showinfo("Comando correto", "Logado como 'suporte'")

            self.lb.place_forget()
            self.lb = Label(janela, text="suporte@debian:/home/suporte")
            self.lb["font"] = ("Lucida console", "18")
            self.lb.config(bg="black", foreground="lightblue")
            self.lb.place(x=5, y=10)

            self.linuxE.delete(0, "end")
            self.p1.place_forget()
            self.p1 = Label(janela, text="Delete o usuário 'suporte'")
            self.p1.config(bg="#1C1C1C", foreground="lightgrey")
            self.p1["font"] = ("Lucida console", "27")
            self.p1.place(x=40, y=300)

            self.bt_enter.place_forget()
            self.bt_enter = Button(janela, text=">")
            self.bt_enter["font"] = ("Lucida console", "18")
            self.bt_enter.config(bg="green", foreground="white")
            self.bt_enter.place(x=865, y=10, width=30, height=30)
            self.bt_enter.bind("<Button-1>", self.comando12)

     


  


    
        
        
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

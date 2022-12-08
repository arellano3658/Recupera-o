import tkinter.messagebox
from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessagerBox

cor1 = "#C0C0C0"
cor1 = "#C0C0C0"
principal = tk()
principal.title("Jogos da Copa")
principa.config(background = cor1)
principal.geometry("300x300")

#metodos

def banco():
  global conexao, cursor
  conexao = sqlite3.connet("banco.db")
  cursor = conexao.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS 'jogos da copa' (id INTERGER PRIMARY KEY AUTOINCREMENT NOT NULL, grupo TEXT, primeira selecao TEXT,  segunda selecao TEXT, terceira selecao TEXT, quarta selecao TEXT")

def cadastrar():
    banco()
    cursor.execute("INSERT INTO 'jogos da copa' (grupo, primeira selecao, segunda selecao, terceira selecao, quarta selecao) VALUES (?,?,?,?,?)",
   (str(grupo.get()), float(primeiraselecao.get()), float(segundaselecao.get()), 
float(terceiraselecao.get()), float(quartaselecao.get())))
  conexao.commit()
  print("DADOS CADASTRADOS COM SUCESSO")
  conexao.close
  grupo.delete(0, "end")
  primeira selecao.delete(0, "end")
  Segunda selecao.delete(0, "end")
  Terceira selecao.delete(0, "end")
  quarta selecao.delete(0, "end")
  cursor.close()                           
  conexao.close()
  tkinter.messagerbox.showinfo(title="SUCESSO", message="JOGO SALVO")
                                                    
#variaveis

grupo = StringVar()                                                    
Primeira Selecao = StringVar()
Segunda Selecao = StringVar()
Terceira Selecao = StringVar()
Quarta Selecao = StringVar()

#frame

topo = Frame(principal, width=600, heigth=50, bd=1, relief="raise")
topo.pack(side=TOP)

esquerda = Frame(principal, width=300, heigth=50, bd=1, relief="raise",
background=cor1)
esquerda.pack(side=LEFT)

Forms = Frame(esquerda, width=300, heigth=50, background=cor1)
Forms.pack(side=TOP)

Buttons = Frame(esquerda, width=300, heigth=50, background=cor1, relief="raise")
Buttons.pack(side=BOTTOM)

#labels

txt_titulo = Label(topo, width=600, font=("arial", 18), text = "jogos da Copa", background=cor1)
txt_titulo.pack()

txt_listar seleçao = Label(Forms, text="Listar seleçao", font=("arial", 10), bd=15, background=cor1)
txt_grupo.grid(row=0, stick="e")

txt_salvar = Label(Forms, text="Salvar", font=("arial", 10), bd=15, background=cor1)
txt_grupo.grid(row=1, stick="e")

txt_cancelar = Label(Forms, text="Cancelar", font=("arial", 10), bd=15, background=cor1)
txt_grupo.grid(row=2, stick="e")

# entrys

grupo = Entry(Forms, textvariable=grupo, width=25)
grupo.grid(row=0, column=1)
primeira selecao = Entry(Forms, textvariable=primeira selecao, width=25)
primeira selecao.grid(row=0, column=1)
segunda selecao = Entry(Forms, textvariable=segunda selecao, width=25)
segunda selecao.grid(row=0, column=1)
terceira selecao = Entry(Forms, textvariable=terceira selecao, width=25)
terceira selecao.grid(row=0, column=1)
quarta selecao = Entry(Forms, textvariable=quarta selecao, width=25)
quarta selecao.grid(row=0, column=1)

#botoes

btn_listar selecao = Button(Buttons, width=10, text="Listar selecao",
command=cadastrar)
btn_listar selecao.pack(side=LEFT)
btn_salvar = Button(Buttons, width=10, text="Salvar",
command=cadastrar)
btn_salvar.pack(side=LEFT)
btn_cancelar = Button(Buttons, width=10, text="Cancelar",
command=cadastrar)
btn_cancelar.pack(side=LEFT)
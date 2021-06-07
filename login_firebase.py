

from tkinter import *
import funct_firebase
import disciplinas_firebase


class login_firebase:

	def __init__ (self):

		self.principal = Tk ()
		self.principal.title ('Login')
		self.principal.geometry ('800x600')

		self.conteiner = []

		for i in range (5):

			self.conteiner.append (Frame ())
			self.conteiner[i]['pady'] = 10
			self.conteiner[i].pack ()

		
		self.login = Label (self.conteiner[0], text = "--> LOGIN <--")
		self.login.pack ()

		
		self.email = Label (self.conteiner[1], text = "E-mail ")
		self.email.pack (side = LEFT)

		self.entrada_email = Entry (self.conteiner[1])
		self.entrada_email ["width"] = 30
		self.entrada_email ["font"] = ("", "12")
		self.entrada_email.pack (side = LEFT)

		self.senha = Label (self.conteiner[2], text = "Senha")
		self.senha.pack (side = LEFT)

		self.entrada_senha = Entry (self.conteiner[2], show = '*')
		self.entrada_senha ["width"] = 30
		self.entrada_senha ["font"] = ("", "12")
		self.entrada_senha.pack (side = LEFT)


		self.autenticar = Button (self.conteiner[3])
		self.autenticar ["text"] = "autenticar"
		self.autenticar ["font"] = ("Calibri", "9")
		self.autenticar ["width"] = 20
		self.autenticar ["command"] = self.chamar_aut
		self.autenticar.pack (side = LEFT)	
		self.principal.mainloop ()

	def chamar_aut (self):
	
		ch = funct_firebase.aut (self.entrada_email.get (), self.entrada_senha.get ()) #chama a função aut do outro arquivo com os paramentros de email e senha inseridos
	
		if (ch == False):

			self.conteiner[-1].destroy ()
			self.conteiner[-1] = Frame ()
			self.conteiner[-1] ["pady"] = 10
			self.conteiner[-1].pack ()  

			self.falha_aut = Label (self.conteiner[-1], text = "Falha na autenticação. Repita o procedimento.")
			self.falha_aut.pack (side = LEFT)

		else:

			self.principal.destroy ()	

			disciplinas_firebase.disciplinas_firebase ()

login_firebase ()


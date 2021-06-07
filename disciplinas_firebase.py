from tkinter import *
import funct_firebase
import python_firebase

class disciplinas_firebase:

	def __init__ (self):

		self.principal = Tk ()
		self.principal.title ("Disciplinas")
		self.principal.geometry ('800x600')

		self.conteiner = []
		self.botao = []

		for i in range (2):

			self.conteiner.append (Frame ())
			self.conteiner[i]['pady'] = 10
			self.conteiner[i].pack ()

		self.disciplinas = Label (self.conteiner[0], text = "--> Disciplinas <--")
		self.disciplinas.pack ()

		self.qde_disciplinas = funct_firebase.disp_disciplinas ()

		'''
		for i in range (len(self.qde_disciplinas)):

			self.botao.append (Button (self.conteiner[-1]))

			self.botao[-1]["text"] = self.qde_disciplinas[i]
			self.botao[-1]["font"] = ("Calibri", "9")
			self.botao[-1]["width"] = 20
			self.botao[-1]["command"] =  
			self.botao[-1].pack (side = LEFT)	
		'''
		for i in range (len(self.qde_disciplinas)):

			if (self.qde_disciplinas[i] == 'python'):

				self.python = Button (self.conteiner[-1])
				self.python ["text"] = "Python"
				self.python ["font"] = ("Calibri", "9")
				self.python ["width"] = 20
				self.python ["command"] = self.chamar_python
				self.python.pack (side = LEFT)

			if (self.qde_disciplinas[i] == 'java'):	
		
				self.java = Button (self.conteiner[-1])
				self.java ["text"] = "Java"
				self.java ["font"] = ("Calibri", "9")
				self.java ["width"] = 20
				#self.java ["command"] = self.chamar_java 
				self.java.pack (side = LEFT)

		self.principal.mainloop ()	
	'''	
	def chamar_disciplina (self, botao_texto):
		
		print (botao_texto)
	'''
	def chamar_python (self):

		self.principal.destroy ()
		
		python_firebase.pdf_python_firebase ()


		





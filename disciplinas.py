
from tkinter import *
import python
import login

class disciplinastk:

	def __init__ (self):

		self.principal = Tk ()
		self.principal.title ("Disciplinas")
		self.principal.geometry ('800x600')            

		self.ct1 = Frame ()
		self.ct1 ["pady"] = 10
		self.ct1.pack ()
        
		self.ct2 = Frame ()
		self.ct2 ["pady"] = 10
		self.ct2.pack ()

		self.disciplinas = Label (self.ct1, text = "--> Disciplinas <--")
		self.disciplinas.pack ()
        
		self.python = Button (self.ct2)
		self.python ["text"] = "Python"
		self.python ["font"] = ("Calibri", "9")
		self.python ["width"] = 20
		self.python ["command"] = self.chamar_python
		self.python.pack (side = LEFT)


		self.mobile = Button (self.ct2)
		self.mobile ["text"] = "Mobile"
		self.mobile ["font"] = ("Calibri", "9")
		self.mobile ["width"] = 20
		#self.autenticar ["command"] = self.chamar_aut #Chama a função "chamar_aut"
		self.mobile.pack (side = LEFT)


		self.java = Button (self.ct2)
		self.java ["text"] = "Java"
		self.java ["font"] = ("Calibri", "9")
		self.java ["width"] = 20
		#self.autenticar ["command"] = self.chamar_aut #Chama a função "chamar_aut"
		self.java.pack (side = LEFT)

		self.principal.mainloop()

	def chamar_python (self):

		self.principal.destroy ()

		python.pythontk ()	



#disciplinastk ()
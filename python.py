from tkinter import *
import disciplinas

class pythontk:

	def __init__ (self):


		self.lista = ['Python para desenvolvedores', 'Python Orientado a objetos', 'Python para Web'] #Receber os elementos que estão dentro da disciplina

		self.principal = Tk ()
		self.principal.title ('Disciplina -> Python')
		self.principal.geometry ('800x600')

		self.ct1 = Frame () #Constroi os conteiners da janela
		self.ct1 ["pady"] = 10
		self.ct1.pack (side = TOP)
        
		self.ct2 = Frame ()
		self.ct2 ["pady"] = 10
		self.ct2.pack ()

		self.ct3 = Frame ()
		self.ct3 ["pady"] = 10
		self.ct3.pack ()



		self.sb = Label (self.ct1, text = "PYTHON ")
		self.sb.pack (side = RIGHT)

		self.voltar_disciplinas = Button (self.ct1)
		self.voltar_disciplinas ["text"] = "<--"
		self.voltar_disciplinas ["command"] = self.chamar_disciplinas
		self.voltar_disciplinas.pack (side = LEFT)

		self.sb_title = Label (self.ct2, text = "Ordenar -> ")
		self.sb_title.pack (side = LEFT)

		self.ordena_nome = Button (self.ct2)
		self.ordena_nome ["text"] = "Nome"
		self.ordena_nome ["font"] = ("Calibri", "9")
		self.ordena_nome ["width"] = 20
		self.ordena_nome ["command"] = self.ordenar_nome
		self.ordena_nome.pack (side = LEFT)


		self.ordena_aval = Button (self.ct2)
		self.ordena_aval ["text"] = "Avaliação"
		self.ordena_aval ["font"] = ("Calibri", "9")
		self.ordena_aval ["width"] = 20
		#self.ordena_aval ["command"] = lista.sort (reverse = True) #Chamar o firebase para retornar uma lista ordenada por avaliação
		self.ordena_aval.pack (side = LEFT)


		self.pdf1 = Button (self.ct3)
		self.pdf1 ["text"] = self.lista[0]
		self.pdf1 ["font"] = ("Calibri", "9")
		self.pdf1 ["width"] = 30
		#self.bot1 ["command"] = self.chamar_pdf_python
		self.pdf1.pack ()

		self.pdf2 = Button (self.ct3)
		self.pdf2 ["text"] = self.lista[1]
		self.pdf2 ["font"] = ("Calibri", "9")
		self.pdf2 ["width"] = 30
		#self.bot2 ["command"] = self.chamar_pdf_python
		self.pdf2.pack ()

		self.pdf3 = Button (self.ct3)
		self.pdf3 ["text"] = self.lista[2]
		self.pdf3 ["font"] = ("Calibri", "9")
		self.pdf3 ["width"] = 30
		#self.bot3 ["command"] = self.chamar_pdf_python
		self.pdf3.pack ()

		self.principal.mainloop ()


	def chamar_disciplinas (self):
	
		self.principal.destroy ()

		disciplinas.disciplinastk ()




	def ordenar_nome (self):

		self.lista.sort ()	
			
		self.ct3.destroy ()

		self.ct3 = Frame ()
		self.ct3 ["pady"] = 10
		self.ct3.pack ()


		self.pdf1 = Button (self.ct3)
		self.pdf1 ["text"] = self.lista[0]
		self.pdf1 ["font"] = ("Calibri", "9")
		self.pdf1 ["width"] = 30
		#self.bot1 ["command"] = self.chamar_pdf_python
		self.pdf1.pack ()

		self.pdf2 = Button (self.ct3)
		self.pdf2 ["text"] = self.lista[1]
		self.pdf2 ["font"] = ("Calibri", "9")
		self.pdf2 ["width"] = 30
		#self.bot2 ["command"] = self.chamar_pdf_python
		self.pdf2.pack ()

		self.pdf3 = Button (self.ct3)
		self.pdf3 ["text"] = self.lista[2]
		self.pdf3 ["font"] = ("Calibri", "9")
		self.pdf3 ["width"] = 30
		#self.bot3 ["command"] = self.chamar_pdf_python
		self.pdf3.pack ()

#pythontk ()
'''				
		self.bot1 = Button (self.ct3)
		self.bot1 ["text"] = lista[0]
		self.bot1 ["font"] = ("Calibri", "9")
		self.bot1 ["width"] = 20
		#self.bot1 ["command"] = self.chamar_pdf_python
		self.bot1.pack ()

		self.bot2 = Button (self.ct3)
		self.bot2 ["text"] = lista[1]
		self.bot2 ["font"] = ("Calibri", "9")
		self.bot2 ["width"] = 20
		#self.bot2 ["command"] = self.chamar_pdf_python
		self.bot2.pack ()

		self.bot3 = Button (self.ct3)
		self.bot3 ["text"] = lista[2]
		self.bot3 ["font"] = ("Calibri", "9")
		self.bot3 ["width"] = 20
		#self.bot3 ["command"] = self.chamar_pdf_python
		self.bot3.pack ()	


		self.principal.mainloop ()


		






		##########
		self.bot1 = Button (self.ct3)
		self.bot1 ["text"] = lista[0]
		self.bot1 ["font"] = ("Calibri", "9")
		self.bot1 ["width"] = 20
		
		if (lista[0] == 'python'):

			self.bot1 ["command"] = self.chamar_pdf_python
		
		if (lista[0] == 'mobile'):
		
			self.bot1 ["command"] = self.chamar_pdf_mobile		

		if (lista[0] == 'java'):

			self.bot1 ["command"] = self.chamar_pdf_java

		self.bot1.pack ()


		self.bot2 = Button (self.ct3)
		self.bot2 ["text"] = lista[1]
		self.bot2 ["font"] = ("Calibri", "9")
		self.bot2 ["width"] = 20

		if (lista[1] == 'python'):

			self.bot2 ["command"] = self.chamar_pdf_python
		
		if (lista[1] == 'mobile'):
		
			self.bot2 ["command"] = self.chamar_pdf_mobile		

		if (lista[1] == 'java'):

			self.bot2 ["command"] = self.chamar_pdf_java
		
		self.bot2.pack ()


		self.bot3 = Button (self.ct3)
		self.bot3 ["text"] = lista[2]
		self.bot3 ["font"] = ("Calibri", "9")
		self.bot3 ["width"] = 20

		if (lista[2] == 'python'):

			self.bot3 ["command"] = self.chamar_pdf_python
		
		if (lista[2] == 'mobile'):
		
			self.bot3 ["command"] = self.chamar_pdf_mobile		

		if (lista[2] == 'java'):

			self.bot3 ["command"] = self.chamar_pdf_java
		
		self.bot3.pack ()

		self.principal.mainloop ()

	def chamar_pdf_python001 (self): #Criar em um outro arquivo

		self.ct4.destroy ()
		self.ct4 = Frame ()
		self.ct4 ["pady"] = 10
		self.ct4.pack ()

		self.msg = Label (self.ct4, text = 'Python')
		self.msg.pack ()


	def chamar_pdf_python002 (self): #Criar em um outro arquivo

		self.ct4.destroy ()
		self.ct4 = Frame ()
		self.ct4 ["pady"] = 10
		self.ct4.pack ()

		self.msg = Label (self.ct4, text = 'Mobile')
		self.msg.pack ()	

		
	def chamar_pdf_java (self): #Criar em um outro arquivo

		self.ct4.destroy ()
		self.ct4 = Frame ()
		self.ct4 ["pady"] = 10
		self.ct4.pack ()

		self.msg = Label (self.ct4, text = 'Java')
		self.msg.pack ()

'''





	

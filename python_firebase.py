

from tkinter import *
import funct_firebase
import webbrowser
import disciplinas_firebase

class pdf_python_firebase:

	def __init__ (self):

		self.principal = Tk ()
		self.principal.title ('PDF')
		self.principal.geometry ('800x600')

		self.conteiner = []
		self.nome = []
		self.qde_pdf = funct_firebase.disp_pdf ('python')

		for i in range (4):

			self.conteiner.append (Frame ())
			self.conteiner[i]['pady'] = 10
			self.conteiner[i].pack ()

		self.voltar = Button (self.conteiner[0])
		self.voltar ["text"] = "<--"	
		self.voltar ["command"] = self.voltar_win
		self.voltar.pack (side = LEFT)


		self.pdf = Label (self.conteiner[0], text = "          Disciplina: Python")
		self.pdf.pack ()

		self.chaves = list (self.qde_pdf.keys ())
		self.valores = list (self.qde_pdf.values ())


		for i in range (len(self.valores)):

			self.nome.append (self.valores[i]['nome'])

		

		self.ordena = Label (self.conteiner[1], text = "Ordenar por: ")
		self.ordena.pack (side = LEFT)

		self.ordena_nome = Button (self.conteiner[1])
		self.ordena_nome ["text"] = "Nome"
		self.ordena_nome ["font"] = ("Calibri", "9")
		self.ordena_nome ["width"] = 20
		self.ordena_nome ["command"] = self.ordenar_nome
		self.ordena_nome.pack (side = RIGHT)

		self.ordena_nota = Button (self.conteiner[1])
		self.ordena_nota ["text"] = "Nota"
		self.ordena_nota ["font"] = ("Calibri", "9")
		self.ordena_nota ["width"] = 20
		#self.ordena_nota ["command"] = self.ordenar_nota
		self.ordena_nota.pack (side = RIGHT)
		

		self.b1 = Button (self.conteiner[2])
		self.b1 ["text"] = self.nome[0]
		self.b1 ["font"] = ("Calibri", "9")
		self.b1 ["width"] = 30
		self.b1 ["command"] = lambda : self.chamar_pdf (self.nome[0])
		self.b1.pack ()

		self.b2 = Button (self.conteiner[2])
		self.b2 ["text"] = self.nome[1]
		self.b2 ["font"] = ("Calibri", "9")
		self.b2 ["width"] = 30
		self.b2 ["command"] = lambda : self.chamar_pdf (self.nome[1])
		self.b2.pack ()

		self.b3 = Button (self.conteiner[2])
		self.b3 ["text"] = self.nome[2]
		self.b3 ["font"] = ("Calibri", "9")
		self.b3 ["width"] = 30
		self.b3 ["command"] = lambda : self.chamar_pdf (self.nome[2])
		self.b3.pack ()

		self.principal.mainloop ()

	def voltar_win (self):
	
		self.principal.destroy ()
		disciplinas_firebase.disciplinas_firebase ()	

	def ordenar_nome (self):

		self.nome.sort ()

		self.conteiner[2].destroy ()

		self.conteiner[2] = (Frame ())
		self.conteiner[2]['pady'] = 10
		self.conteiner[2].pack ()

		self.b1 = Button (self.conteiner[2])
		self.b1 ["text"] = self.nome [0]
		self.b1 ["font"] = ("Calibri", "9")
		self.b1 ["width"] = 30
		self.b1 ["command"] = lambda : self.chamar_pdf (self.nome[0])
		self.b1.pack ()

		self.b2 = Button (self.conteiner[2])
		self.b2 ["text"] = self.nome[1]
		self.b2 ["font"] = ("Calibri", "9")
		self.b2 ["width"] = 30
		self.b2 ["command"] = lambda : self.chamar_pdf (self.nome[1])
		self.b2.pack ()

		self.b3 = Button (self.conteiner[2])
		self.b3 ["text"] = self.nome[2]
		self.b3 ["font"] = ("Calibri", "9")
		self.b3 ["width"] = 30
		self.b3 ["command"] = lambda : self.chamar_pdf (self.nome[2])
		self.b3.pack ()



	#def ordednar_nota (self):
	
	def chamar_pdf (self, texto):

		self.secundario = Tk ()
		self.secundario.title ('PDF_INF')
		self.secundario.geometry ('1024x768')
		self.conteiner_s = []
		self.info = []
		self.glob = texto		
		

		self.conteiner_s.append (Frame (self.secundario))
		self.conteiner_s[0] ['pady'] = 10
		self.conteiner_s[0].pack ()

		
		
		self.pdf_info = Label (self.conteiner_s[0], text = "--> INFORMAÇÕES <--")
		self.pdf_info.pack ()			
		
		temp = ['nome', 'autor', 'editora', 'ano', 'tamanho', 'nota', 'comentario']

		for i in range (len(self.valores)):

			if (self.valores[i]['nome'] == texto):

				self.url = self.valores[i]['link']
				self.nota = self.valores[i]['nota']
				self.comentario = self.valores[i]['comentario']


				for j in self.chaves:

					
					if (self.qde_pdf[j]['nome'] == texto):	
					
						self.pdf_index = j
	

				for j in range (len(temp)):

					self.conteiner_s.append (Frame (self.secundario))
					self.conteiner_s[-1]['pady'] = 10
					self.conteiner_s[-1].pack ()

					#temp = list (self.valores[i].keys ())

					#print (temp[j], self.valores[i][temp[j]])

					self.info.append (Label (self.conteiner_s[-1], text = temp[j] + ': ' + self.valores[i][temp[j]]))
					self.info[-1].pack (side = LEFT)
				
		for i in range (3):			

			self.conteiner_s.append (Frame (self.secundario))
			self.conteiner_s[-1] ['pady'] = 10
			self.conteiner_s[-1].pack ()

		self.label_comentario = Label (self.conteiner_s[-3], text = "Comente: ")
		self.label_comentario.pack (side = LEFT)

		self.entrada_comentario = Entry (self.conteiner_s[-3])
		self.entrada_comentario ["width"] = 50
		self.entrada_comentario ["font"] = ("", "12")
		self.entrada_comentario.pack (side = LEFT)

		self.label_nota = Label (self.conteiner_s[-2], text = "Nota_avaliativa (0 - Ruim; 5 - Excelente): ")
		self.label_nota.pack (side = LEFT)

		self.entrada_nota = Entry (self.conteiner_s[-2])
		self.entrada_nota ["width"] = 5
		self.entrada_nota ["font"] = ("", "12")
		self.entrada_nota.pack (side = LEFT)

		self.linha = Label (self.conteiner_s[-2], text = "                       ")
		self.linha.pack (side = LEFT)

		self.inserir = Button (self.conteiner_s[-2])
		self.inserir ["text"] = 'INSERIR'
		self.inserir ["font"] = ("Calibri", "9")
		self.inserir ["width"] = 20
		self.inserir ["command"] = self.inserir_nota_comentario
		self.inserir.pack (side = LEFT)

		

		self.download = Button (self.conteiner_s[-1])
		self.download ["text"] = 'DOWNLOAD_PDF'
		self.download ["font"] = ("Calibri", "9")
		self.download ["width"] = 30
		self.download ["command"] = self.open_url
		self.download.pack ()		

		
		self.secundario.mainloop ()

	def inserir_nota_comentario (self):
		

		nota = (self.entrada_nota.get ())

		comentario = self.entrada_comentario.get ()
		'''
		nota = nota in ['0', '1', '2', '3', '4', '5']

		comentario = self.entrada_comentario.get ()

		if (nota == False):

			nota = self.nota
		
		else:

			nota = str ((float (nota) + float (self.nota)) / 2)	
		'''
		nota = str ((float (nota) + float (self.nota)) / 2)

		comentario = comentario + '-;-' + self.comentario    

		funct_firebase.update_nota_comentario ('python', self.pdf_index, nota, comentario)
		
		self.qde_pdf = funct_firebase.disp_pdf ('python')
		self.chaves = list (self.qde_pdf.keys ())
		self.valores = list (self.qde_pdf.values ())

		self.secundario.destroy ()

		self.conteiner_s.clear ()

		self.chamar_pdf (self.glob)
		
	def open_url (self):
	
		webbrowser.open_new (self.url)		


		
	
		


#pdf_python_firebase ()			


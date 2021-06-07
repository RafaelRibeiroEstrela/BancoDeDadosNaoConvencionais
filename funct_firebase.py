


import pyrebase as fb


def con ():

	config = {

	"apiKey": "AIzaSyDn8EdQC8mV9jiD4DaX1pSFCvAmZ7y_mxc",
    "authDomain": "bdnc-c070c.firebaseapp.com",
    "databaseURL": "https://bdnc-c070c.firebaseio.com",
    "storageBucket": "bdnc-c070c.appspot.com",
    "serviceAccount": "credencial.json"
	
	}


	conexao = fb.initialize_app(config)

	return (conexao)


def aut (email, senha):
	
	firebase = con ()

	auth = firebase.auth ()

	try:

		user = auth.sign_in_with_email_and_password (email, senha)

		return (True)
			
	except:
		
		return (False)

def disp_disciplinas ():

	firebase = con ()		

	db = firebase.database ()

	retrieve = db.child ('ic').child ('disciplinas').get ()

	lista = list (retrieve.val())

	return (lista)

def disp_pdf (disciplina):

	firebase = con ()

	db = firebase.database ()

	retrieve = db.child ('ic').child ('disciplinas').child (disciplina).get () 
	
	tupla = dict (retrieve.val ())

	return (tupla)

def ordenar ():

	firebase = con ()

	db = firebase.database ()

	retrieve = db.child ('ic').child ('disciplinas').child ('python').order_by_child('nota').get () 
	
	tupla = dict (retrieve.val ())

	return (tupla)

def update_nota_comentario (disciplina, pdf, nota, comentario):

	firebase = con ()

	db = firebase.database ()
		
	try:
		db.child ('ic').child ('disciplinas').child (disciplina).child (pdf).update ({'nota': nota})
		db.child ('ic').child ('disciplinas').child (disciplina).child (pdf).update ({'comentario': comentario})
		print ("SUCESSO")
	except:
		print ("FRACASSO")		

#print (ordenar ())

'''

firebase = con ()

auth = firebase.auth ()

try:
	user = auth.sign_in_with_email_and_password('usuario@teste.com', 'quake3arena')
except:
	print ("nao deu")

print ('deu')	

db = firebase.database ()

retrieve = db.child ('ic').child ('disciplinas').child ('python').get ()

tupla = dict(retrieve.val ())

print ('Quantidade de pdf armazenados', len(tupla))

'''


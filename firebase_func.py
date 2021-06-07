
from firebase_conect import con

#from login import *


#Função que faz a autenticação junto ao firebase

def aut (email, senha):
	
	firebase = con ()

	auth = firebase.auth ()

	try:

		user = auth.sign_in_with_email_and_password (email, senha)

		return (True)
			
	except:
		
		return (True)



#def chamar_dados (pdf):







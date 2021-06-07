#!/usr/bin/env python
# -*- coding: utf-8 -*-



import pyrebase as fb


# Função que conecta ao firebase

def con ():


	chamado = {
		
			"apiKey": "AIzaSyCAstMo2zJWckxY3ojmrW2SBFV0Z6gxHGs",
		    "authDomain": "bdnc-2019-2.firebaseapp.com",
		    "databaseURL": "https://bdnc-2019-2.firebaseio.com",
		    "projectId": "bdnc-2019-2",
		    "storageBucket": "bdnc-2019-2.appspot.com",
		    "messagingSenderId": "1084510086560",
		    "appId": "1:1084510086560:web:5499acbfbd62e3285230c5"


	}

	firebase = fb.initialize_app(chamado)

	return (firebase)


	







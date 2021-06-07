




#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tkinter import *
import disciplinas
import firebase_func

class logintk:
    
    def __init__(self):
        



        self.principal = Tk ()
        self.principal.title ('Login')
        self.principal.geometry ('800x600')
        
        self.ct1 = Frame () #Constroi os conteiners da janela
        self.ct1 ["pady"] = 10
        self.ct1.pack ()
        
        self.ct2 = Frame ()
        self.ct2 ["pady"] = 10
        self.ct2.pack ()

        self.ct3 = Frame ()
        self.ct3 ["pady"] = 10
        self.ct3.pack ()

        self.ct4 = Frame ()
        self.ct4 ["pady"] = 10
        self.ct4.pack ()

        self.ct5 = Frame ()
        self.ct5 ["pady"] = 10
        self.ct5.pack ()  

        self.login = Label (self.ct1, text = "--> LOGIN <--")
        self.login.pack ()
        
        
        self.email = Label (self.ct2, text = "E-mail ")
        self.email.pack (side = LEFT)

        self.entrada_email = Entry (self.ct2)
        self.entrada_email ["width"] = 30
        self.entrada_email ["font"] = ("", "12")
        self.entrada_email.pack (side = LEFT)

        self.senha = Label (self.ct3, text = "Senha")
        self.senha.pack (side = LEFT)
        
        self.entrada_senha = Entry (self.ct3, show = '*')
        self.entrada_senha ["width"] = 30
        self.entrada_senha ["font"] = ("", "12")
        self.entrada_senha.pack (side = LEFT)


        self.autenticar = Button (self.ct4)
        self.autenticar ["text"] = "autenticar"
        self.autenticar ["font"] = ("Calibri", "9")
        self.autenticar ["width"] = 20
        self.autenticar ["command"] = self.chamar_aut #Chama a função "chamar_aut"
        self.autenticar.pack (side = LEFT)

        self.principal.mainloop()

        


    def chamar_aut (self):
        
        ch = firebase_func.aut (self.entrada_email.get (), self.entrada_senha.get ()) #chama a função aut do outro arquivo com os paramentros de email e senha inseridos

        if (ch == False):
            
            self.ct5.destroy ()

            self.ct5 = Frame ()
            self.ct5 ["pady"] = 10
            self.ct5.pack ()  
            
            self.falha_aut = Label (self.ct5, text = "Falha na autenticação. Repita o procedimento.")
            self.falha_aut.pack (side = LEFT)

        else:
            
            self.principal.destroy ()

            
            disciplinas.disciplinastk ()        



logintk ()




import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credencial = credentials.Certificate ('certificado.json')

firebase_admin.initialize_app (credencial)

db = firestore.client ()

colect = db.collection (u'ic')

documento = colect.stream ()

for d in documento:

	print (u'{} => {}'.format (d.id, d.to_dict ()))

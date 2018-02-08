import firebase_admin
#Authentication
from firebase_admin import credentials
#Database
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/home/ubuntu/workspace/firebase/adminkey.json.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://handbook-26031.firebaseio.com/'
})

ref = db.reference('/private/testConnection')
print(ref.get())
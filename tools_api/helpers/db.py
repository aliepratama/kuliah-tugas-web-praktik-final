from supabase import create_client, Client
from dotenv import load_dotenv
import os, firebase_admin
from firebase_admin import db

load_dotenv()
supabase = create_client(os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY"))

cred_obj = firebase_admin.credentials.Certificate('./auth/zimo-tools-104a99f0deaa.json')
firebase = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': os.environ.get("FIREBASE_URL")
})
frbs_ref_history = lambda x : db.reference(f"/history/{x}")
# frbs_ref_history.set({"history": -1})

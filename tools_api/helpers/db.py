from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()
supabase = create_client(os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY"))
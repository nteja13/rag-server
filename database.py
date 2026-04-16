import os
from supabase import create_client,Client
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.getenv("SUPABASE_API_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_KEY")

if not supabase_url or not supabase_key:
    raise ValueError("Missing Supabase credential in the environment variables")

supabase : Client = create_client(supabase_url,supabase_key)
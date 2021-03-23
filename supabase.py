import os
from supabase_py import create_client, Client


url = "https://feeylixypghiumtqiuco.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYxNDg5OTM4OSwiZXhwIjoxOTMwNDc1Mzg5fQ.-s5U5KCAkc-WaWAzjD3qZoSxCNOpxYZ7vjQ_HaGfF3Q"

# url: str = os.environ.get("SUPABASE_URL")
# key: str = os.environ.get("SUPABASE_KEY")
email = "abcdde@gmail.com"
password = "password"
supabase: Client = create_client(url, key)


savedImages = supabase.from('Profile')
  .select("
    email,
    images,
  ")
print(savedImages)
import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="your_supabase_password",
        host="mfusnfwxtnzzbmalklqw.supabase.co",
        port="5432"
    )
    print("✅ Connection successful!")
    conn.close()
except Exception as e:
    print("🚨 Connection failed:", e)

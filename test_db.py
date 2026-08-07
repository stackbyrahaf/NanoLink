from app.databse import engine

try:
    connection = engine.connect()
    print("Connection to the database was successful!")
    connection.close()
except Exception as e:
    print(f"Failed to connect to the database: {e}")
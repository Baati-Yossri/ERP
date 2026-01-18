from fastapi import FastAPI
import psycopg2

app = FastAPI()

# Connect to the School database
conn = psycopg2.connect(
    dbname="ERP",
    user="postgres",
    password="",
    host="localhost",
    port=""
)

@app.get("/")
def home():
    return {"message": "ERP backend running"}

@app.get("/users")
def recuperer_users():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return users

@app.post("/users")
def ajouter_user(user: dict):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (user['name'], user['email']))
    conn.commit()
    cursor.close()
    return {"message": "User added successfully"}
@app.get("/users/{id}")
def recuperer_user(id:int):
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=%s",(id,))
    user=cursor.fetchone()
    if user:
        cursor.close()
        return user
    else:
        cursor.close()
        return {"message": "user not found"}
@app.put("/users/{id}")
def modifier_user(id:int,user:dict):
    cursor=conn.cursor()
    cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s",(user["name"],user["email"],id))
    conn.commit()
    cursor.close()
    return {"message": "user updated successfully"}
@app.delete("/users/{id}")
def supprimer_user(id:int):
    cursor=conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s",(id,))
    conn.commit()
    cursor.close()
    return {"message": "user deleted successfully"}
  
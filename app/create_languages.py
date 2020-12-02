en= {
    "title":"what year will you turn 100?", 
    "age":"Enter your age",
    "compute": "start calculation",
    "result": "You will turn 100 years old in: ",
    }

fr= {
    "title":"Quand aurez vous 100 ans", 
    "age":"Entrez votre age",
    "compute": "lancer le calcul",
    "result": "vous aurez 100 ans en: ",
    }

fi= {
    "title":"what year will you turn 100?FI ", 
    "age":"Enter your ageFI ",
    "compute": "start calculation FI",
    "result": "You will turn 100 years old in: FI ",
    }

se= {
    "title":" ", 
    "age":"Enter your ageFI ",
    "compute": "start calculation FI",
    "result": "You will turn 100 years old in: FI ",
    }






import sqlite3
conn = sqlite3.connect("language.db")
c = conn.cursor()

c.execute("""
 CREATE TABLE IF NOT EXISTS
 english(title text, age text, compute text, result text)
 """)

c.execute("""
 CREATE TABLE IF NOT EXISTS
 french(title text, age text, compute text, result text)
 """)

c.execute("""
 CREATE TABLE IF NOT EXISTS
 finnish(title text, age text, compute text, result text)
 """)

c.execute("INSERT INTO english VALUES (:title, :age, :compute, :result)", en)

c.execute("INSERT INTO french VALUES (:title, :age, :compute, :result)", fr)

c.execute("INSERT INTO finnish VALUES (:title, :age, :compute, :result)", fi)

conn.commit()
conn.close

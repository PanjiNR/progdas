from flask import Flask, render_template, request, redirect, url_for
from hitung import kalkulasi_statistik
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'statistik_db' 
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    error = None
    nama_kelompok = ""

    if request.method == "POST":
        nama_kelompok = request.form.get("namaKel", "")
        pendapatan_raw = request.form.get("pendapatan", "")
        try:
            data_pendapatan = [float(x.strip()) for x in pendapatan_raw.split(",") if x.strip()]
            hasil = kalkulasi_statistik(data_pendapatan)
            
            conn = get_db_connection()
            cursor = conn.cursor()
            
            query = """
                INSERT INTO hasil_statistik (nama_kelompok, rata_rata, tertinggi, terendah, gini)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (
                nama_kelompok, 
                hasil['rata_rata'], 
                hasil['tertinggi'], 
                hasil['terendah'], 
                hasil['gini']
            )
            
            cursor.execute(query, values)
            conn.commit() 
            cursor.close()
            conn.close()
        except ValueError:
            error = "Data tidak valid"
        except mysql.connector.Error as err:
            error = f"Database Error: {err}"

    return render_template("index.html", hasil=hasil, nama_kelompok=nama_kelompok, error=error)

@app.route("/riwayat")
def riwayat():
    try:
        conn = get_db_connection()
        # Use dictionary=True so we can access columns by name in HTML
        cursor = conn.cursor(dictionary=True)
        
        # Select the data from your MySQL table
        cursor.execute("SELECT * FROM hasil_statistik ORDER BY created_at DESC")
        results = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return render_template("riwayat.html", data_history=results)
    except Exception as e:
        return f"Database Error: {e}"

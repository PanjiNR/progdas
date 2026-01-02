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
                INSERT IGNORE INTO hasil_statistik (nama_kelompok, rata_rata, tertinggi, terendah, gini)
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
    
@app.route("/banding", methods=["GET", "POST"])
def banding():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    hasil_banding = None
    
    cursor.execute("SELECT id, nama_kelompok, gini FROM hasil_statistik")
    daftar_kelompok = cursor.fetchall()
    
    if request.method == "POST":
        id1 = request.form.get("pilihan1")
        id2 = request.form.get("pilihan2")

        if id1 and id2:
            cursor.execute("SELECT * FROM hasil_statistik WHERE id IN (%s, %s)", (id1, id2))
            items = cursor.fetchall()

            if len(items) == 2:
                d1_data = items[0] if str(items[0]['id']) == str(id1) else items[1]
                
            
                d2_data = items[0] if str(items[0]['id']) == str(id2) else items[1]

                if d1_data['gini'] < d2_data['gini']:
                    pesan = f"{d1_data['nama_kelompok']} memiliki pemerataan pendapatan yang lebih baik dari {d2_data['nama_kelompok']}"
                elif d2_data['gini'] < d1_data['gini']:
                    pesan = f"{d2_data['nama_kelompok']} memiliki pemerataan pendapatan yang lebih baik dari {d1_data['nama_kelompok']}"
                else:
                    pesan = "Kedua kelompok memiliki tingkat pemerataan yang sama."

 
                hasil_banding = {
                    'pesan': pesan,
                    'd1': d1_data,
                    'd2': d2_data
                }
    
    cursor.close()
    conn.close()
    return render_template("banding.html", kelompok_list=daftar_kelompok, hasil=hasil_banding)

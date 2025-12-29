from flask import Flask, render_template, request
from hitung import kalkulasi_statistik

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Ambil data dari form, ubah string menjadi list angka
        input_user = request.form.get('pendapatan')
        try:
            list_pendapatan = [float(x.strip()) for x in input_user.split(',')]
            hasil = kalkulasi_statistik(list_pendapatan)
            return render_template('hasil.html', hasil=hasil, data_asli=list_pendapatan)
        except ValueError:
            return "Input tidak valid! Gunakan angka dan pisahkan dengan koma."
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
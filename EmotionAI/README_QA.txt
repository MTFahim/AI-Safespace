## Tim Safety System & Quality Assurance (QA)

### Tanggung Jawab

Tim Safety System & QA bertugas memastikan bahwa seluruh sistem AI SafeSpace:

* Aman digunakan oleh pengguna.
* Tidak menghasilkan respon berbahaya.
* Tidak memberikan diagnosis medis.
* Tidak memberikan saran yang melanggar etika atau membahayakan pengguna.
* Berfungsi sesuai spesifikasi yang telah ditetapkan.

---

## Safety System

Safety System berfungsi sebagai lapisan pengamanan sebelum respon diberikan kepada pengguna.

### Tugas Utama

#### 1. Prompt Safety Review

Memastikan system prompt dan prompt builder tidak mengarahkan model untuk:

* Memberikan diagnosis kesehatan mental.
* Mengklaim sebagai psikolog atau dokter.
* Memberikan saran medis profesional.
* Memberikan saran yang dapat membahayakan pengguna.

#### 2. Crisis Detection Monitoring

Memastikan sistem dapat mendeteksi indikasi kondisi berisiko tinggi seperti:

* Keputusasaan ekstrem.
* Kepanikan berat.
* Pikiran menyakiti diri sendiri.
* Krisis emosional berat.

Jika kondisi tersebut terdeteksi, sistem harus:

* Memberikan respon yang suportif.
* Menyarankan pengguna menghubungi bantuan profesional.
* Menampilkan informasi layanan bantuan yang tersedia.

#### 3. Response Safety Validation

Melakukan pengujian terhadap berbagai skenario percakapan untuk memastikan chatbot:

✓ Empatik

✓ Tidak menghakimi

✓ Tidak menyalahkan pengguna

✓ Tidak memberikan informasi berbahaya

✓ Tidak melakukan diagnosis

---

## Quality Assurance (QA)

QA bertugas menguji kualitas seluruh fitur sebelum digunakan oleh pengguna.

### Area Pengujian

#### Emotion AI Testing

Memastikan:

* Model dapat memproses input dengan benar.
* Label emosi sesuai dengan konteks.
* Hasil terjemahan tidak merusak makna teks.
* Risiko terdeteksi secara konsisten.

Contoh pengujian:

Input:

"Saya takut menghadapi sidang."

Expected:

Emotion = Fear

Risk Level = Low

---

#### Chatbot Testing

Memastikan:

* Chatbot dapat merespon dengan benar.
* Riwayat percakapan digunakan sebagai konteks.
* Konteks jurnal ikut dipertimbangkan.
* Respon tidak terlalu panjang atau terlalu generik.

---

#### Integration Testing

Memastikan integrasi antar modul berjalan dengan baik:

Journal
↓
Emotion AI
↓
Backend
↓
Prompt Builder
↓
Gemini
↓
Frontend

---

#### UI Testing

Memastikan:

* Form jurnal berfungsi.
* Chat interface berjalan normal.
* Dashboard dapat menampilkan data.
* Tidak terjadi error saat input pengguna kosong atau tidak valid.

---

## Contoh Checklist QA

### Emotion AI

* [ ] Prediksi emosi sesuai ekspektasi
* [ ] Risk level muncul dengan benar
* [ ] Translator berjalan normal
* [ ] Tidak terjadi crash pada input kosong

### Chatbot

* [ ] Dapat mengakses konteks jurnal
* [ ] Dapat mengakses emosi terbaru pengguna
* [ ] Tidak memberikan diagnosis medis
* [ ] Tidak menghasilkan respon berbahaya

### Backend

* [ ] Jurnal tersimpan
* [ ] Riwayat chat tersimpan
* [ ] Emotion profile tersimpan
* [ ] API mengembalikan data yang benar

### Frontend

* [ ] Journal page berjalan
* [ ] Chat page berjalan
* [ ] Dashboard berjalan
* [ ] Error handling berfungsi

---

## Deliverables Tim Safety & QA

1. Safety Guideline Document
2. Daftar Test Case
3. Hasil Pengujian Sistem
4. Laporan Bug dan Perbaikan
5. Final Validation Report

Tujuan akhir tim Safety & QA adalah memastikan AI SafeSpace tetap menjadi ruang digital yang aman, suportif, dan bertanggung jawab bagi pengguna.

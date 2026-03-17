# Tugas Backtracking: N-Queen Problem 

**Mata Kuliah:** Algoritma dan Pemrograman  
**Dosen Pengampu:** Arseto Satriyo Nugroho  

## Identitas Mahasiswa
* **Nama:** Faras Fauzan Attaqi
* **NIM:** 21120124140119
* **Program Studi:** Teknik Komputer
* **Universitas:** Universitas Diponegoro  

---

## 1. Deskripsi Masalah
Tugas ini mengimplementasikan algoritma Backtracking untuk menyelesaikan masalah **N-Queen Problem**. Tujuannya adalah meletakkan sejumlah N bidak ratu pada papan catur berukuran NxN[cite: 448]. 
Batasan (*constraint*) utama dari permasalahan ini adalah semua bidak ratu tidak boleh bisa memakan dengan 1 langkah. Secara spesifik:
* Satu kolom tidak boleh lebih dari satu bidak ratu.
* Satu baris tidak boleh lebih dari satu bidak ratu.
* Diagonal tidak boleh berisi lebih dari satu bidak ratu.

## 2. Penjelasan Logika Algoritma
Penyelesaian masalah dilakukan menggunakan teknik Backtracking, yaitu mencari solusi secara *incremental* (satu per satu) dan meng-eliminasi solusi yang tidak sesuai dengan kondisi batasan. Logika berjalannya program:
1. Program mengecek apakah semua bidak ratu (N) sudah diletakkan. Jika ya, sudahi program.
2. Jika belum, mulai dari kiri atas, cek apakah aman untuk diletakkan bidak ratu.
3. Jika aman, letakkan ratu dan geser ke baris selanjutnya. Jika tidak aman, geser ke kolom selanjutnya.
4. Jika tidak ada jalan yang aman, berhenti, tandai cabang ini sebagai *unsolved*, dan lanjutkan untuk cabang yang lain ke langkah pertama (Proses *Backtrack*).

## 3. Pseudocode Algoritma

```text
FUNGSI Selesaikan_N_Queen(baris):
    JIKA semua ratu sudah diletakkan (baris == N):
        KEMBALIKAN Benar (Solusi valid ditemukan)

    UNTUK setiap kolom dari 0 sampai N-1:
        JIKA posisi (baris, kolom) aman dari ancaman:
            Letakkan Ratu di (baris, kolom)

            JIKA Selesaikan_N_Queen(baris + 1) bernilai Benar:
                KEMBALIKAN Benar

            Tarik kembali Ratu dari (baris, kolom) // Proses Backtrack

    KEMBALIKAN Salah

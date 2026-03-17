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
[cite_start]Tugas ini mengimplementasikan algoritma Backtracking untuk menyelesaikan masalah **N-Queen Problem**[cite: 425]. [cite_start]Tujuannya adalah meletakkan sejumlah N bidak ratu pada papan catur berukuran NxN[cite: 448]. 

[cite_start]Batasan (*constraint*) utama dari permasalahan ini adalah semua bidak ratu tidak boleh bisa memakan dengan 1 langkah[cite: 450]. Secara spesifik:
* [cite_start]Satu kolom tidak boleh lebih dari satu bidak ratu[cite: 452].
* [cite_start]Satu baris tidak boleh lebih dari satu bidak ratu[cite: 454].
* [cite_start]Diagonal tidak boleh berisi lebih dari satu bidak ratu[cite: 456].

## 2. Penjelasan Logika Algoritma
[cite_start]Penyelesaian masalah dilakukan menggunakan teknik Backtracking, yaitu mencari solusi secara *incremental* (satu per satu) dan meng-eliminasi solusi yang tidak sesuai dengan kondisi batasan[cite: 320]. Logika berjalannya program:
1. [cite_start]Program mengecek apakah semua bidak ratu (N) sudah diletakkan[cite: 458]. [cite_start]Jika ya, sudahi program[cite: 461].
2. [cite_start]Jika belum, mulai dari kiri atas, cek apakah aman untuk diletakkan bidak ratu[cite: 463, 465].
3. [cite_start]Jika aman, letakkan ratu dan geser ke baris selanjutnya[cite: 467]. [cite_start]Jika tidak aman, geser ke kolom selanjutnya[cite: 468].
4. [cite_start]Jika tidak ada jalan yang aman, berhenti, tandai cabang ini sebagai *unsolved*, dan lanjutkan untuk cabang yang lain ke langkah pertama (Proses *Backtrack*)[cite: 473].

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

import time
import os

def clear_screen():
    # Membersihkan layar terminal agar animasi terlihat rapi
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board, N, step, message):
    clear_screen()
    print(f"--- N-QUEEN PROBLEM ({N}x{N}) ---")
    print(f"Langkah ke-{step}: {message}\n")
    
    for row in board:
        print(" ".join(row))
    print("\n" + "="*30)
    time.sleep(0.5)  # Jeda 0.5 detik untuk efek visualisasi

def is_safe(board, row, col, N):
    # Cek kolom ke atas
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Cek diagonal kiri atas
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Cek diagonal kanan atas
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_n_queen_util(board, row, N, step_counter):
    # Basis: Jika semua ratu (N) sudah diletakkan, kembalikan True
    if row >= N:
        return True

    for col in range(N):
        # Cek apakah aman untuk diletakkan bidak ratu
        if is_safe(board, row, col, N):
            # Letakkan ratu
            board[row][col] = 'Q'
            step_counter[0] += 1
            print_board(board, N, step_counter[0], f"Mencoba letakkan Ratu di Baris {row}, Kolom {col}")

            # Geser ke baris selanjutnya
            if solve_n_queen_util(board, row + 1, N, step_counter):
                return True

            # Backtracking: Jika tidak ada solusi, tandai sebagai unsolved dan tarik ratu
            board[row][col] = '.'
            step_counter[0] += 1
            print_board(board, N, step_counter[0], f"BACKTRACK! Menarik Ratu dari Baris {row}, Kolom {col}")

    # Geser ke kolom selanjutnya jika tidak aman
    return False

def solve_n_queen(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    step_counter = [0]
    
    print("Memulai pencarian solusi...")
    time.sleep(1)
    
    if solve_n_queen_util(board, 0, N, step_counter) == False:
        print("Solusi tidak ditemukan!")
    else:
        print(f"Solusi DITEMUKAN dalam {step_counter[0]} langkah!")
        
if __name__ == "__main__":
    # Kamu bisa mengganti N dengan 4 atau 8. 
    # N=4 sangat disarankan untuk presentasi video karena lebih singkat.
    N_SIZE = 4
    solve_n_queen(N_SIZE)
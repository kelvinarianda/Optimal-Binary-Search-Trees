def jumlah_frekuensi(frekuensi, awal, akhir):
    return sum(frekuensi[awal:akhir+1])

def optimal_bst(kunci, frekuensi):
    n = len(kunci)
    biaya = [[0] * n for _ in range(n)]
    akar = [[0] * n for _ in range(n)]
    
    for i in range(n):
        biaya[i][i] = frekuensi[i]
        akar[i][i] = i
    
    for panjang in range(2, n+1):
        for i in range(n - panjang + 1):
            j = i + panjang - 1
            biaya[i][j] = float('inf')
            
            for r in range(i, j + 1):
                kiri = biaya[i][r-1] if r > i else 0
                kanan = biaya[r+1][j] if r < j else 0
                total_biaya = kiri + kanan + jumlah_frekuensi(frekuensi, i, j)
                
                if total_biaya < biaya[i][j]:
                    biaya[i][j] = total_biaya
                    akar[i][j] = r
    
    return biaya, akar

# Contoh penggunaan
kunci = [10, 20, 30, 40]
frekuensi = [4, 2, 6, 3]
biaya, akar = optimal_bst(kunci, frekuensi)
print("Matriks Biaya:")
for baris in biaya:
    print(baris)
print("Matriks Akar:")
for baris in akar:
    print(baris)
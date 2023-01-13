# ada sebuah array berisi deret matematika
# contoh disini ada 6 angka

# 6
# -4 3 -9 0 4 1

# proporsi dari angka positif adalah 0.5
# proporsi dari angka negatif adalah 0.333333
# proporsi dari angka 0 adalah 0.166667

def klasifikasi(arr):
    awal = 0
    pos = 0
    neg = 0
    nol = 0
    for i in arr:
        if i < 0:
            neg += 1
            awal += 1
        elif i == 0:
            nol += 1
            awal += 1
        elif i > 0:
            pos += 1
            awal += 1
        
    ProPos = pos/awal
    ProNeg = neg/awal
    ProNol = nol/awal

    return ProPos, ProNeg, ProNol

print(klasifikasi([1, 0, 3, -4, -7, 8]))
print("-"*100)
# Hitunglah sebuah nilai di arr yang merupakan angka yang habis di bagi 3
# 6 
# 1 3 2 6 1 2

# jawaban 5

# explanation
# (0,2) -> ar[0] + ar[2] = 1 + 2 = 3
# (0,5) -> ar[0] + ar[5] = 1 + 2 = 3
# (1,3) -> ar[1] + ar[3] = 3 + 6 = 3
# (2,4) -> ar[2] + ar[4] = 2 + 1 = 3
# (4,5) -> ar[4] + ar[5] = 1 + 2 = 3

def hitung(x, arr):
    jwb = 0
    for i in range(len(arr)-1):
       for j in range(i+1, len(arr)):
        if (arr[i] + arr[j]) % x ==0:
            jwb += 1
    return "jawaban", jwb,

print(hitung(3, [1, 2, 3, 5, 7, 8]))
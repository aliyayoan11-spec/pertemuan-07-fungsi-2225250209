def luas_persegi_panjang(p, l):
    return p * l

def luas_segitiga(a, t):
    return 0.5 * a * t

def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

def tampilkan_menu():
    print("=== PROGRAM UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")

# Program Utama
tampilkan_menu()
pilihan = input("Masukkan pilihan (1-4): ")

if pilihan == "1":
    p = float(input("Panjang: "))
    l = float(input("Lebar: "))
    print(f"Luas Persegi Panjang = {luas_persegi_panjang(p, l)}")
elif pilihan == "2":
    a = float(input("Alas: "))
    t = float(input("Tinggi: "))
    print(f"Luas Segitiga = {luas_segitiga(a, t)}")
elif pilihan == "3":
    n = int(input("Masukkan nilai n: "))
    if n >= 0:
        print(f"Jumlah 1 sampai {n} = {jumlah_n(n)}")
    else:
        print("Nilai n harus berupa bilangan bulat nonnegatif.")
elif pilihan == "4":
    n = int(input("Masukkan nilai n: "))
    if n >= 0:
        print(f"Faktorial dari {n} = {faktorial(n)}")
    else:
        print("Nilai n harus berupa bilangan bulat nonnegatif.")
else:
    print("Pilihan menu tidak valid!")
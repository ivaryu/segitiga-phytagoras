print("="*15, "POST TEST", "="*15)
print("\t","Rumus Segitiga Phytagoras")

username = (input("Nama     = "))
nim      = int(input("NIM      = "))
angkatan = input("Angkatan = ")

print("Selamat datang!")

print("\n","-"*30)
print("Segitiga")
print("1. Keliling")
print("2. Luas")
print("3. Tinggi")
print("4. Alas")
print("5. Keluar")
rumus = int(input("Mau Menghitung Apa? = "))

if rumus==1:
    print("Masukkan Angka")
    bil1 = int(input("Sisi Miring   = "))
    bil2 = int(input("Alas Segitiga = "))
    keliling = ((2*bil1)+bil2)
    print(f"Keliling Segitiganya {keliling}")
elif rumus==2:
    print("Masukkan Angka")
    bil1 = int(input("Tinggi        = "))
    bil2 = int(input("Alas Segitiga = "))
    luas = ((bil2/2)*bil1)
    print(f"Keliling Segitiganya {luas}")
elif rumus==3:
    print("Masukkan Angka")
    bil1 = int(input("Luas          = "))
    bil2 = int(input("Alas Segitiga = "))
    tinggi = ((2*bil1)/bil2)
    print(f"Keliling Segitiganya {tinggi}")
elif rumus==4:
    print("Masukkan Angka")
    bil1 = int(input("Luas          = "))
    bil2 = int(input("Tinggi        = "))
    tinggi = ((2*bil1)/bil2)
    print(f"Keliling Segitiganya {tinggi}")
elif rumus==5:
    print("Anda keluar dari program")
print("\n")
print("Program Selesai")
    

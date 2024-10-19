import os
import random
import string
os.system("cls")# Win
print(f"{'Data Tentara ':-^50}")
data = dict()
while True:
    Kunci = "".join(random.choice(string.ascii_uppercase)for i in range(3))
    print(f"Kunci = {Kunci}")
    nama = input("Nama\t:")
    Tinggi_Badan = input("Tinggi Badan\t:")
    Berat_Badan = input("Berat Badan\t:")
    Jawaban = input("Siapa Yang Mau Ikut Tentara Lagi Iya atau Tidak ").lower()
    data[Kunci] = {'Nama':nama, 'Tinggi Badan':Tinggi_Badan,'Berat Badan': Berat_Badan }
    if Jawaban == 't':
        break
    elif Jawaban == 'y':
        continue
    

print("-"*40)
print(f"Key\t Nama\t Tinggi Badan\t Berat Badan")
print("-"*40)
for k,v in data.items():
    print(f"{Kunci}.\t{data[Kunci]['Nama']}\t {data[Kunci]['Tinggi Badan']}\t \t{data[Kunci]['Berat Badan']}")
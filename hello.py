print('-----Nomor satu-----')

Kendaraan=["Yamaha NMAX","Motor","155","hitam","dua"]
Kendaraan.append("30 Juta")
Kendaraan.append("NMAX")
Kendaraan.insert(2,"Honda")
print(Kendaraan)

print('-----Nomor Dua-----')

rumus=int(input("rumus apa yang kamu kerjakan:"))
match rumus:
    case 1 :
        print("luas persegi (sisi*sisi)")
        sisi1=float (input("masukkan sisi 1:"))
        sisi2=float (input("masukkan sisi 2:"))
        luas_persegi= sisi1*sisi2
        print("luasnya adalah",int(luas_persegi))
    case 2:
        print("luas.lingkaran (3.14.*r*r)")
        phi=3.14
        r= float(input("masukkan jari-jari: "))
        luas_lingkaran = phi*r*r
        print("luasnya adalah",int(luas_lingkaran))
    case 3:
        print("luas segitiga (0,5*a*t)")
        setengah =0.5
        a = float(input("masukkan alas: "))
        t = float(input("masukkan tinggi: "))
        luas_segitiga = setengah*a*t
        print("luasnya adalah",int(luas_segitiga))
    case _ :
        print("salahpilih angka")
        
        


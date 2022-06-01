def paket_Harga():
    print("Selamat Datang Di Warnet Bianglala")
    print("")
    print("========== Daftar Harga ==========")
    print("")
    print("1. Kelas Regular")
    print("2. Kelas VIP")
    print("3. Keluar")
paket_Harga()
pilih = int(input("Kelas yang dipilih: "))
if pilih == 1 :
    print("")
    print("----------------------------------")
    Nama = input("Nama: ")
    print("Kelas Regular\nHarga 1 Jam = Rp.5000")
    jumlah = int(input("Lama waktu bermain (dalam jam):"))
    PW = 5*2112
    print ("")
    print("")
    total = jumlah*5000
    print ("Total Harga : Rp",total)
    print("----------------------------------")
    print("         CV. Sukses Sendiri       ")
    print("       Jln. Bianglala NO. 13      ")
    print("==================================")
    print("User ID:",Nama)
    print("Password:", PW)
    print ("")
    print ("========== Terima Kasih ==========")
elif pilih == 2 :
    print("")
    print("----------------------------------")
    Nama = input("Nama: ")
    print("Kelas VIP\nHarga 1 Jam = Rp.8000")
    jumlah = int(input("Lama waktu bermain (dalam jam):"))
    PW = 10*2112
    print ("---------------------------------")
    print("")
    total = jumlah*8000
    print ("Total yang harus dibayar: Rp",total)
    print("----------------------------------")
    print("         CV. Sukses Sendiri       ")
    print("      Jln. Bianglala NO. 13       ")
    print("==================================")
    print("User ID:",Nama)
    print("Password:", PW)
    print ("")
    print ("========== Terima Kasih ==========")
elif pilih == 3 :
    exit 
else:
    exit
 

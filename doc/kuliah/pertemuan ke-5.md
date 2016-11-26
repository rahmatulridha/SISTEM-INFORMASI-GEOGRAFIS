# Membuat dan Mengedit Data Geospasial

# A. Membuat Data Geospasial 
Pembutan data geospasial ini menggunakan Library Pyshp.
kita akan membuat file baru bernama anu.shp beserta anu.dbf. 
Contoh : 
1. Import shapefile
2. Instansiasi writer method
    Sf = shapefile.Writed (param). 
   Dimana param adalah pilih : 
   a. shapeType = 1
   b. shapeType = 3
   c. shapeType = 5
3. Sama seperti rend kita lakukan metode shp dan dbf.

# - SHP
Untuk menambahkan record tambah tergantung type ESRInya:
1.	Sf.point(x,y)
2.	Sf.line = (parts = [ [x,y], [z,w], ... ] )
3.	Sf.poly = (parts = [ [x,y],[z,w], ... ] )

# -	DBF
Tahapannya adalah segabai berikut :
1.	Membuat atribut dahulu, kemudian menambahkan record adalah 
    Sf.field (‘nama+file’, ‘c’, ‘40’)
   Artinya nama atribuut nama field dengan 40 karakter.
2.	Untuk menambahkan record
    Sf.record(‘Bandung’)
    Sf.record ‘Bandung’, ‘sarijadi’)
3. Setelah selesai maka simpan, dengan perintah :
    Sf.save(‘namafile.shp’)

# B. Editing 
Adapun dalam editing data geospasial hampir sama dengan langkah-langkah 
membuat data geospasial, yang membedakan adalah : 
    Sf.shapefile.Editor (param)
   Dimana param adalah nama attau letak file.
Contohnya :
	Sf.shapefile.Editing(shapefile =”warteg.shp”)

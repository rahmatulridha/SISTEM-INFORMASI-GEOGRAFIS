# RETRIEVE DATA GEOSPASIAL

# 
Retrieve Data yaitu memperoleh data dari sistem manajemen 
database seperti ODBMS. Dalam hal ini, dianggap bahwa data 
yang diwakili dengan cara yang terstruktur, dan tidak ada 
ambiguitas dalam data.

# 
Meretrieve Data Vektor bisa menggunakan :
-	Data Shape File .shp yaitu operasi retireve data yang menggunakan 
Library Python yang bernama pyshp.
-	Shapefile (Standar File) yaitu geospasial dari data yang dikeluarkan 
oleh ESRI. Shapefile terbagi menjadi 2 yaitu :
   •	.shp (data geometri)
   •	.dbf (tabel basis data)

# 
Geometri adalah data kordinat yang membentuk bagun datar atau bangun 
ruang. Diantaranya :
1.	Point / titik [1]
2.	Line / garis [3]	
3.	Poligon [5]

# 
Proses pengambilan data bisa menggunakan :
-	Library pyshp, class shapefile
  1.	Buka atau baca 

# 
Method dari SHP  (akses menggunakan method) :
-	Shapes() – menampilkan semua
-	Shape (n) – menampilkan dengan parameter yang terdiri dari ;
•	Bbox (bonding box) merupakan batas view peta.
•	Points adalah kordinat pembentuk peta.
•	Parts  itu apakah record ini bagian dari record lain atau precahan relasi.
•	Shapetype adalah jenis geometri dari points.

# 
Method dari DBF ( akses menggunakan [] ) :
•	Fields – nama fields
•	Record(n) – baris ke 
•	Records() – semua isi tabel
*n = nomor sequence record

# 
Membuat Class pada Retrieve di editor
<p align="center">
   <img src="../../img/tugasrahma-py.jpg"></p>

# 
Menampilkan Select Negara
<p align="center">
   <img src="../../img/tugasrahma-pyc.jpg"></p>

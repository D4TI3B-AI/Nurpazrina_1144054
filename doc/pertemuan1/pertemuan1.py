import time
mulai_waktu = time.time()
print("Menghitung (Jumlah Perhitungan)")
x = raw_input("Masukan angka x : ")
y = raw_input("Masukan angka y : ")
a = raw_input("masukan angka a : ")
b = raw_input("Masukan angka b : ")
c = raw_input("Masukan angka c : ")
if x == 'satu':
	x=1
if x == 'dua':
	x=2
if x == 'tiga':
	x=3
if x == 'empat':
	x=4
if x == 'lima':
	x=5
if x == 'enam':
	x=6
if x == 'tujuh':
	x=7
if x == 'delapan':
	x=8
if x == 'sembilan':
	x=9
if x == 'nol':
	x=0

if y == 'satu':
	y=1
if y == 'dua':
	y=2
if y == 'tiga':
	y=3
if y == 'empat':
	y=4
if y == 'lima':
	y=5
if y == 'enam':
	y=6
if y == 'tujuh':
	y=7
if y == 'delapan':
	y=8
if y == 'sembilan':
	y=9
if y == 'nol':
	y=0

if a == 'satu':
	a=1
if a == 'dua':
	a=2
if a == 'tiga':
	a=3
if a == 'empat':
	a=4
if a == 'lima':
	a=5
if a == 'enam':
	a=6
if a == 'tujuh':
	a=7
if a == 'delapan':
	a=8
if a == 'sembilan':
	a=9
if a == 'nol':
	a=0

if b == 'satu':
	b=1
if b == 'dua':
	b=2
if b == 'tiga':
	b=3
if b == 'empat':
	b=4
if b == 'lima':
	b=5
if b == 'enam':
	b=6
if b == 'tujuh':
	b=7
if b == 'delapan':
	b=8
if b == 'sembilan':
	b=9
if b == 'nol':
	b=0

if c == 'satu':
	c=1
if c == 'dua':
	c=2
if c == 'tiga':
	c=3
if c == 'empat':
	c=4
if c == 'lima':
	c=5
if c == 'enam':
	c=6
if c == 'tujuh':
	c=7
if c == 'delapan':
	c=8
if c == 'sembilan':
	c=9
if c == 'nol':
	c=0
Jumlah = (x*a)+(b/c)-y
print("Jumlah Perhitungan", Jumlah)
print("Waktu Menghitung : %s detik " % (time.time() - mulai_waktu))
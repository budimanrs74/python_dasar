# ANGKA_KONSTANTA = 12
# print(ANGKA_KONSTANTA)

# ANGKA_KONSTANTA = 10
# print(ANGKA_KONSTANTA)

name_variable = 10
print(name_variable)

variable1 = 12
print(variable1)

# 123variable = 13
# print(123variable)

# variable-nama = 13
# print(variable-nama)

# variable@ = 10
# print(variable@)

# if = 10
#     print(if)

variable1 = 10*3
print(variable1)

# integer
jumlahSisiPersegiPanjang = 10
print(jumlahSisiPersegiPanjang)

# float atau bilangan desimal
float_angka = 10.5
print(float_angka)

# boolean untuk logika 
boolean_true = True
print(boolean_true)

# string digunakan untuk input text atau buat penulisan word mau ditampilkan di web pakai string
# inline string sama dengan string
string_kata = 'Aku belajar di Haltev'
print(string_kata)

# multiline string (docs) 
string_multiline = """
    ini adalah baris 1
    ini adalah baris 2
    ini adalah baris 3
"""
print(string_multiline)

# casting untuk mengkonversi dari string ke integer atau dr float ke integer dan timbal balik atau fungsi lainnya 
angka_int_to_int = int(1)
angka_float_to_int = int(2.5)
angka_string_to_int = ("3")

print(angka_int_to_int, angka_float_to_int, angka_string_to_int)

# float untuk mengkonversi menjadi desimal
angka_string_float_to_float = float("3.5")
angka_int_to_float = float(3)
angka_string_int_to_float = float("3")
print(angka_string_float_to_float, angka_int_to_float, angka_string_int_to_float)

#string, cara mengkonversi bilangan angka dan float menjadi string
angka_int_to_string = str(1)
angka_float_to_string = str(2.5)
print(angka_int_to_string, angka_float_to_string) #ini otomatis spasi dengan ,
print(angka_int_to_string+angka_float_to_string)
print(angka_int_to_string+"  "+angka_float_to_string)
print(type(angka_int_to_string), type(angka_float_to_string))

# format  string
price_fruit = 5000
string_format = f"harga buah = {price_fruit}" #Cara1
print(string_format)
string_format = f"harga buah = {'Rp'} {price_fruit}"
print(string_format)

string_format = "harga buah = {} {}".format('Rp' , price_fruit) #cara2
print(string_format)
string_format = f"harga buah = {'Rp'} {price_fruit:.2f}" #ubah menjadi string float atau menambah desimal dalam angka numeric
print(string_format)

# escape character 
string_escape = 'Aku seorang developer "Python" di Haltev' #cara mensiasati penggunaan string yang mau menampilkan tanda petik 2 tapi gak mau pakai backslash
print(string_escape)
string_escape = "Aku seorang developer \"Python\" di Haltev"
print(string_escape) 

# operator aritmatika
a = 20
b = 6
print(a//b)#pembagian bulat 
print(a%b)#sisa pembagian
print(a**b)#eksponen atau pangkat
print()

# operator pembanding
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print()

# operator logika
print((a>b) and (a==b))
print((a>b) or (a==b))
print(not ((a>b) or (a==b)))#not membalikkan fungsi akhir dari operator or 
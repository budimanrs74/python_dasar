list_bahasa_pemprograman = ['python','C++','java','JavaScript']
# mencetak list
print(list_bahasa_pemprograman)

# menambahkan list
# cara 1
list_bahasa_pemprograman.append('c')
# list_bahasa_pemprograman.append('')
print(list_bahasa_pemprograman)

# cara 2
# list_bahasa_pemprograman[5] = 'Flutter'
# print(list_bahasa_pemprograman)

# insert
list_bahasa_pemprograman.insert(1, 'Flutter')
print(list_bahasa_pemprograman)

# extend
list_bahasa_pemprograman.extend(['PHP','Swift','Kotlin'])
print(list_bahasa_pemprograman)
list_bahasa_pemprograman.extend(['Golang','Reac-native'])
print(list_bahasa_pemprograman)

# modifikasi
list_bahasa_pemprograman[1] = 'C#'
print(list_bahasa_pemprograman)

list_bahasa_pemprograman[6] = 'Flutter'
print(list_bahasa_pemprograman)

list_bahasa_pemprograman[2:4] = ["GO", "Rust"]
print(list_bahasa_pemprograman)

# menghapus
list_bahasa_pemprograman.remove('Kotlin')
print(list_bahasa_pemprograman)

# end

# tuple, dugunakan untuk data yang konstan
tuple_buah = ('apel','mangga','jeruk')
tuple_list_bahasa_pemprograman = tuple(list_bahasa_pemprograman)
print(tuple_list_bahasa_pemprograman)
print(tuple_buah)

# tambah (error)
# tuple_buah.append('coba1')
# print(tuple_buah)

# modifikasi (error)
# tuple_buah[1] = 'Jeruk'
# print(tuple_buah)

# end

# dictionary
person = {
    'name' : 'Alice',
    'age' : 25,
    'city' : 'Jakarta'

}

print(person)

# akses value berdasarkan key
print(person['age'])

# akses value tanpa key
print(person.values())

# akses key nya saja 
print(person.keys())

# modifikasi
person['city'] = 'Bandung'
print(person)

# add birthday
person['birthday'] = 'Bekasi, 12 Jan 2003' 
print(person)

# remove birthday
# person.pop('birthday')
# del person['birthday']

# destroy all data 
# del person

# hapus semua isinya saja
person.clear()
print(person)

# end

# conditional statement
person = {
    'name' : 'Bobby',
    'age' : 30,
    'city' : 'Bandung',
    'verified' : True
}

# if
if person['name'] != 'Bobby':
    print('Umur Bobby {}'.format(person['age']))
elif person['verified']:
    print(f"{person['name']} sudah terverifikasi")
else:
    print('tidak ada nama tersebut')

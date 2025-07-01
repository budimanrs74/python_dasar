# percobaan try and except

try:
    x=10
    print(x)
except:
    print('terjadi error')

print('='*5)

# error case type data
try:
    x1='10'
    x2=float(x1)
    xtotal=x1+x2
    print(xtotal)
except:
    print('type data float tidak bisa ditambah dengan string')

print('=*5')

# case dengan nama errornya 
# try:
#     x1=input('masukkan string angka: ')
#     x2=int(x1)
#     xtotal= x1-x2
#     print(xtotal)
# except ValueError:
#     print('nilainya bukan angka')
# except TypeError:
#     print('string tidak bisa logika dengan angka')

# try:
#     x1=input('masukkan string angka: ')
#     x2=float(x1)
#     xtotal= x1-x2
#     print(xtotal)
# except ValueError:
#     print('nilainya bukan angka')
# except TypeError:
#     print('string tidak bisa logika dengan angka')
# except:
#     print('type data float tidak bisa ditambah dengan string')

# try:
#     print(2/0)
# except ZeroDivisionError:
#     print('tidak bisa dibagi dengan angka nol')

# case paksa error
try:
    angka1=int(input('masukkan angka pertama:'))
    angka2=int(input('masukkan angka kedua:'))

    if(angka1 == angka2):
        raise Exception('angkanya sama gan')
    
    print(angka1/angka2)
except Exception as e:
    print(e)

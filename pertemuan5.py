list_1=[1,2,3,4,5,6,7,8,9,10]

# looping for list 
for i in list_1:
    print(f'data ke - {i}')

print('===========')

# looping dengan for range 
for i in range(1,11): #start dan stop
    print(f'data ke - {i}')


# for dengan if
for i in list_1:
    print(f'data ke - {i}')
    # ganjil
    if(i%2==0):
        print('even')
    #  genap
    if(i%2==1):
        print('odd')
    print()

print('======')

# for break
for i in list_1:
    print(f'data ke-{i}')

    if(i==5):
        print('berhenti')
        break

print('=====')

#  for continue 
for i in list_1:
    if (i==8):
        print('lanjutkan')
        continue

    print(f'data ke -{i}')

print('======')

# break cara lain
i = 0
out = True
while out:
    print(f'data ke - {list_1[i]}')

    if (list_1[i] == 5):
        print('berhenti/keluar')
        out=False
    i+=1

print('========')

# membuat bintang
jumlah_bintang = 6
for i in range(1, jumlah_bintang):
    print('*'*i)

print('=========')
# for else

for i in list_1:
    print(i)
    if i == 5:
        break
else:
    print('tidak ditemukan')
    print('syntax selanjutnya')

print('====')

for i in list_1:
    print(i)
    if i ==11:
        break 
else:
    print('tidak ditemukan')
    print('syntax selanjutnya')


    
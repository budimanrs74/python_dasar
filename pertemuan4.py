# while
# infinite loop
# while True:tidak akan berhenti atau berulang terus 
    # print('jalan')
#     print ('jalan') maka tidak akan berhenti

# mengatasinya
# cara 1
kondisi = True

# while kondisi:
#     print('jalan')
#     kondisi = False

#  cara 2
# while True:
#     print('jalan')
#     break # berhenti dari looping 

# continue
# data = [1,2,3,4,5,6,7,8,9,10]
# i = 0
# while True:
#     if i ==10:
#         break
#     if i ==5:
#         i+=1
#         continue
#     print(data[i])
#     i+=1 #i=i+1


# contoh soal
# dataList = []
# increment_pembanding = 0
# while True:
#     if increment_pembanding== 24:
#         break
#     a = int(input('Masukan Bilangan :'))
#     if a == increment_pembanding:
#         print(f'bilangan valid: {a}')
#         increment_pembanding+=1
#     else:
#         print(f'bilangan tidak valid:{a}')
#         continue


# contoh soal
# dataList = []
# increment_pembanding = 0
# while True:
#     if increment_pembanding== 24:
#         break
#     a = input('Masukan Bilangan :')

# #     string kosong 
#     if a.strip() == '':
#         print('string kosong')
#         continue
   
#     #  membandingkan alphabet
#     if a.isalpha():
#         print(f'{a} ini bukan bilangan')
#         continue
    
#     elif a.isspace():
#         print(f'{a} terdapat space')
#         continue
        
#     else:
#         a = int(a)

#     #  untuk pembandingan hasil
#     if a == increment_pembanding:
#         print(f'bilangan valid: {a}')
#         dataList.append(a)   
#         increment_pembanding+=1
#     else:
#         print(f'bilangan tidak valid:{a}')
#         continue
# print(dataList)

#  contoh soal 2 
while True:
    inputpassword = input('Masukkan password:')
    confirmpassword = input('Masukkan konfirmasi password :')

    if inputpassword==confirmpassword:
        print('password valid')
        break
    else:
        print('passord tidak valid')
        continue

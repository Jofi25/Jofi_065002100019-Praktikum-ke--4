# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 09:33:36 2021

@author: jofi
"""

print('Program ini akan menghitung hari dalam suatau bulan')
b = int(input('Masukkan Bulan Yang Ingin Dilihat dalam Nomor (1 - 12):' ))
if b > 12 :
    print('Bukan Termasuk Bulan, Silahkan masukkan angka yang benar !')

elif b == 1 :
    print('Jumlah Hari Pada Bulan Januari Adalah 31 Hari')
    
elif b == 2 :
    t = int(input('Silahkan Masukkan Tahunnya : '))
    if t % 4 == 0 and t % 100 != 0 or t % 400 == 0 :
        print('Jumlah Hari Pada Tahun', t, 'Adalah 29 Hari')
    else :
        print('Jumlah Hari Pada Tahun', t, 'Adalah 28 Hari')
        
elif b == 3 :
    print('Jumlah Hari Pada Bulan Januari Adalah 31 Hari')

elif b == 4 :
    print('Jumlah Hari Pada Bulan Januari Adalah 30 Hari')
    
elif b == 5 :
    print('Jumlah Hari Pada Bulan Januari Adalah 31 Hari')
    
elif b == 6 :
    print('Jumlah Hari Pada Bulan Januari Adalah 30 Hari')
    
elif b == 7 :
    print('Jumlah Hari Pada Bulan Januari Adalah 31 Hari')
    
elif b == 8 :
    print('Jumlah Hari Pada Bulan Januari Adalah 31 Hari')
    
elif b == 9 :
    print('Jumlah Hari Pada Bulan Januari Adalah 30 Hari')
    
elif b == 10 :
    print('Jumlah Hari Pada Bulan Januari Adalah 31 Hari')
    
elif b == 11 :
    print('Jumlah Hari Pada Bulan Januari Adalah 30 Hari')
    
elif b == 12 :
    print('Jumlah Hari Pada Bulan Januari Adalah 31 Hari')
    
else : 
    print('Terimakasih Telah Menggunakan Program Kami')
    
print('Terima Kasih Telah Menggunakan Program Kami')
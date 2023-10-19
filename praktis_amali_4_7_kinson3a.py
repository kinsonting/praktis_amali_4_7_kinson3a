'''Ini merupakan satu program ringkas untuk mendapatkan isipadu kubiod'''
pi=3.142
def kira_kubiod(tinggi,panjang,lebar):
    isipadu_kubiod=tinggi*panjang*lebar
    return isipadu_kubiod

def kubiod(): #Isipadu kubiod
    tinggi=float(input("Masukkan tinggi:"))
    panjang=float(input("Masukkan panjang:"))
    lebar=float(input("Masukkan lebar:"))
    print("Isipadu kubiod=",kira_kubiod(tinggi,panjang,lebar))

def kira_silinder(pi,jejari,tinggi):
    isipadu_silinder=pi*(jejari**2)*(tinggi)
    return isipadu_silinder

def silinder(): #Isipadu silinder
    jejari=float(input("Masukkan jejari:"))
    tinggi=float(input("Masukkan tinggi:"))
    print("Isipadu silinder=",kira_silinder(pi,jejari,tinggi))

def kira_kon(pi,jejari,tinggi):
    isipadu_kon=(1/3)*pi*(jejari**2)*(tinggi)
    return isipadu_kon

def kon():#Isipadu kon
    jejari:float(input("Masukkan jejari:"))
    tinggi:float(input("Masukkan tinggi:"))
    print("Isipadu kon=",kira_kon(pi,jejari,tinggi))

def kira_sfera(pi,jejari):
    isipadu_sfera=(4/3)*pi*(jejari**3)
    return isipadu_sfera

def sfera(): #Isipadu sfera
    jejari=int(input("Masukkan jejari:"))
    print=("Isipadu sfera=",kira_sfera(pi,jejari))

###################
#Subatur cara utama
###################
    
ulang=True

while(ulang):
    print(' ' '**************************************     MENU MENGIRA ISI PADU     ************************************** 1. Kubiod 2.Silinder 3.Kon 4.Sfera 5.Keluar dari program' ' ')
    print("")
    
    pilih=int(input("Sila masukkan pilihan anda:"))
    
    if(pilih==1):
        kubiod() #memanggil fungsi kubiod
    elif(pilih==2):
        silinder() #memanggil fungsi silinder
    elif(pilih==3):
        kon() #memanggil fungsi kon
    elif(pilih==4):
        sfera() #memanggil fungsi sfera
    elif(pilih==5):
        ulang=False
        print("Goodbye")
        exit
    else:
        print ("Pilihan anda tiada dalam senarai")
        print("")
    



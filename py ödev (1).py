import time

def isimkontrol():
    sayac = 0
    while sayac <= 2:  
        ad = input("Adınız:")
        soyad = input("Soyadınız:")
        if ad.lower() == "eray" and soyad.lower() == "akın" or soyad.lower() == "akin": 
            print("\nHoşgeldiniz!")
            return 1  
            break
        
        if sayac == 2:
            print("3 kere hatalı giriş yaptınız.Lütfen daha sonra tekrar deneyiniz. ")
            return 0 
            break
            
        else:
            print("Yanlış giriş.Tekrar Deneyiniz:")
            sayac += 1  


def dersler():  
    dersler = []
    ders = input("aldığınız dersleri aralarında boşluk bırakarak giriniz :")
    dersler = ders.split(" ") 
    if len(dersler) < 3:
        return 0  
    if len(dersler) >= 3:
        return 1  



def puan():  
    sınavlar = {"ders": " ", "dönemortası": 0, "final": 0, "proje": 0}
    sınavlar["ders"] = input("sınav olduğunuz dersi giriniz :")
    sınavlar["dönemortası"] = int(input("dönemortası sınavı notunuzu giriniz :"))
    sınavlar["final"] = int(input("final sınavı notunuzu giriniz :"))
    sınavlar["proje"] = int(input("proje notunuzu giriniz :"))
    puan = ((sınavlar["dönemortası"]/100)*30) + ((sınavlar["final"]/100)*50) + ((sınavlar["proje"]/100)*20)
    return puan


durum = 1
durum = isimkontrol()

if durum == 0:
    durum = 2
  
if durum == 1:
    durum = dersler() 
 
if durum == 0:
    print("Az ders aldığınızdan dolayı sınıfı geçmeyi başaramadınız.")
    durum = 2

if durum == 1:
    puan = puan()
    print("puanınız =",puan)
    if puan >= 90:
        print("notunuz AA")
    elif 70 <= puan and puan < 90:
        print("notunuz BB")
    elif 50 <= puan and puan < 70:
        print("notunuz CC")    
    elif 30 <= puan and puan < 50:
        print("notunuz DD")    
    elif 0 <= puan and puan < 30:
        print("notunuz FF")
        print("sınıfı geçmeyi başaramadınız.")

if durum != 2:
    time.sleep(5)
elif durum == 2:
    time.sleep(3)
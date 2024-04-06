import random
import time

class Kumanda():
    def __init__(self,tv_durum="Kapali",tv_ses=0,kanal_listesi=["Trt"],kanal="Trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_ac(self):
        if (self.tv_durum=="Acik"):
            print("Televizyon zaten acik")
        else:
            print("Televizyon aciliyor...")
            self.tv_durum="Acik"
    def tv_kapat(self):
        if(self.tv_durum=="Kapali"):
            print("Televizyon zaten kapali")
        else:
            print("Televizyon kapaniyor...")
            self.tv_durum="Kapali"
    
    def ses_ayarlari(self):
        while True:
            cevap=input("Sesi azalt: '<'\nSesi Artir: '>'\nCikis :cikis:")
            if (cevap =="<"):
                if (self.tv_ses != 0):

                    self.tv_ses-=1
                    print("Ses:",self.tv_ses)
            elif(cevap ==">"):
                if (self.tv_ses != 31):

                    self.tv_ses+=1
                    print("Ses:",self.tv_ses)
            else:
                print("Ses Guncellendi:",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor....")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi")
    def rastgele_kanal(self):
         rastgele=random.randint(0,len(self.kanal_listesi)-1)
         self.kanal=self.kanal_listesi(rastgele)
         print("Su anki kanal:",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv Durumu:{}\nTv ses:{}\nKanal listesi:{}\nSu anki kanal:{}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda=Kumanda()

print("""

Televizyon Uygulamasi


1. Tv Ac

2.Tv Kapat

3.Ses Ayarlari

4.Kanal  Ekle

5.Kanal Sayisini Oyrenme

6.Rastgele Kanala Gecme

7.Televizyon Bilgileri

Cikmak icin 'q' ya basin.
""")

while True:
    islem=input("Islem secin:")
     
    if islem =='q':
        print("Proqram sonlandiriliyor...")
        break
    elif islem =="1":
        kumanda.tv_ac()
    elif islem =="2":
        kumanda.tv_kapat()
    elif islem =="3":
        kumanda.ses_ayarlari()
    elif islem =="4":
        kanal_isimleri=input("kanal isimleri ',' ile ayirarak girin")
        kanal_listesi=kanal_isimleri.split(",")
        for eklenecek in kanal_listesi:
            kumanda.kanal_ekle(eklenecek)
    elif islem =="5":
        print("kanal listesi:",len(kumanda))
    elif islem =="6":
        kumanda.rastgele_kanal()
    elif islem =="7":
        print(kumanda)
    else:
        print("Gecersiz islem")


    
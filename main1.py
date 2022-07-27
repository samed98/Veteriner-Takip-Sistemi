# -*- coding: utf-8 -*-
"""
Created on Thu May 12 01:16:38 2022

@author: MONSTER
"""
# -----------KÜTÜPHANE-----------#

import sqlite3
import sys
import os
import webbrowser



from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
from PyQt5.QtCore import QDate, QTime, QDateTime
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from Anasayfa1UI import *
from listeUI import*
from GirisEkraniUI import *
from HakkindaUI import *
from KayitEkraniUI import *
from SikayetlerUI import *

# -----------UYGULAMA OLUŞTUR-----------#
Uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)

Uygulama1 = QApplication(sys.argv)
penListe = QMainWindow()
ui1 = Ui_liste()
ui1.setupUi(penListe)

penHakkinda = QDialog()
ui2 = Ui_Dialog()
ui2.setupUi(penHakkinda)

Uygulama3 = QApplication(sys.argv)
penGiris = QMainWindow()
ui3 = Ui_Giris()
ui3.setupUi(penGiris)
penGiris.show()

Uygulama4 = QApplication(sys.argv)
penKayit = QMainWindow()
ui4 = Ui_KayitOl()
ui4.setupUi(penKayit)

Uygulama5 = QApplication(sys.argv)
penSikayet = QMainWindow()
ui5 = Ui_Sikayet()
ui5.setupUi(penSikayet)

# -----------VERİ TABANI-----------#


global curs
global conn
conn = sqlite3.connect('veritabani.db')
curs = conn.cursor()
sorguCreTblVeteriner = ("CREATE TABLE IF NOT EXISTS Anasayfa(                 \
                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,    \
                 Tarih TEXT NOT NULL,                          \
                 SahipAdi TEXT NOT NULL,                          \
                 SahipAdres TEXT NOT NULL,                       \
                 SahipIl TEXT NOT NULL,                           \
                 SahipIlçe TEXT NOT NULL,                           \
                 SahipTelNo TEXT NOT NULL,                               \
                 SahipE_Posta TEXT NOT NULL,                               \
                 HastaIsmi TEXT NOT NULL,                            \
                 HastaD_Tarihi TEXT NOT NULL,                            \
                 HastaCinsiyet TEXT NOT NULL,                            \
                 HastaCins TEXT NOT NULL,                            \
                 HastaYavru TEXT NOT NULL,                            \
                 HastaAgirlik TEXT NOT NULL,                     \
                 TemelSikayetler TEXT NOT NULL,                 \
                 Sicaklik TEXT NOT NULL,                        \
                 KalpAtisi TEXT NOT NULL,                           \
                 Solunum TEXT NOT NULL,                                 \
                 KondisyonPuan TEXT NOT NULL,                       \
                 AgizBoslugu TEXT NOT NULL,                            \
                 Gozler TEXT NOT NULL,                            \
                 Kulaklar TEXT NOT NULL,                          \
                 BurunBogaz TEXT NOT NULL,                            \
                 Kalp TEXT NOT NULL,                            \
                 Sinirler TEXT NOT NULL,                            \
                 Akcigerler TEXT NOT NULL,                            \
                 Karin TEXT NOT NULL,                            \
                 LenfDügümler TEXT NOT NULL,                          \
                 Deri TEXT NOT NULL,                            \
                 IskeletKas TEXT NOT NULL,                            \
                 Urogenital TEXT NOT NULL,                            \
                 BulguAgiz TEXT NOT NULL,                            \
                 BulguGoz TEXT NOT NULL,                            \
                 BulguKulak TEXT NOT NULL,                            \
                 BulguBurunBogaz TEXT NOT NULL,                            \
                 BulguKalp TEXT NOT NULL,                            \
                 BulguSinir TEXT NOT NULL,                            \
                 BulguAkciger TEXT NOT NULL,                            \
                 BulguKarin TEXT NOT NULL,                            \
                 BulguLenf TEXT NOT NULL,                            \
                 BulguDeri TEXT NOT NULL,                            \
                 BulguIskeletKas TEXT NOT NULL,                            \
                 BulguUrogenital TEXT NOT NULL,                         \
                 SahipAdSoyad TEXT,                            \
                 HastaAdi TEXT,                                \
                 HastaCinsi TEXT,                          \
                 Teshisler TEXT NOT NULL,           \
                 OnGozlem TEXT NOT NULL,                            \
                 Degerlendirme TEXT NOT NULL,           \
                 Tedavi TEXT NOT NULL,           \
                 Sikayet TEXT NOT NULL,           \
                 Gecmis TEXT NOT NULL,                      \
                 Fiyat TEXT)")
curs.execute(sorguCreTblVeteriner)
conn.commit()

conn0 = sqlite3.connect('veritabani.db')
curs0 = conn0.cursor()
sorguCreTblIller = ("CREATE TABLE IF NOT EXISTS il (     \
                    IlId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
	                SehirAdi VARCHAR(255) NULL)")

curs0.execute(sorguCreTblIller)
conn0.commit()

conn1 = sqlite3.connect('veritabani.db')
curs1 = conn1.cursor()
sorguCreTblIlceler = ("CREATE TABLE IF NOT EXISTS ilce(                 \
                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,                        \
                 IlceAdi varchar(255) NOT NULL,                     \
                 SehirId TEXT NOT NULL)")
curs1.execute(sorguCreTblIlceler)
conn1.commit()

# -------------GİRİŞ-KAYIT OL VERİTABANI-------------------#


conn2 = sqlite3.connect("giris_veritabani.db")
curs2 = conn2.cursor()
sorguCreTblGiris = ("CREATE TABLE IF NOT EXISTS giris (    \
                    Id2 INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                    KullaniciAdi TEXT NOT NULL UNIQUE, \
                    Sifre TEXT NOT NULL UNIQUE)")

curs2.execute(sorguCreTblGiris)
conn2.commit()

# ----------------------SIRALI SAYFA AÇMA------------------#


def GIRISAC():
    penGiris.show()
    penAna.close()
    penKayit.close()
    penListe.close()

def KAYITAC():
    penKayit.show()
    penGiris.close()
    penAna.close()
    penListe.close()


def ANASAYFAAC():
    penAna.show()
    penKayit.close()
    penGiris.close()
    penListe.close()


# ----------------------KAYIT OL EKRANI--------------------#


def KAYIT():
    ui3.lnekullaniciadi.clear()
    ui3.lnesifre.clear()
    kullaniciAdi = ui4.lnekullaniciadi1.text()
    sifre = ui4.lnesifre1.text()
    if (sifre != "") and (kullaniciAdi != ""):
        curs2.execute("INSERT INTO giris (KullaniciAdi,Sifre) VALUES (?,?)", (kullaniciAdi, sifre))
        conn2.commit()
        #ui3.statusbar.showMessage(" "*5 + "Kayıt Başarıyla Gerçekleştirildi...", 3000)
        ui4.lnekullaniciadi1.clear()
        ui4.lnesifre1.clear()
        GIRISAC()
    else:
        ui4.statusbar.showMessage(" " * 5 + "Hatalı Kayıt Açtınız...", 3000)
        
# ----------------------KAYIT OL EKRANI İPTAL ETME--------------------#        
def IPTALET():
    cevappp = QMessageBox.question(penKayit, "İptal Et", "Kaydı iptal etmek istediğinize emin misiniz?", \
                                   QMessageBox.Yes | QMessageBox.No)
    if cevappp == QMessageBox.Yes:
        #conn2.close()
        ui4.lnekullaniciadi1.clear()
        ui4.lnesifre1.clear()
        GIRISAC()

    else:
        penKayit.show()
        
# ----------------------GİRİŞ EKRANI-----------------------#


def GIRIS():
    global KullaniciAdi

    kullaniciadi = ui3.lnekullaniciadi.text()
    sifre = ui3.lnesifre.text()

    curs2.execute("SELECT * FROM giris WHERE KullaniciAdi='%s' and Sifre='%s'" % (kullaniciadi, sifre))
    conn2.commit()

    if (len(curs2.fetchall()) > 0):
        #ui.statusbar.showMessage(" " * 3 + "Hoşgeldiniz...", 5000)
        penGiris.close()
        penAna.show()
        ui3.lnekullaniciadi.clear()
        ui3.lnesifre.clear()
    else:
        ui3.statusbar.showMessage(" " * 3 + "Kullanıcı Adı Ya da Şifre Hatalı. Tekrar Deneyiniz...", 5000)

# ----------------------GİRİŞ EKRANI ÇIKIŞ YAPMA-----------------------#
def CİKİSYAP():
    cevapp = QMessageBox.question(penGiris, "ÇIKIŞ", "Giriş ekranından çıkmak istediğinize emin misiniz?", \
                                  QMessageBox.Yes | QMessageBox.No)
    if cevapp == QMessageBox.Yes:
        conn2.close()
        penGiris.close()
        window.close()
        sys.exit(Uygulama2.exec_())
        sys.exit(app.exec_())

    else:
        penGiris.show()


# ----------------------ŞİFRE GÖSTER-----------------------#


def SIFREGOSTER():
    if ui3.rdsifregosterr.isChecked():
        ui3.lnesifre.setEchoMode(QLineEdit.Normal)
    else:
        ui3.lnesifre.setEchoMode(QLineEdit.Password)


def SIFREGOSTERR():
    if ui4.rdsifregoster.isChecked():
        ui4.lnesifre1.setEchoMode(QLineEdit.Normal)
    else:
        ui4.lnesifre1.setEchoMode(QLineEdit.Password)


# ----------------------YOUTUBE SAYFA AÇMA-----------------------#
        
def YOUTUBE():
    
    webbrowser.open('https://www.youtube.com/channel/UC-G8Ls71gbWti5vxVupROuA')
        
# ----------------------TABLO-ŞİKAYETLER GERİ GELME-----------------------#

def GERİ():
    penListe.close()
    penSikayet.show()


# ----------------------ŞİKAYETLER-ANA PENCERE GERİ GELME-----------------------#

def GERİİ():
    penSikayet.close()
    penAna.show()


# ----------------------ANA-ŞİKAYETLER İLERİ GİTME-----------------------#

def İLERİ():
    penAna.close()
    penSikayet.show()


# ----------------------ŞİKAYETLER-TABLO İLERİ GİTME-----------------------#

def İLERİİ():
    penSikayet.close()
    penListe.show()


# -----------E-POSTA-----------#

import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


x = curs0
x.execute("SELECT * FROM il")
for i in x:
    _Il = ui.Il.addItem(str(i[1]))
_Il = ui.Il.currentText() 

y = curs1    
def ilcesec():
    
    _Ilce = ui.Ilce.clear()    
    secili_il=int(ui.Il.currentIndex())

    secim=("""SELECT * FROM ilce WHERE SehirId = {}""").format(int(secili_il))
    y.execute(secim)
    ilce1 = y.fetchall()
    
    for ilce in ilce1:
        
        _Ilce = ui.Ilce.addItem(str(ilce[1]))
    
    _Ilce = ui.Ilce.currentText() 

   



ui.Il.currentIndexChanged['int'].connect(ilcesec)       


# -----------KAYDET-----------#
def EKLE():
    
    _Ad_Soyad = ui.Ad_Soyad.text()
    _Adres = ui.Adres.text()
    _Il = ui.Il.currentText()
    _Ilce = ui.Ilce.currentText()
    _Telefon_Numarasi = ui.Telefon_Numarasi.text()
    _Sicaklik = ui.Sicaklik.text()
    _Kalp_Atisi =ui.Kalp_Atisi.text()
    _Solunum = ui.Solunum.text()
    _cmb_Puan = ui.cmb_Puan.currentText()
    _Hasta_Ismi = ui.Hasta_Ismi.text()
    _dogum_tarihi = ui.dogum_tarihi.date().toString(QtCore.Qt.ISODate)
    _cmb_Cinsiyet = ui.cmb_Cinsiyet.currentText()
    _cmb_Cins = ui.cmb_Cins.currentText()
    _Yavru = ui.Yavru.text()
    _Ad_Soyad1 = _Ad_Soyad
    _Hasta_Ismi1 = _Hasta_Ismi
    _cmb_Cins1 = _cmb_Cins
   
    
    eposta = ui.E_Posta.text() 
    
    match = re.fullmatch(regex, eposta)
    
    

    if match is not None:
        ui.statusbar.showMessage(" " * 3 + "Geçerli Bir E-posta Girildi.", 5000)
        _E_Posta = eposta
        match.group()
        
    else:
       QMessageBox.warning(penAna, "HATA", "Geçersiz Bir E-Posta girildi. Lütfen Tekrar Deneyiniz.",\
                           QMessageBox.Ok)
        
    
         
    
    if ui.rb_normal1.isChecked():
        _AgizBoslugu = "Normal"
    if ui.rb_anormal1.isChecked():
        _AgizBoslugu = "Anormal"
    
    if ui.rb_normal2.isChecked():
        _Gozler = "Normal"
    if ui.rb_anormal2.isChecked():
        _Gozler = "Anormal"
        
    if ui.rb_normal3.isChecked():
        _Kulaklar = "Normal"
    if ui.rb_anormal3.isChecked():
        _Kulaklar = "Anormal"
        
    if ui.rb_normal4.isChecked():
        _BurunBogaz = "Normal"
    if ui.rb_anormal4.isChecked():
        _BurunBogaz = "Anormal"
        
    if ui.rb_normal5.isChecked():
        _Kalp = "Normal"
    if ui.rb_anormal5.isChecked():
        _Kalp = "Anormal"
        
    if ui.rb_normal6.isChecked():
        _Sinirler = "Normal"
    if ui.rb_anormal6.isChecked():
        _Sinirler = "Anormal"
    
    if ui.rb_normal7.isChecked():
        _Akcigerler = "Normal"
    if ui.rb_anormal7.isChecked():
        _Akcigerler = "Anormal"
    
    if ui.rb_normal8.isChecked():
        _Karin = "Normal"
    if ui.rb_anormal8.isChecked():
        _Karin = "Anormal"
        
    if ui.rb_normal9.isChecked():
        _LenfDugumleri = "Normal"
    if ui.rb_anormal9.isChecked():
        _LenfDugumleri = "Anormal"
    
    if ui.rb_normal10.isChecked():
        _Deri = "Normal"
    if ui.rb_anormal10.isChecked():
        _Deri = "Anormal"
    
    if ui.rb_normal11.isChecked():
        _IskeletKas = "Normal"
    if ui.rb_anormal11.isChecked():
        _IskeletKas = "Anormal"
        
    if ui.rb_normal12.isChecked():
        _Urogenital = "Normal"
    if ui.rb_anormal12.isChecked():
        _Urogenital = "Anormal"
    
    _Bulgu_Agiz_Boslugu = ui.Bulgu_Agiz_Boslugu.text()
    _Bulgu_Gozler = ui.Bulgu_Gozler.text()
    _Bulgu__Kulaklar = ui.Bulgu__Kulaklar.text()
    _Bulgu_Burun_Bogaz  = ui.Bulgu_Burun_Bogaz.text()
    _Bulgu_Kalp = ui.Bulgu_Kalp.text()
    _Bulgu_Sinirler = ui.Bulgu_Sinirler.text()
    _Bulgu_Akcigerler = ui.Bulgu_Akcigerler.text()
    _Bulgu_Karin = ui.Bulgu_Karin.text()
    _Bulgu_Lenf_Dugumleri = ui.Bulgu_Lenf_Dugumleri.text()
    _Bulgu_Deri = ui.Bulgu_Deri.text()
    _Bulgu_Iskelet_Kas =  ui.Bulgu_Iskelet_Kas.text()
    _Bulgu_Urogenital = ui.Bulgu_Urogenital.text()
    _de_Tarih = ui.de_Tarih.date().toString(QtCore.Qt.ISODate)
    _cmb_Cinsiyet = ui.cmb_Cinsiyet.currentText()
    _cmb_Cins = ui.cmb_Cins.currentText()
    
    _Degerlendirme = ui5.Degerlendirme.text()
    _Tedavi_Tavsiyeler = ui5.Tedavi_Tavsiyeler.text()
    _Diger_Sikayetler = ui5.Diger_Sikayetler.text()
    _Gecmis = ui5.Gecmis.text()

    _On_Gozlem = ""
    if ui.chk_Hareket.isChecked():
        _On_Gozlem += "Hareket;"
    if ui.chk_Terli.isChecked():
        _On_Gozlem += "Terli;"
    if ui.chk_Duyarsiz.isChecked():
        _On_Gozlem += "Duyarsız;"
    if ui.chk_Istikrarsiz.isChecked():
        _On_Gozlem += "İstikrarsız;"
    if ui.chk_Stresli.isChecked():
        _On_Gozlem += "Stresli;"
    if ui.chk_Kuru.isChecked():
        _On_Gozlem += "Kuru;"
    if ui.chk_Istikrarli.isChecked():
        _On_Gozlem += "İstikrarlı;"
    if ui.chk_Dinc.isChecked():
        _On_Gozlem += "Dinç;"
    if ui.chk_Sokta.isChecked():
        _On_Gozlem += "Şokta;"
    if ui.chk_Olasi.isChecked():
        _On_Gozlem += "Olası İstikrarsız;"
    if ui.chk_Diger1.isChecked():
        _On_Gozlem += "Diğer;"
    
    
    _Teshisler = ""
    if ui.chk_CBC.isChecked():
        _Teshisler+= "CBC;"
    if ui.chk_T4.isChecked():
        _Teshisler += "T4;"
    if ui.chk_ECG.isChecked():
        _Teshisler += "ECG;"
    if ui.chk_Deri_Testi.isChecked():
        _Teshisler += "Deri Testi;"
    if ui.chk_Felv_Fiv.isChecked():
        _Teshisler += "FELV/FIV;"
    if ui.chk_Diski.isChecked():
        _Teshisler += "Dışkı;"
    if ui.chk_Biyopsi.isChecked():
        _Teshisler += "Biyopsi;"
    if ui.chk_Chem.isChecked():
        _Teshisler += "Chem;"
    if ui.chk_Radyografi.isChecked():
        _Teshisler += "Radyografi;"
    if ui.chk_Karin_Ultrasonu.isChecked():
        _Teshisler += "Karın Ultrasonu;"
    if ui.chk_C_S.isChecked():
        _Teshisler += "Aerobic C ve S;"
    if ui.chk_Kalp_Kurdu_Testi.isChecked():
        _Teshisler += "Kalp Kurdu Testi;"
    if ui.chk_Laym_Titre.isChecked():
        _Teshisler+= "Laym Titre;"
    if ui.chk_Ameliyat_Oncesi_Kan_Tahlili.isChecked():
        _Teshisler += "Ameliyat Öncesi Kan Tahlili;"
    if ui.chk_Idrar_Tahlili.isChecked():
        _Teshisler += "İdrar Tahlili;"
    if ui.chk_Yankl_Yurek_Gosterimi.isChecked():
        _Teshisler += "Yankılı Yürek Gösterimi;"
    if ui.chk_Idrar_Gosterimi.isChecked():
        _Teshisler += "İdrar Gösterimi;"
    if ui.chk_Diger3.isChecked():
        _Teshisler += "Diğer;"
    
    _Fiyat=0
    
    if ui.chk_CBC.isChecked():
        _Fiyat += 50
    if ui.chk_T4.isChecked():
        _Fiyat += 55
    if ui.chk_ECG.isChecked():
        _Fiyat += 60
    if ui.chk_Deri_Testi.isChecked():
        _Fiyat += 65
    if ui.chk_Felv_Fiv.isChecked():
        _Fiyat += 70
    if ui.chk_Diski.isChecked():
        _Fiyat += 75
    if ui.chk_Biyopsi.isChecked():
        _Fiyat += 80
    if ui.chk_Chem.isChecked():
        _Fiyat += 85
    if ui.chk_Radyografi.isChecked():
        _Fiyat += 90
    if ui.chk_Karin_Ultrasonu.isChecked():
        _Fiyat += 95
    if ui.chk_C_S.isChecked():
        _Fiyat += 100
    if ui.chk_Kalp_Kurdu_Testi.isChecked():
        _Fiyat += 105
    if ui.chk_Laym_Titre.isChecked():
        _Fiyat += 110
    if ui.chk_Ameliyat_Oncesi_Kan_Tahlili.isChecked():
        _Fiyat += 115
    if ui.chk_Idrar_Tahlili.isChecked():
        _Fiyat += 120
    if ui.chk_Yankl_Yurek_Gosterimi.isChecked():
        _Fiyat += 125
    if ui.chk_Idrar_Gosterimi.isChecked():
        _Fiyat += 130
    if ui.chk_Diger3.isChecked():
        _Fiyat += 40
    
    
    
    _Temel_Sikayetler = ""
    if ui.chk_Yillik_Kontrol.isChecked():
        _Temel_Sikayetler+= "Yıllık Kontrol;"
    if ui.chk_Yavru_Kedi.isChecked():
        _Temel_Sikayetler += "Yavru Kedi;"
    if ui.chk_Uyusukluk.isChecked():
        _Temel_Sikayetler += "Uyuşukluk;"
    if ui.chk_Kusma.isChecked():
        _Temel_Sikayetler += "Kusma;"
    if ui.chkDis.isChecked():
        _Temel_Sikayetler += "Diş;"
    if ui.chk_Ishal.isChecked():
        _Temel_Sikayetler += "İshal;"
    if ui.chk_Oksuruk.isChecked():
        _Temel_Sikayetler += "Öksürük;"
    if ui.chk_Hapsirik.isChecked():
        _Temel_Sikayetler += "Hapşırma;"
    if ui.chk_Goz_Kontrol.isChecked():
        _Temel_Sikayetler += "Göz Kontrol;"
    if ui.chk_Cerrahi.isChecked():
        _Temel_Sikayetler += "Cerrahi;"
    if ui.chk_Kulak_Kontrol.isChecked():
        _Temel_Sikayetler += "Kulak Kontrol;"
    if ui.chk_Cilt_Kontrol.isChecked():
        _Temel_Sikayetler += "Cilt Kontrol;"
    if ui.chk_Topallik.isChecked():
        _Temel_Sikayetler+= "Topallık;"
    if ui.chk_Nefes_Problemi.isChecked():
        _Temel_Sikayetler += "Nefes Problemi;"
    if ui.chk_Felc.isChecked():
        _Temel_Sikayetler += "Felç;"
    if ui.chk_Artan_Istah.isChecked():
        _Temel_Sikayetler += "Artan İştah;"
    if ui.chk_Azalan_Istah.isChecked():
        _Temel_Sikayetler += "Azalan İştah;"
    if ui.chk_Secmeli_Cerrahi.isChecked():
        _Temel_Sikayetler += "Seçmeli Cerrahi;"
    if ui.chk_Idrar_Yapma.isChecked():
        _Temel_Sikayetler += "Artan İçme/İdrar Yapma;"
    if ui.chk_Diger2.isChecked():
        _Temel_Sikayetler += "Diğer;"
        
    _dsb_Agirlik = ui.dsb_Agirlik.value()

    curs.execute("INSERT INTO Anasayfa \
                     (Tarih,SahipAdi,SahipAdres,SahipIl ,SahipIlçe ,SahipTelNo , \
                      SahipE_Posta ,HastaIsmi ,HastaD_Tarihi ,HastaCinsiyet ,HastaCins ,HastaYavru, \
                      HastaAgirlik, TemelSikayetler, Sicaklik, KalpAtisi, KondisyonPuan, Solunum, AgizBoslugu, Gozler, Kulaklar,\
                      BurunBogaz, Kalp, Sinirler, Akcigerler, Karin, LenfDügümler, Deri, IskeletKas,\
                      Urogenital, BulguAgiz, BulguGoz, BulguKulak, BulguBurunBogaz, BulguKalp, BulguSinir,          \
                      BulguAkciger, BulguKarin, BulguLenf, BulguDeri, BulguIskeletKas, BulguUrogenital,          \
                      SahipAdSoyad, HastaAdi, HastaCinsi, Teshisler, Ongozlem, Degerlendirme, Tedavi, Sikayet, Gecmis, Fiyat)\
                      VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
                 ( _de_Tarih, _Ad_Soyad, _Adres, _Il, _Ilce, _Telefon_Numarasi, _E_Posta,
                  _Hasta_Ismi, _dogum_tarihi, _cmb_Cinsiyet, _cmb_Cins, _Yavru,                             
                  _dsb_Agirlik, _Temel_Sikayetler, _Sicaklik, _Kalp_Atisi, _cmb_Puan, _Solunum, _AgizBoslugu, _Gozler,     
                  _Kulaklar, _BurunBogaz, _Kalp, _Sinirler, _Akcigerler, _Karin, _LenfDugumleri, _Deri, _IskeletKas,
                  _Urogenital, _Bulgu_Agiz_Boslugu, _Bulgu_Gozler, _Bulgu__Kulaklar, _Bulgu_Burun_Bogaz,                    
                  _Bulgu_Kalp, _Bulgu_Sinirler, _Bulgu_Akcigerler, _Bulgu_Karin, _Bulgu_Lenf_Dugumleri, _Bulgu_Deri,            
                  _Bulgu_Iskelet_Kas, _Bulgu_Urogenital, _Ad_Soyad1, _Hasta_Ismi1, _cmb_Cins1, _Teshisler, _On_Gozlem, _Degerlendirme, _Tedavi_Tavsiyeler,            
                  _Diger_Sikayetler, _Gecmis, _Fiyat))
    conn.commit()

    LISTELE()

# -----------LİSTELE-----------#

def LISTELE():
    ui1.tblw_HastaBilgi.clear()

    ui1.tblw_HastaBilgi.setHorizontalHeaderLabels(('No', 'Tarih', 'SahipAdi','SahipAdres','SahipIl' ,'SahipIlçe' ,'SahipTelNo' , \
                      'SahipE_Posta' ,'HastaIsmi' ,'HastaD_Tarihi' ,'HastaCinsiyet' ,'HastaCins' ,'HastaYavru', \
                      'HastaAgirlik', 'TemelSikayetler' , 'Sicaklik', 'KalpAtisi', 'KondisyonPuan', 'Solunum',
                      'AgizBoslugu', 'Gozler', 'Kulaklar', 'BurunBogaz', 'Kalp',  'Sinirler' , 'Akcigerler', \
                      'Karin' ,'LenfDügümler', 'Deri' ,'IskeletKas', 'Urogenital' , 'BulguAgiz', 'BulguGoz',      \
                      'BulguKulak', 'BulguBurunBogaz', 'BulguKalp', 'BulguSinir', 'BulguAkciger', 'BulguKarin', 'BulguLenf',       \
                      'BulguDeri', 'BulguIskeletKas', 'BulguUrogenital', 'SahipAdSoyad', 'HastaAdi', 'HastaCinsi', 'Teshisler',             \
                      'Ongozlem', 'Degerlendirme' ,'Tedavi','Sikayet', 'Gecmis', 'Fiyat'))

    ui1.tblw_HastaBilgi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    curs.execute("SELECT * FROM AnaSayfa")

    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui1.tblw_HastaBilgi.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
            
    ui.Ad_Soyad.clear()
    ui.Adres.clear()
    ui.Il.setCurrentIndex(0)
    ui.Ilce.setCurrentIndex(0)
    ui.Telefon_Numarasi.clear()
    ui.E_Posta.clear()
    ui.Sicaklik.clear()
    ui.Kalp_Atisi.clear()
    ui.Solunum.clear()
    ui.cmb_Puan.setCurrentIndex(0)
    ui.Hasta_Ismi.clear()
    ui.dogum_tarihi.setCurrentSectionIndex(0)
    ui.cmb_Cinsiyet.setCurrentIndex(0)
    ui.cmb_Cins.setCurrentIndex(0)
    ui.Yavru.clear()
    ui.rb_normal1.setChecked(False)
    ui.rb_normal2.setChecked(False)
    ui.rb_normal3.setChecked(False)
    ui.rb_normal4.setChecked(False)
    ui.rb_normal5.setChecked(False)
    ui.rb_normal6.setChecked(False)
    ui.rb_normal7.setChecked(False)
    ui.rb_normal8.setChecked(False)
    ui.rb_normal9.setChecked(False)
    ui.rb_normal10.setChecked(False)
    ui.rb_normal11.setChecked(False)
    ui.rb_normal12.setChecked(False)
    ui.rb_anormal1.setChecked(False)
    ui.rb_anormal2.setChecked(False)
    ui.rb_anormal3.setChecked(False)
    ui.rb_anormal4.setChecked(False)
    ui.rb_anormal5.setChecked(False)
    ui.rb_anormal6.setChecked(False)
    ui.rb_anormal7.setChecked(False)
    ui.rb_anormal8.setChecked(False)
    ui.rb_anormal9.setChecked(False)
    ui.rb_anormal10.setChecked(False)
    ui.rb_anormal11.setChecked(False)
    ui.rb_anormal12.setChecked(False)
    ui.Bulgu_Agiz_Boslugu.clear()
    ui.Bulgu_Gozler.clear()
    ui.Bulgu__Kulaklar.clear()
    ui.Bulgu_Burun_Bogaz.clear()
    ui.Bulgu_Kalp.clear()
    ui.Bulgu_Sinirler.clear()
    ui.Bulgu_Akcigerler.clear()
    ui.Bulgu_Karin.clear()
    ui.Bulgu_Lenf_Dugumleri.clear()
    ui.Bulgu_Deri.clear()
    ui.Bulgu_Iskelet_Kas.clear()
    ui.Bulgu_Urogenital.clear()
    ui5.Degerlendirme.clear()
    ui5.Tedavi_Tavsiyeler.clear()
    ui5.Diger_Sikayetler.clear()
    ui5.Gecmis.clear()
    ui.de_Tarih.setCurrentSectionIndex(0)
    ui.cmb_Cinsiyet.setCurrentIndex(0)
    ui.cmb_Cins.setCurrentIndex(0)
    ui.chk_Hareket.setChecked(False)
    ui.chk_Terli.setChecked(False)
    ui.chk_Duyarsiz.setChecked(False)
    ui.chk_Istikrarsiz.setChecked(False)
    ui.chk_Stresli.setChecked(False)
    ui.chk_Kuru.setChecked(False)
    ui.chk_Istikrarli.setChecked(False)
    ui.chk_Dinc.setChecked(False)
    ui.chk_Sokta.setChecked(False)
    ui.chk_Olasi.setChecked(False)
    ui.chk_Diger1.setChecked(False)
    ui.chk_CBC.setChecked(False)
    ui.chk_T4.setChecked(False)
    ui.chk_ECG.setChecked(False)
    ui.chk_Deri_Testi.setChecked(False)
    ui.chk_Felv_Fiv.setChecked(False)
    ui.chk_Diski.setChecked(False)
    ui.chk_Biyopsi.setChecked(False)
    ui.chk_Chem.setChecked(False)
    ui.chk_Radyografi.setChecked(False)
    ui.chk_Karin_Ultrasonu.setChecked(False)
    ui.chk_C_S.setChecked(False)
    ui.chk_Kalp_Kurdu_Testi.setChecked(False)
    ui.chk_Laym_Titre.setChecked(False)
    ui.chk_Ameliyat_Oncesi_Kan_Tahlili.setChecked(False)
    ui.chk_Idrar_Tahlili.setChecked(False)
    ui.chk_Yankl_Yurek_Gosterimi.setChecked(False)
    ui.chk_Idrar_Gosterimi.setChecked(False)
    ui.chk_Diger3.setChecked(False)
    ui.chk_Yillik_Kontrol.setChecked(False)
    ui.chk_Yavru_Kedi.setChecked(False)
    ui.chk_Uyusukluk.setChecked(False)
    ui.chk_Kusma.setChecked(False)
    ui.chkDis.setChecked(False)
    ui.chk_Ishal.setChecked(False)
    ui.chk_Oksuruk.setChecked(False)
    ui.chk_Hapsirik.setChecked(False)
    ui.chk_Goz_Kontrol.setChecked(False)
    ui.chk_Cerrahi.setChecked(False)
    ui.chk_Kulak_Kontrol.setChecked(False)
    ui.chk_Cilt_Kontrol.setChecked(False)
    ui.chk_Topallik.setChecked(False)
    ui.chk_Nefes_Problemi.setChecked(False)
    ui.chk_Felc.setChecked(False)
    ui.chk_Artan_Istah.setChecked(False)
    ui.chk_Azalan_Istah.setChecked(False)
    ui.chk_Secmeli_Cerrahi.setChecked(False)
    ui.chk_Idrar_Yapma.setChecked(False)
    ui.chk_Diger2.setChecked(False)
    ui.dsb_Agirlik.setValue(0.00)
    ui5.Hasta_Ismi1.clear()
    ui5.Sahip_Adi1.clear()
    ui5.cmb_Cins1.setCurrentIndex(0)
    ui5.fiyat.clear()
    
    curs.execute("SELECT COUNT(*) FROM Anasayfa")
    kayitSayisi = curs.fetchone()
    ui1.kayitsayisi.setText(str(kayitSayisi[0]))


LISTELE()


# -----------ÇIKIŞ-----------#
def CIKIS():
    cevap = QMessageBox.question(penAna, "ÇIKIŞ", "Programdan çıkmak istediğinize emin misiniz?", \
                                 QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:
        conn.close()
        sys.exit(Uygulama.exec_())
        sys.exit(Uygulama1.exec_())
        sys.exit(Uygulama2.exec_())
        sys.exit(Uygulama3.exec_())
        sys.exit(Uygulama4.exec_())
        sys.exit(Uygulama5.exec_())
    else:
        penListe.show()
        

# -----------SİL-----------#
def SIL():
    cevap = QMessageBox.question(penListe, "KAYIT SİL", "Kaydı silmek istediğinize emin misiniz?", \
                                 QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:
        secili = ui1.tblw_HastaBilgi.selectedItems()
        silinecek = secili[6].text()
        try:
            curs.execute("DELETE FROM Anasayfa WHERE SahipTelNo='%s'" % (silinecek))
            conn.commit()

            LISTELE()

            ui1.statusbar.showMessage("KAYIT SİLME İŞLEMİ BAŞARIYLA GERÇEKLEŞTİ...", 10000)
        except Exception as Hata:
            ui1.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı:" + str(Hata))
    else:
        ui1.statusbar.showMessage("Silme işlemi iptal edildi...", 10000)
    

# -----------ARA-----------#
def ARA():
    aranan1 = ui.Ad_Soyad.text()
    aranan2 = ui.Hasta_Ismi.text()
    aranan3 = ui.cmb_Cins.currentText()
    aranan4 = ui.Telefon_Numarasi.text()
    curs.execute(
        "SELECT * FROM Anasayfa WHERE SahipAdi=? OR HastaIsmi=? OR HastaCins=? OR SahipTelNo=? OR (SahipAdi=? AND SahipTelNo=?) OR (HastaIsmi=? AND HastaCins=?)", \
        (aranan1, aranan2, aranan3, aranan4, aranan1, aranan4, aranan2, aranan3))
    conn.commit()
    ui1.tblw_HastaBilgi.clear()
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui1.tblw_HastaBilgi.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))


# -----------GÜNCELLE-----------#

def GUNCELLE():
    cevap = QMessageBox.question(penSikayet, "KAYIT GÜNCELLE", "Kaydı güncellemek istediğinize emin misiniz?", \
                                 QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:
        try:
            secili = ui1.tblw_HastaBilgi.selectedItems()
            _Id = int(secili[0].text())
            _Ad_Soyad = ui.Ad_Soyad.text()
            _Adres = ui.Adres.text()
            _Il = ui.Il.currentText()
            _Ilce = ui.Ilce.currentText()
            _Telefon_Numarasi = ui.Telefon_Numarasi.text()
           
           
            eposta = ui.E_Posta.text() 
            
            match = re.fullmatch(regex, eposta)
            
            

            if match is not None:
                ui.statusbar.showMessage(" " * 3 + "Geçerli Bir E-posta Girildi.", 5000)
                _E_Posta = eposta
                match.group()
                
            else:
               QMessageBox.warning(penAna, "HATA", "Geçersiz Bir E-Posta girildi. Lütfen Tekrar Deneyiniz.",\
                                   QMessageBox.Ok)
            
            _Sicaklik = ui.Sicaklik.text()
            _Kalp_Atisi =ui.Kalp_Atisi.text()
            _Solunum = ui.Solunum.text()
            _cmb_Puan = ui.cmb_Puan.currentText()
            _Hasta_Ismi = ui.Hasta_Ismi.text()
            _dogum_tarihi = ui.dogum_tarihi.date().toString(QtCore.Qt.ISODate)
            _cmb_Cinsiyet = ui.cmb_Cinsiyet.currentText()
            _cmb_Cins = ui.cmb_Cins.currentText()
            _Yavru = ui.Yavru.text()
            _Ad_Soyad1 = _Ad_Soyad
            _Hasta_Ismi1 = _Hasta_Ismi
            _cmb_Cins1 = _cmb_Cins
            
            
          
            
            if ui.rb_normal1.isChecked():
                _AgizBoslugu = "Normal"
            elif ui.rb_anormal1.isChecked():
                _AgizBoslugu = "Anormal"
            
            if ui.rb_normal2.isChecked():
                _Gozler = "Normal"
            elif ui.rb_anormal2.isChecked():
                _Gozler = "Anormal"
                
            if ui.rb_normal3.isChecked():
                _Kulaklar = "Normal"
            elif ui.rb_anormal3.isChecked():
                _Kulaklar = "Anormal"
                
            if ui.rb_normal4.isChecked():
                _BurunBogaz = "Normal"
            elif ui.rb_anormal4.isChecked():
                _BurunBogaz = "Anormal"
                
            if ui.rb_normal5.isChecked():
                _Kalp = "Normal"
            elif ui.rb_anormal5.isChecked():
                _Kalp = "Anormal"
                
            if ui.rb_normal6.isChecked():
                _Sinirler = "Normal"
            elif ui.rb_anormal6.isChecked():
                _Sinirler = "Anormal"
            
            if ui.rb_normal7.isChecked():
                _Akcigerler = "Normal"
            elif ui.rb_anormal7.isChecked():
                _Akcigerler = "Anormal"
            
            if ui.rb_normal8.isChecked():
                _Karin = "Normal"
            elif ui.rb_anormal8.isChecked():
                _Karin = "Anormal"
                
            if ui.rb_normal9.isChecked():
                _LenfDugumleri = "Normal"
            elif ui.rb_anormal9.isChecked():
                _LenfDugumleri = "Anormal"
            
            if ui.rb_normal10.isChecked():
                _Deri = "Normal"
            elif ui.rb_anormal10.isChecked():
                _Deri = "Anormal"
            
            if ui.rb_normal11.isChecked():
                _IskeletKas = "Normal"
            elif ui.rb_anormal11.isChecked():
                _IskeletKas = "Anormal"
                
            if ui.rb_normal12.isChecked():
                _Urogenital = "Normal"
            elif ui.rb_anormal12.isChecked():
                _Urogenital = "Anormal"
            
            _Bulgu_Agiz_Boslugu = ui.Bulgu_Agiz_Boslugu.text()
            _Bulgu_Gozler = ui.Bulgu_Gozler.text()
            _Bulgu__Kulaklar = ui.Bulgu__Kulaklar.text()
            _Bulgu_Burun_Bogaz  = ui.Bulgu_Burun_Bogaz.text()
            _Bulgu_Kalp = ui.Bulgu_Kalp.text()
            _Bulgu_Sinirler = ui.Bulgu_Sinirler.text()
            _Bulgu_Akcigerler = ui.Bulgu_Akcigerler.text()
            _Bulgu_Karin = ui.Bulgu_Karin.text()
            _Bulgu_Lenf_Dugumleri = ui.Bulgu_Lenf_Dugumleri.text()
            _Bulgu_Deri = ui.Bulgu_Deri.text()
            _Bulgu_Iskelet_Kas =  ui.Bulgu_Iskelet_Kas.text()
            _Bulgu_Urogenital = ui.Bulgu_Urogenital.text()
            _de_Tarih = ui.de_Tarih.date().toString(QtCore.Qt.ISODate)
            _cmb_Cinsiyet = ui.cmb_Cinsiyet.currentText()
            _cmb_Cins = ui.cmb_Cins.currentText()

            _Degerlendirme = ui5.Degerlendirme.text()
            _Tedavi_Tavsiyeler = ui5.Tedavi_Tavsiyeler.text()
            _Diger_Sikayetler = ui5.Diger_Sikayetler.text()
            _Gecmis = ui5.Gecmis.text()

            _On_Gozlem = ""
            if ui.chk_Hareket.isChecked():
                _On_Gozlem += "Hareket;"
            if ui.chk_Terli.isChecked():
                _On_Gozlem += "Terli;"
            if ui.chk_Duyarsiz.isChecked():
                _On_Gozlem += "Duyarsız;"
            if ui.chk_Istikrarsiz.isChecked():
                _On_Gozlem += "İstikrarsız;"
            if ui.chk_Stresli.isChecked():
                _On_Gozlem += "Stresli;"
            if ui.chk_Kuru.isChecked():
                _On_Gozlem += "Kuru;"
            if ui.chk_Istikrarli.isChecked():
                _On_Gozlem += "İstikrarlı;"
            if ui.chk_Dinc.isChecked():
                _On_Gozlem += "Dinç;"
            if ui.chk_Sokta.isChecked():
                _On_Gozlem += "Şokta;"
            if ui.chk_Olasi.isChecked():
                _On_Gozlem += "Olası İstikrarsız;"
            if ui.chk_Diger1.isChecked():
                _On_Gozlem += "Diğer;"
            
            
            _Teshisler = ""
            if ui.chk_CBC.isChecked():
                _Teshisler+= "CBC;"
            if ui.chk_T4.isChecked():
                _Teshisler += "T4;"
            if ui.chk_ECG.isChecked():
                _Teshisler += "ECG;"
            if ui.chk_Deri_Testi.isChecked():
                _Teshisler += "Deri Testi;"
            if ui.chk_Felv_Fiv.isChecked():
                _Teshisler += "FELV/FIV;"
            if ui.chk_Diski.isChecked():
                _Teshisler += "Dışkı;"
            if ui.chk_Biyopsi.isChecked():
                _Teshisler += "Biyopsi;"
            if ui.chk_Chem.isChecked():
                _Teshisler += "Chem;"
            if ui.chk_Radyografi.isChecked():
                _Teshisler += "Radyografi;"
            if ui.chk_Karin_Ultrasonu.isChecked():
                _Teshisler += "Karın Ultrasonu;"
            if ui.chk_C_S.isChecked():
                _Teshisler += "Aerobic C ve S;"
            if ui.chk_Kalp_Kurdu_Testi.isChecked():
                _Teshisler += "Kalp Kurdu Testi;"
            if ui.chk_Laym_Titre.isChecked():
                _Teshisler+= "Laym Titre;"
            if ui.chk_Ameliyat_Oncesi_Kan_Tahlili.isChecked():
                _Teshisler += "Ameliyat Öncesi Kan Tahlili;"
            if ui.chk_Idrar_Tahlili.isChecked():
                _Teshisler += "İdrar Tahlili;"
            if ui.chk_Yankl_Yurek_Gosterimi.isChecked():
                _Teshisler += "Yankılı Yürek Gösterimi;"
            if ui.chk_Idrar_Gosterimi.isChecked():
                _Teshisler += "İdrar Gösterimi;"
            if ui.chk_Diger3.isChecked():
                _Teshisler += "Diğer;"
            
            
            _Fiyat=0
            
            if ui.chk_CBC.isChecked():
                _Fiyat += 50
            if ui.chk_T4.isChecked():
                _Fiyat += 55
            if ui.chk_ECG.isChecked():
                _Fiyat += 60
            if ui.chk_Deri_Testi.isChecked():
                _Fiyat += 65
            if ui.chk_Felv_Fiv.isChecked():
                _Fiyat += 70
            if ui.chk_Diski.isChecked():
                _Fiyat += 75
            if ui.chk_Biyopsi.isChecked():
                _Fiyat += 80
            if ui.chk_Chem.isChecked():
                _Fiyat += 85
            if ui.chk_Radyografi.isChecked():
                _Fiyat += 90
            if ui.chk_Karin_Ultrasonu.isChecked():
                _Fiyat += 95
            if ui.chk_C_S.isChecked():
                _Fiyat += 100
            if ui.chk_Kalp_Kurdu_Testi.isChecked():
                _Fiyat += 105
            if ui.chk_Laym_Titre.isChecked():
                _Fiyat += 110
            if ui.chk_Ameliyat_Oncesi_Kan_Tahlili.isChecked():
                _Fiyat += 115
            if ui.chk_Idrar_Tahlili.isChecked():
                _Fiyat += 120
            if ui.chk_Yankl_Yurek_Gosterimi.isChecked():
                _Fiyat += 125
            if ui.chk_Idrar_Gosterimi.isChecked():
                _Fiyat += 130
            if ui.chk_Diger3.isChecked():
                _Fiyat += 40
            
            
            
            _Temel_Sikayetler = ""
            if ui.chk_Yillik_Kontrol.isChecked():
                _Temel_Sikayetler+= "Yıllık Kontrol;"
            if ui.chk_Yavru_Kedi.isChecked():
                _Temel_Sikayetler += "Yavru Kedi;"
            if ui.chk_Uyusukluk.isChecked():
                _Temel_Sikayetler += "Uyuşukluk;"
            if ui.chk_Kusma.isChecked():
                _Temel_Sikayetler += "Kusma;"
            if ui.chkDis.isChecked():
                _Temel_Sikayetler += "Diş;"
            if ui.chk_Ishal.isChecked():
                _Temel_Sikayetler += "İshal;"
            if ui.chk_Oksuruk.isChecked():
                _Temel_Sikayetler += "Öksürük;"
            if ui.chk_Hapsirik.isChecked():
                _Temel_Sikayetler += "Hapşırma;"
            if ui.chk_Goz_Kontrol.isChecked():
                _Temel_Sikayetler += "Göz Kontrol;"
            if ui.chk_Cerrahi.isChecked():
                _Temel_Sikayetler += "Cerrahi;"
            if ui.chk_Kulak_Kontrol.isChecked():
                _Temel_Sikayetler += "Kulak Kontrol;"
            if ui.chk_Cilt_Kontrol.isChecked():
                _Temel_Sikayetler += "Cilt Kontrol;"
            if ui.chk_Topallik.isChecked():
                _Temel_Sikayetler+= "Topallık;"
            if ui.chk_Nefes_Problemi.isChecked():
                _Temel_Sikayetler += "Nefes Problemi;"
            if ui.chk_Felc.isChecked():
                _Temel_Sikayetler += "Felç;"
            if ui.chk_Artan_Istah.isChecked():
                _Temel_Sikayetler += "Artan İştah;"
            if ui.chk_Azalan_Istah.isChecked():
                _Temel_Sikayetler += "Azalan İştah;"
            if ui.chk_Secmeli_Cerrahi.isChecked():
                _Temel_Sikayetler += "Seçmeli Cerrahi;"
            if ui.chk_Idrar_Yapma.isChecked():
                _Temel_Sikayetler += "Artan İçme/İdrar Yapma;"
            if ui.chk_Diger2.isChecked():
                _Temel_Sikayetler += "Diğer;"
                
            _dsb_Agirlik = ui.dsb_Agirlik.value()

            curs.execute("UPDATE AnaSayfa SET Tarih=?, SahipAdi=?, SahipAdres=?, SahipIl=?,   \
                              SahipIlçe=?, SahipTelNo=?, SahipE_Posta=?, HastaIsmi=?, HastaD_Tarihi=?,      \
                              HastaCinsiyet=?, HastaCins=?, HastaYavru=?, HastaAgirlik=?,           \
                              TemelSikayetler=?, Sicaklik=?, KalpAtisi=?, KondisyonPuan=?,              \
                              Solunum=?, AgizBoslugu=?, Gozler=?, Kulaklar=?, BurunBogaz=?,             \
                              Kalp=?, Sinirler=?, Akcigerler=?, Karin=?, LenfDügümler=?, Deri=?,        \
                              IskeletKas=?, Urogenital=?, BulguAgiz=?, BulguGoz=?, BulguKulak=?,            \
                              BulguBurunBogaz=?, BulguKalp=?, BulguSinir=?, BulguAkciger=?, BulguKarin=?,   \
                              BulguLenf=?, BulguDeri=?, BulguIskeletKas=?, BulguUrogenital=?,          \
                              SahipAdSoyad=?, HastaAdi=?, HastaCinsi=?, Teshisler=?, Ongozlem=?, Degerlendirme=?,           \
                              Tedavi=?, Sikayet=?, Gecmis=?, Fiyat=? WHERE Id=?",\
                         ( _de_Tarih, _Ad_Soyad,_Adres, _Il, _Ilce, _Telefon_Numarasi, _E_Posta,
                          _Hasta_Ismi, _dogum_tarihi, _cmb_Cinsiyet, _cmb_Cins, _Yavru, 
                          _dsb_Agirlik, _Temel_Sikayetler, _Sicaklik, _Kalp_Atisi, _cmb_Puan, _Solunum, _AgizBoslugu, _Gozler,     
                          _Kulaklar, _BurunBogaz, _Kalp, _Sinirler, _Akcigerler, _Karin, _LenfDugumleri, _Deri, _IskeletKas,
                          _Urogenital, _Bulgu_Agiz_Boslugu, _Bulgu_Gozler, _Bulgu__Kulaklar, _Bulgu_Burun_Bogaz,                    
                          _Bulgu_Kalp, _Bulgu_Sinirler, _Bulgu_Akcigerler, _Bulgu_Karin, _Bulgu_Lenf_Dugumleri, _Bulgu_Deri,            
                          _Bulgu_Iskelet_Kas, _Bulgu_Urogenital, _Ad_Soyad1, _Hasta_Ismi1, _cmb_Cins1, _Teshisler, _On_Gozlem, _Degerlendirme, _Tedavi_Tavsiyeler,            
                          _Diger_Sikayetler, _Gecmis, _Fiyat, _Id))
            conn.commit()
            LISTELE()
            
        except Exception as Hata:
             ui5.statusbar.showMessage("Şöyle bir hata meydana geldi" + str(Hata))
    else:
         ui5.statusbar.showMessage("Güncelleme iptal edildi", 10000)
         
         

# -----------DOLDUR-----------#
def DOLDUR():
    ui.rb_normal1.setChecked(False)
    ui.rb_normal2.setChecked(False)
    ui.rb_normal3.setChecked(False)
    ui.rb_normal4.setChecked(False)
    ui.rb_normal5.setChecked(False)
    ui.rb_normal6.setChecked(False)
    ui.rb_normal7.setChecked(False)
    ui.rb_normal8.setChecked(False)
    ui.rb_normal9.setChecked(False)
    ui.rb_normal10.setChecked(False)
    ui.rb_normal11.setChecked(False)
    ui.rb_normal12.setChecked(False)
    ui.rb_anormal1.setChecked(False)
    ui.rb_anormal2.setChecked(False)
    ui.rb_anormal3.setChecked(False)
    ui.rb_anormal4.setChecked(False)
    ui.rb_anormal5.setChecked(False)
    ui.rb_anormal6.setChecked(False)
    ui.rb_anormal7.setChecked(False)
    ui.rb_anormal8.setChecked(False)
    ui.rb_anormal9.setChecked(False)
    ui.rb_anormal10.setChecked(False)
    ui.rb_anormal11.setChecked(False)
    ui.rb_anormal12.setChecked(False)
    ui.chk_Hareket.setChecked(False)
    ui.chk_Terli.setChecked(False)
    ui.chk_Duyarsiz.setChecked(False)
    ui.chk_Istikrarsiz.setChecked(False)
    ui.chk_Stresli.setChecked(False)
    ui.chk_Kuru.setChecked(False)
    ui.chk_Istikrarli.setChecked(False)
    ui.chk_Dinc.setChecked(False)
    ui.chk_Sokta.setChecked(False)
    ui.chk_Olasi.setChecked(False)
    ui.chk_Diger1.setChecked(False)
    ui.chk_CBC.setChecked(False)
    ui.chk_T4.setChecked(False)
    ui.chk_ECG.setChecked(False)
    ui.chk_Deri_Testi.setChecked(False)
    ui.chk_Felv_Fiv.setChecked(False)
    ui.chk_Diski.setChecked(False)
    ui.chk_Biyopsi.setChecked(False)
    ui.chk_Chem.setChecked(False)
    ui.chk_Radyografi.setChecked(False)
    ui.chk_Karin_Ultrasonu.setChecked(False)
    ui.chk_C_S.setChecked(False)
    ui.chk_Kalp_Kurdu_Testi.setChecked(False)
    ui.chk_Laym_Titre.setChecked(False)
    ui.chk_Ameliyat_Oncesi_Kan_Tahlili.setChecked(False)
    ui.chk_Idrar_Tahlili.setChecked(False)
    ui.chk_Yankl_Yurek_Gosterimi.setChecked(False)
    ui.chk_Idrar_Gosterimi.setChecked(False)
    ui.chk_Diger3.setChecked(False)
    ui.chk_Yillik_Kontrol.setChecked(False)
    ui.chk_Yavru_Kedi.setChecked(False)
    ui.chk_Uyusukluk.setChecked(False)
    ui.chk_Kusma.setChecked(False)
    ui.chkDis.setChecked(False)
    ui.chk_Ishal.setChecked(False)
    ui.chk_Oksuruk.setChecked(False)
    ui.chk_Hapsirik.setChecked(False)
    ui.chk_Goz_Kontrol.setChecked(False)
    ui.chk_Cerrahi.setChecked(False)
    ui.chk_Kulak_Kontrol.setChecked(False)
    ui.chk_Cilt_Kontrol.setChecked(False)
    ui.chk_Topallik.setChecked(False)
    ui.chk_Nefes_Problemi.setChecked(False)
    ui.chk_Felc.setChecked(False)
    ui.chk_Artan_Istah.setChecked(False)
    ui.chk_Azalan_Istah.setChecked(False)
    ui.chk_Secmeli_Cerrahi.setChecked(False)
    ui.chk_Idrar_Yapma.setChecked(False)
    ui.chk_Diger2.setChecked(False)

    secili = ui1.tblw_HastaBilgi.selectedItems()
    _Id = int(secili[0].text())
    
    yil = int(secili[1].text()[0:4])
    ay = int(secili[1].text()[5:7])
    gun = int(secili[1].text()[8:10])
    ui.de_Tarih.setDate(QtCore.QDate(yil, ay, gun))
    
    ui.Ad_Soyad.setText(secili[2].text())
    ui.Adres.setText(secili[3].text())
    ui.Il.setCurrentText(secili[4].text())
    ui.Ilce.setCurrentText(secili[5].text())
    ui.Telefon_Numarasi.setText(secili[6].text())
    ui.E_Posta.setText(secili[7].text())
    ui.Hasta_Ismi.setText(secili[8].text())
    
    yil1 = int(secili[9].text()[0:4])
    ay1 = int(secili[9].text()[5:7])
    gun1 = int(secili[9].text()[8:10])
    ui.dogum_tarihi.setDate(QtCore.QDate(yil1, ay1, gun1))
    
    ui.cmb_Cinsiyet.setCurrentText(secili[10].text())
    ui.cmb_Cins.setCurrentText(secili[11].text())
    ui.Yavru.setText(secili[12].text())
    ui.dsb_Agirlik.setValue(float(secili[13].text()))
    
    TemelSikayetlerListesi = secili[14].text().split(";")
    for sikayet in TemelSikayetlerListesi:
        if sikayet == "Yıllık Kontrol":
            ui.chk_Yillik_Kontrol.setChecked(True)
        if sikayet == "Yavru Kedi":
            ui.chk_Yavru_Kedi.setChecked(True)
        if sikayet == "Uyuşukluk":
            ui.chk_Uyusukluk.setChecked(True)
        if sikayet == "Kusma":
            ui.chk_Kusma.setChecked(True)
        if sikayet == "Diş":
            ui.chkDis.setChecked(True)
        if sikayet == "İshal":
            ui.chk_Ishal.setChecked(True)
        if sikayet == "Öksürük":
            ui.chk_Oksuruk.setChecked(True)
        if sikayet == "Hapşırma":
            ui.chk_Hapsirik.setChecked(True)
        if sikayet == "Göz Kontrol":
            ui.chk_Goz_Kontrol.setChecked(True)
        if sikayet == "Cerrahi":
            ui.chk_Cerrahi.setChecked(True)
        if sikayet == "Kulak Kontrol":
            ui.chk_Yillik_Kontrol.setChecked(True)
        if sikayet == "Cilt Kontrol":
            ui.chk_Cilt_Kontrol.setChecked(True)
        if sikayet == "Topallık":
            ui.chk_Topallik.setChecked(True)
        if sikayet == "Nefes Problemi":
            ui.chk_Nefes_Problemi.setChecked(True)
        if sikayet == "Diğer":
            ui.chk_Diger2.setChecked(True)
        if sikayet == "Felç":
            ui.chk_Felc.setChecked(True)
        if sikayet == "Artan İştah":
            ui.chk_Artan_Istah.setChecked(True)
        if sikayet == "Azalan İştah":
            ui.chk_Azalan_Istah.setChecked(True)
        if sikayet == "Seçmeli Cerrahi":
            ui.chk_Secmeli_Cerrahi.setChecked(True)
        if sikayet == "Artan İçme/İdrar Yapma":
            ui.chk_Idrar_Yapma.setChecked(True)
        
   
    ui.Sicaklik.setText(secili[15].text())
    ui.Kalp_Atisi.setText(secili[16].text())
    ui.Solunum.setText(secili[17].text())
    ui.cmb_Puan.setCurrentText(secili[18].text())
    
    if secili[19].text() == "Normal":
        ui.rb_normal1.setChecked(True)
        ui.rb_anormal1.setChecked(False)
    if secili[19].text() == "Anormal":
        ui.rb_anormal1.setChecked(True)
        ui.rb_normal1.setChecked(False)
    if secili[20].text() == "Normal":
        ui.rb_normal2.setChecked(True)
        ui.rb_anormal2.setChecked(False)
    if secili[20].text() == "Anormal":
        ui.rb_anormal2.setChecked(True)
        ui.rb_normal2.setChecked(False)
    if secili[21].text() == "Normal":
        ui.rb_normal3.setChecked(True)
        ui.rb_anormal3.setChecked(False)
    if secili[21].text() == "Anormal":
        ui.rb_anormal3.setChecked(True)
        ui.rb_normal3.setChecked(False)
    if secili[22].text() == "Normal":
        ui.rb_normal4.setChecked(True)
        ui.rb_anormal4.setChecked(False)
    if secili[22].text() == "Anormal":
        ui.rb_anormal4.setChecked(True)
        ui.rb_normal4.setChecked(False)
    if secili[23].text() == "Normal":
        ui.rb_normal5.setChecked(True)
        ui.rb_anormal5.setChecked(False)
    if secili[23].text() == "Anormal":
        ui.rb_anormal5.setChecked(True)
        ui.rb_normal5.setChecked(False)
    if secili[24].text() == "Normal":
        ui.rb_normal6.setChecked(True)
        ui.rb_anormal6.setChecked(False)
    if secili[24].text() == "Anormal":
        ui.rb_anormal6.setChecked(True)
        ui.rb_normal6.setChecked(False)
    if secili[25].text() == "Normal":
        ui.rb_normal7.setChecked(True)
        ui.rb_anormal7.setChecked(False)
    if secili[25].text() == "Anormal":
        ui.rb_anormal7.setChecked(True)
        ui.rb_normal7.setChecked(False)
    if secili[26].text() == "Normal":
        ui.rb_normal8.setChecked(True)
        ui.rb_anormal8.setChecked(False)
    if secili[26].text() == "Anormal":
        ui.rb_anormal8.setChecked(True)
        ui.rb_normal8.setChecked(False)
    if secili[27].text() == "Normal":
        ui.rb_normal9.setChecked(True)
        ui.rb_anormal9.setChecked(False)
    if secili[27].text() == "Anormal":
        ui.rb_anormal9.setChecked(True)
        ui.rb_normal9.setChecked(False)
    if secili[28].text() == "Normal":
        ui.rb_normal10.setChecked(True)
        ui.rb_anormal10.setChecked(False)
    if secili[28].text() == "Anormal":
        ui.rb_anormal10.setChecked(True)
        ui.rb_normal10.setChecked(False)
    if secili[29].text() == "Normal":
        ui.rb_normal11.setChecked(True)
        ui.rb_anormal11.setChecked(False)
    if secili[29].text() == "Anormal":
        ui.rb_anormal11.setChecked(True)
        ui.rb_normal11.setChecked(False)
    if secili[30].text() == "Normal":
        ui.rb_normal12.setChecked(True)
        ui.rb_anormal12.setChecked(False)
    if secili[30].text() == "Anormal":
        ui.rb_anormal12.setChecked(True)
        ui.rb_normal12.setChecked(False)
    
    ui.Bulgu_Agiz_Boslugu.setText(secili[31].text())
    ui.Bulgu_Gozler.setText(secili[32].text())
    ui.Bulgu__Kulaklar.setText(secili[33].text())
    ui.Bulgu_Burun_Bogaz.setText(secili[34].text())
    ui.Bulgu_Kalp.setText(secili[35].text())
    ui.Bulgu_Sinirler.setText(secili[36].text())
    ui.Bulgu_Akcigerler.setText(secili[37].text())
    ui.Bulgu_Karin.setText(secili[38].text())
    ui.Bulgu_Lenf_Dugumleri.setText(secili[39].text())
    ui.Bulgu_Deri.setText(secili[40].text())
    ui.Bulgu_Iskelet_Kas.setText(secili[41].text())
    ui.Bulgu_Urogenital.setText(secili[42].text())
    
    ui5.Sahip_Adi1.setText(secili[43].text())
    ui5.Hasta_Ismi1.setText(secili[44].text())
    ui5.cmb_Cins1.setCurrentText(secili[45].text())
    
    TeshislerListesi = secili[46].text().split(";")
    
    for teshis  in TeshislerListesi:
        if teshis == "CBC":
            ui.chk_CBC.setChecked(True)
        if teshis == "T4":
            ui.chk_T4.setChecked(True)
        if teshis == "ECG":
            ui.chk_ECG.setChecked(True)
        if teshis == "Deri Testi":
            ui.chk_Deri_Testi.setChecked(True)
        if teshis == "FELV/FIV":
            ui.chk_Felv_Fiv.setChecked(True)
        if teshis == "Dışkı":
            ui.chk_Diski.setChecked(True)
        if teshis == "Biyopsi":
            ui.chk_Biyopsi.setChecked(True)
        if teshis == "Chem":
            ui.chk_Chem.setChecked(True)
        if teshis == "Radyografi":
            ui.chk_Radyografi.setChecked(True)
        if teshis == "Karın Ultrasonu":
            ui.chk_Karin_Ultrasonu.setChecked(True)
        if teshis == "Aerobic C ve S":
            ui.chk_C_S.setChecked(True)
        if teshis == "Kalp Kuru Testi":
            ui.chk_Kalp_Kurdu_Testi.setChecked(True)
        if teshis == "Laym Titre":
            ui.chk_Laym_Titre.setChecked(True)
        if teshis == "Ameliyat Öncesi Kan Tahlili":
            ui.chk_Ameliyat_Oncesi_Kan_Tahlili.setChecked(True)
        if teshis == "İdrar Tahlili":
            ui.chk_Idrar_Tahlili.setChecked(True)
        if teshis == "Yankılı Yürek Gösterimi":
            ui.chk_Yankl_Yurek_Gosterimi.setChecked(True)
        if teshis == "İdrar Gösterimi":
            ui.chk_Idrar_Gosterimi.setChecked(True)
        if teshis == "Diğer":
            ui.chk_Diger3.setChecked(True)
        
        
        
    
    OngozlemListesi = secili[47].text().split(";")
        
    for gozlem in OngozlemListesi:
        if gozlem == "Hareketli":
            ui.chk_Hareket.setChecked(True)
        if gozlem == "Terli":
            ui.chk_Terli.setChecked(True)
        if gozlem == "Duyarsız":
            ui.chk_Duyarsiz.setChecked(True)
        if gozlem == "İstikrarsız":
            ui.chk_Istikrarsiz.setChecked(True)
        if gozlem == "Stresli":
            ui.chk_Stresli.setChecked(True)
        if gozlem == "Kuru":
            ui.chk_Kuru.setChecked(True)
        if gozlem == "İstikrarlı":
            ui.chk_Istikrarli.setChecked(True)
        if gozlem == "Diğer":
            ui.chk_Diger1.setChecked(True)
        if gozlem == "Dinç":
            ui.chk_Dinc.setChecked(True)
        if gozlem == "Şokta":
            ui.chk_Sokta.setChecked(True)
        if gozlem == "Olası İstikrarsız":
            ui.chk_Olasi.setChecked(True)
    
    
    ui5.Degerlendirme.setText(secili[48].text())   
    ui5.Tedavi_Tavsiyeler.setText(secili[49].text())
    ui5.Diger_Sikayetler.setText(secili[50].text())
    ui5.Gecmis.setText(secili[51].text())
    ui5.fiyat.setText(secili[52].text())
            
            
            
# -----------HAKKINDA-----------#

def HAKKINDA():
    penHakkinda.show()



# -----------SİNYAL-SLOT-----------#
ui.menuhakkinda.triggered.connect(HAKKINDA)
ui4.btnkayit.clicked.connect(KAYIT)
ui1.btn_Listele.clicked.connect(LISTELE)
ui1.btn_Cikis.clicked.connect(CIKIS)
ui1.btn_Kayit_Sil.clicked.connect(SIL)
ui5.btn_Kayit_Ol.clicked.connect(EKLE)
ui5.btnara.clicked.connect(ARA)
ui1.tblw_HastaBilgi.itemSelectionChanged.connect(DOLDUR)
ui5.btn_guncelle.clicked.connect(GUNCELLE)
ui3.btngirisyap.clicked.connect(GIRIS)
ui3.btnkayitolmak.clicked.connect(KAYITAC)
ui3.btncikisyap.clicked.connect(CİKİSYAP)
ui3.btnytube.clicked.connect(YOUTUBE)
ui3.rdsifregosterr.clicked.connect(SIFREGOSTER)
ui4.rdsifregoster.clicked.connect(SIFREGOSTERR)
ui4.btniptal.clicked.connect(IPTALET)
ui1.btn_geri.clicked.connect(GERİ)
ui5.btn_geri1.clicked.connect(GERİİ)
ui5.btn_ileri1.clicked.connect(İLERİİ)
ui.btn_ileri.clicked.connect(İLERİ)


sys.exit(Uygulama.exec_())
sys.exit(Uygulama1.exec_())
sys.exit(Uygulama5.exec_())


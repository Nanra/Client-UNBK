#!/usr/bin/python

# Section for reading braille convert to alphabet
import RPi.GPIO as GPIO
import time
import subprocess as cmd

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pressed = "0"
isivalid = ""
antrian = []
pinbtnValid = 31
pinbtnNext = 5
pinbtnPrev = 29
pinbtnDelete = 32
pinbtnEnter = 3
pinbtnSatu = 36
pinbtnDua = 38
pinbtnTiga = 40
pinbtnEmpat = 37
pinbtnLima = 35
pinbtnEnam = 33
suara = 'google_speech -l id '
suaraEnter = "omxplayer -o local notif/Enter.ogg"
suaraError = "omxplayer -o local notif/Error.ogg"
suaraHapus = "omxplayer -o local notif/Hapus2.ogg"
suaraHapus2 = "omxplayer -o local notif/Hapus.ogg"
belum = "omxplayer -o local notif/belum.ogg"
tandaStrip = "google_speech -l id '....Tanda Strip'"
pinbtn = [pinbtnValid, pinbtnNext,
          pinbtnPrev, pinbtnDelete,
          pinbtnEnter, pinbtnSatu,
          pinbtnDua, pinbtnTiga,
          pinbtnEmpat, pinbtnLima, pinbtnEnam]

# Deklarasi Button Huruf Sebagai OUTPUT
i = 0
while i < len(pinbtn):
    GPIO.setup(pinbtn[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    i += 1

# cmd.call('google_speech -l id "Status Semua PIN OK !"', shell=True)
print "All Pin OK\n"
print "Test Pembacaan Huruf\n"
cmd.call('google_speech -l id "Ini Adalah Menu Pengisian Nama. Isi Nama Anda Dengan Benar"', shell=True)
cmd.call('google_speech -l id "Masukkan Kode Huruf Terlebih Dahulu"', shell=True)
cmd.call('google_speech -l id "Kemudian Teekan Tombol Validasi Untuk Memilih Huruf"', shell=True)
cmd.call('google_speech -l id "Teekan Tombol Enter Untuk Menyimpan Huruf Yang Dipilih"', shell=True)
cmd.call('google_speech -l id "Jika kode huruf tidak sesuai, silahkan teekan tombol hapus"', shell=True)
cmd.call('google_speech -l id "Kemudian Jika Nama sudah sesuai, silahkan tekan tombol Next untuk lanjut ke tahap pengisian nomor ujian"', shell=True)
cmd.call('google_speech -l id "Sekarang silahkan masukkan kode huruf"', shell=True)
print "Masukkan Huruf\n"


# Fungsi Baca Kode Braille
def braille():
    tom1 = str(GPIO.input(pinbtnSatu))
    tom2 = str(GPIO.input(pinbtnDua))
    tom3 = str(GPIO.input(pinbtnTiga))
    tom4 = str(GPIO.input(pinbtnEmpat))
    tom5 = str(GPIO.input(pinbtnLima))
    tom6 = str(GPIO.input(pinbtnEnam))
    n = tom3 + tom2 + tom1 + tom4 + tom5 + tom6
    if n == "111111":
        pass
    else:
        return n

def abjad(n="111111"):
    if n == "110111":
        x = "A"
        #ejaHuruf = "omxplayer -o local Abjad/A.mp3"
    elif n == "100111":
        x = "B"
    elif n == "110011":
        x = "C"
    elif n == "110001":
        x = "D"
    elif n == "110101":
        x = "E"
    elif n == "100011":
        x = "F"
    elif n == "100001":
        x = "G"
    elif n == "100101":
        x = "H"
    elif n == "101011":
        x = "I"
    elif n == "101001":
        x = "J"
    elif n == "010111":
        x = "K"
    elif n == "000111":
        x = "L"
    elif n == "010011":
        x = "M"
    elif n == "010001":
        x = "N"
    elif n == "010101":
        x = "O"
    elif n == "000011":
        x = "P"
    elif n == "000001":
        x = "Q"
    elif n == "000101":
        x = "R"
    elif n == "001011":
        x = "S"
    elif n == "001001":
        x = "T"
    elif n == "010110":
        x = "U"
    elif n == "000110":
        x = "V"
    elif n == "101000":
        x = "W"
    elif n == "010010":
        x = "X"
    elif n == "010000":
        x = "Y"
    elif n == "010100":
        x = "Z"
    elif n == "011110":
        x = "-"
    else:
        x = "NULL"
    return x


def bacainputhuruf():
    baca = braille()
    if baca is None:
        baca
    else:
        return baca


def bacahuruf():
    isi = abjad(n=bacainputhuruf())
    return isi

while True:
    tombolValidasi = str(GPIO.input(pinbtnValid))
    tombolEnter = str(GPIO.input(pinbtnEnter))
    tombolNext = str(GPIO.input(pinbtnNext))
    tombolPrev = str(GPIO.input(pinbtnPrev))
    tombolDelete = str(GPIO.input(pinbtnDelete))
    huruf = bacahuruf()  # Baca Huruf
    if huruf == "NULL":
        bacahuruf()
    else:
        if tombolValidasi is pressed:
            isivalid = huruf
            suaraHuruf = suara + str(isivalid)

            if isivalid is "-":
                cmd.call(tandaStrip, shell=True)
                print isivalid
            cmd.call(suaraHuruf, shell=True)
            print "Isi Valid = ", isivalid
            # print suaraHuruf # Bug Checker
        print huruf,

    if (tombolEnter is pressed) & (isivalid is ""):
        print "Anda Belum Mengisi Huruf"
        cmd.call(suaraError, shell=True)
        cmd.call(belum, shell=True)
        continue

    if tombolEnter is pressed:
        print "Huruf telah disimpan ke antrian"
        antrian.append(isivalid)
        cmd.call(suaraEnter, shell=True)
        print "Antrian = ", antrian
        isivalid = ""

    if (tombolNext is pressed) & (len(antrian) == 0):
        print "Anda tidak bisa lanjutkan, Antrian masih kosong"
        cmd.call(suaraError, shell=True)
        cmd.call('google_speech -l id "Anda belum mengisikan nama!,,.. Isi nama terlebih dahulu !"', shell=True)
        continue


    if tombolNext is pressed:
        kalimat = ''.join(antrian)
        kalimat = '"Nama Anda Adalah : "' + kalimat
        suaraKalimat = suara + kalimat + '",,.. Apakah Nama Tersebut benar ?"'
        cmd.call(suaraKalimat, shell=True)
        cmd.call('google_speech -l id "Pilih tombol validasi jika benar"', shell=True)
        time.sleep(2)
        # Konfirmasi Nama ( Baru sampai disini besok lanjut lagi)
        tombolValidasi2 = str(GPIO.input(pinbtnValid))
        print tombolValidasi2
        if tombolValidasi2 is pressed:
            print "Y"
            cmd.call('google_speech -l id "Anda menekan tombol validasi"', shell=True)
            break
        else:
            continue

    if tombolPrev is pressed:
        cmd.call(suaraHapus, shell=True)
        antrian = []
        print "\nAntrian dihapus kabeh Lur\n"
        cmd.call('google_speech -l id "antrian telah dihapus, sekarang masukkan huruf kembali"', shell=True)
        print "Masukkan Huruf\n"

    if tombolDelete is pressed:
        if len(antrian) is 0:
            print "Antrian Kosong Laek"
            cmd.call(suaraError, shell=True)
            continue
        else:
            cmd.call(suaraHapus2, shell=True)
            antrian.pop()
            print antrian
            if len(antrian) is 0:
                cmd.call('google_speech -l id "antrian telah kosong, sekarang masukkan huruf kembali"', shell=True)

    time.sleep(0.3)

import RPi.GPIO as GPIO
import time
global str

pinbtnValid   = 31
pinbtnNext    = 29
pinbtnPrev    = 32
pinbtnDelete  = 5
pinbtnEnter   = 3
pinbtnSatu    = 36
pinbtnDua     = 38
pinbtnTiga    = 40
pinbtnEmpat   = 37
pinbtnLima    = 35
pinbtnEnam    = 33
pinbtn        = [pinbtnValid, pinbtnNext, pinbtnPrev, pinbtnDelete, pinbtnEnter, pinbtnSatu, pinbtnDua, pinbtnTiga
, pinbtnEmpat, pinbtnLima, pinbtnEnam]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Deklarasi Button Huruf Sebagai OUTPUT
i = 0
while i < len(pinbtn):
	GPIO.setup(pinbtn[i], GPIO.IN,pull_up_down=GPIO.PUD_UP)
	i+=1

print "Test Pembacaan Angka"
print "Masukkan Angka"

##Test Button
#while True:
#	inputValue = GPIO.input(pinbtnValid)
#	if (inputValue == False):
#		print "Tombol Ditekan"
#		time.sleep(0.3)

#Fungsi Baca Kode Braille
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

#Deklarasi Angka
def angka(n="111111",x=""):
	if (n=="110111"):
		x = "1"
	elif (n=="100111"):
		x = "2"
	elif (n=="110011"):
		x = "3"
	elif (n=="100011"):
		x = "4"
	elif (n=="110101"):
		x = "5"
	elif (n=="100011"):
		x = "6"
	elif (n=="100001"):
		x = "7"
	elif (n=="100101"):
		x = "8"
	elif (n=="101011"):
		x = "9"
	elif (n=="101001"):
		x = "0"
	else:
		x = "SALAH"
	return x


def bacaInputAngka():
	    baca = braille()
	    if baca is None:
		        baca
	    else:
		        return baca
	
def bacaAngka():
	isi = angka(n=bacaInputAngka())
	return isi

while True:	
	isiangka = bacaAngka() # Baca Angka
	if isiangka == "SALAH":
		bacaAngka()
	else:
		print isiangka,
	time.sleep(0.3)

#! /usr/bin/python

## Section for testing logical input buttons
import RPi.GPIO as GPIO
import time

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

# Deklarasi Button Huruf Sebagai OUTPUT
i = 0
while i < len(pinbtn):
        GPIO.setup(pinbtn[i], GPIO.IN,pull_up_down=GPIO.PUD_UP)
        i+=1

print "All Pin OK"
def braille(): # Fungsi Baca Push Button Dan Konversi Ke Braille
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
def bacaInput(): # Fungsi Baca Inputan Kode Braille
    baca = braille()
    if baca is None:
        baca
    else:
        print baca


while True:
    bacaInput()
    time.sleep(0.5)

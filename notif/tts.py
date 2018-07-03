from gtts import gTTS

while True:
    nama = raw_input('\nMasukkan nama file : ')
    text = raw_input('Masukkan text : ')

    tts = gTTS(text, lang='id')
    tts.save(nama + '.ogg')
    print ("\nData {}.ogg Tersimpan").format(nama)

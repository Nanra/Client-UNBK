from gtts import gTTS

while True:
    nama = raw_input('\nMasukkan nama file : ')
    text = raw_input('Masukkan text : ')

    tts = gTTS(text, lang='id')
    tts.save(nama + '.mp3')
    print ("\nData {}.mp3 Tersimpan").format(nama)

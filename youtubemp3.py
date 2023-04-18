from pytube import YouTube
import os
link = str(input("Video linkini giriniz: "))
yt = YouTube(link)
print('Title: ', yt.title)
print("İndiriliyor...")
ytmp3 = yt.streams.filter(only_audio=True).first()
print("Kaydetmek istediğiniz dizini giriniz. Girmemeniz durumunda 'İndirilenler' dizinine kaydedilir.")
defaultfolderpath = "İndirilenler"
folder = str(input(">> ")) or defaultfolderpath

out_file = ytmp3.download(output_path=folder)

base,ext = os.path.splitext(out_file)
new_file = base + ".mp3"
os.rename(out_file,new_file)
print("Dosya başarıyla indirildi.")
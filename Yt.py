import pytube 
D_F ="/storage/emulated/Zender/files"
url = input ('Enter url = ')

vid = pytube.YouTube(url)

vd_name=vid.title
print(vd_name)

vd_qt=vid.streams.all()
vd_lt= list(enumerate(vd_qt))
for i in vd_lt:
      print(i)

video=int(input ('Enter one of this number = '))
 
vd_qt[video].download()
print('Successfull')

import geocoder as g
import os as s
import time as t
while True:
  s.system ('color B')
  print ('Введите айпи или введите (Мой айпи) для просмотра вашей гео-локации')
  ipi = input ('>>')
  if ipi == 'Мой айпи':
    print (g.ip('me'))
    geo = g.ip('me')
  else:
    geo = g.ip(ipi)
    print ('Город, страна:')
    print (g.ip(ipi))
  print ('\nШирота и долгота:')
  print (geo.latlng)
  s.system('pause')
  s.system ('cls')

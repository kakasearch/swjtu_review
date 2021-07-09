import piexif,os
def walkFile(file):
  timu = []
  for root, dirs, files in os.walk(file):
    for f in files:
      if f[-4:] == '.jpg':
        addr = os.path.join(root, f).replace('\\','/')
        timu.append(addr)
  return timu

path = os.getcwd()
print(path)
for jpg in walkFile(path):
	piexif.remove(jpg)
	print("{},已经被抹去exif信息。".format(jpg))
print('exfi信息删除完成')

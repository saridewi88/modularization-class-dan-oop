class Teman:
    JUMLAH= 0
def __init__(self, nama, sex):

        self.nama = nama
        self.sex = sex
        self.alamat = ''
        Teman.JUMLAH = Teman.JUMLAH + 1

def __str__(self):
  return ('Nama= %s , sex=%s, alamat=%s' % (self.nama, self.sex, self.alamat))

def berbicara(self):
     print('Hai kamu,nama saya adalah %s. Nama kamu siapa?' % self.nama)

daftar_teman = []
daftar_teman.append(Teman('Sakura','perempuan')
daftar_teman.append(Teman('Naruto','laki-laki')
daftar_teman.append(Teman('Tomoyo','perempuan')
sakura = Teman 'Sakura','tidak tahu')
sakura.alamat = 'Perumahan Mranggen'
sakura.berbicara()
daftar_teman.append(sakura)

print('Jumlah teman %d' % len(daftar_teman))
print('Jumlah teman %d' % Teman.JUMLAH)


# daftar_teman.append('Sakura')
# daftar_teman.append('Naruto')
# daftar_teman.append('tomoyo')
# daftar_teman.append('akira')


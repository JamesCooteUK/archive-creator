import sys, getopt, py7zr, os, tarfile, gzip,pycdlib
from zipfile import ZipFile

try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

def create_zip(file, name):
    zipObj = ZipFile(name+'.zip', 'w')
    zipObj.write(file)
    zipObj.close()

def create_iso(file,name):
    iso = pycdlib.PyCdlib()
    iso.new()
    iso.add_file(file, '/'+name.upper()[0:7]+'.;1')
    iso.write('new.iso')
    iso.close()

def create_gz(file, name):   
    with open(file, 'rb') as f_in, gzip.open(name+'.gz', 'wb') as f_out:
        f_out.writelines(f_in)

def create_bz2(file, name):
    with tarfile.open(name+'.bz2', 'w:bz2') as tar:
        tar.add(file)
    tar.close()

def create_7z(file, name):
    with py7zr.SevenZipFile(name+'.7z', 'w') as z:
        z.writeall(file)
        
def main(argv):
   file = sys.argv[1]
   name = os.path.splitext(os.path.basename(file))[0]
   create_7z(file, name)
   create_bz2(file, name)
   create_gz(file, name)
   create_zip(file, name)
   create_iso(file, name)
   

if __name__ == "__main__":
   main(sys.argv[1:])


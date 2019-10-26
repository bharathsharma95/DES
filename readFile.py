from __future__ import with_statement

""" Function definitions """

def main(file):
    #print(file + " opened in 'rb' mode")
    with open(file, 'rb') as fid:
      byte = fid.read(1)
      fileInBytes = list(byte)
      while byte:
          byte = fid.read(1)
          fileInBytes = fileInBytes + list(byte)
    fid.close()
    return fileInBytes

if '__name__' == '__main__':
    main()
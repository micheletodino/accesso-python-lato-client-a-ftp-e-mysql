from ftplib import FTP  
import os
ftp = FTP('ftp.esempio.it')  
ftp.login('esempio@esempio.it', 'prova')  


# CARTELLA FTP DOVE CARICA I DATI
# change directory to upload
ftp.cwd('/www.esempio.it/dati__python')
# print the content of directory

print("local host DIR: \n")




#   ATTENZIONE!!!! CAMBIARE QUESTA DIRECTORY NELLA VERSIONE FINALE

localdir = 'C:/Users/michele/AppData/Local/Programs/Python/Python38-32/'

files = os.listdir(localdir)
for name in files:
    print(name)
print("\n")

# si ipotizzano 3 file chiamati rana da inviare tramite ftp 
print(ftp.dir())
fp = open("rana-csv1.txt", 'rb')

# upload file
#   ATTENZIONE!!!! CAMBIARE QUESTI FILES NELLA VERSIONE FINALE

ftp.storbinary('STOR %s' % os.path.basename("rana-csv1.txt"), fp, 1024)
ftp.storbinary('STOR %s' % os.path.basename("rana-csv2.txt"), fp, 1024)
ftp.storbinary('STOR %s' % os.path.basename("rana-csv3.txt"), fp, 1024)
# print the content of directory
print("FTP DATA FOLDER (after): \n")
print(ftp.dir())
file.dacancellare=ftp.delete('STOR %s' % os.path.basename("rana-csv1.txt"));
print(file.dacancellare); #per vedere se il file 1 è stato cancellato o meno 
file.dacancellare1=ftp.delete('STOR %s' % os.path.basename("rana-csv2.txt"));
print(file.dacancellare1);  #per vedere se il file 2è stato cancellato o meno 
file.dacancellare2=ftp.delete('STOR %s' % os.path.basename("rana-csv3.txt"));
print(file.dacancellare2);  #per vedere se il file 3 è stato cancellato o meno 

fp.close()
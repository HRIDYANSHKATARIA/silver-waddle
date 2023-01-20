from tkinter import *
from tkinter import filedialog as fd
import hashlib


root = Tk()

root.title("ENCRYPTION AND DECRYPTION")
root.geometry("500x500")

def SHA256():
    print("SHA256 FUNCTION")
    text_file1 = fd.askopenfilename(title="OPEN TEXT FILE", filetypes=(("Text Files","*.txt"),))
    print(text_file1)
    read_file1 = open(text_file1, 'r')
    paragraph1 = read_file1.read()
    file_result1 = hashlib.sha256(paragraph1.encode())
    file_hexd1 = file_result1.hexdigest()
    sha256 = open(text_file1, 'w')
    sha256.write(file_hexd1)
    print(file_hexd1)
    sha256.close()
    
SHA256()

def MD5():
    print("MD5 FUNCTION")
    text_file = fd.askopenfilename(title="OPEN TEXT FILE", filetypes=(("Text Files","*.txt"),))
    print(text_file)
    read_file = open(text_file, 'r')
    paragraph = read_file.read()
    file_result = hashlib.md5(paragraph.encode())
    file_hexd = file_result.hexdigest()
    md5_file = open(text_file, 'w')
    md5_file.write(file_hexd)
    print(file_hexd)
    md5_file.close()

btn = Button(root,text="Apply SHA256",command=SHA256)
btn.place(relx=0.4,rely=0.2,anchor=CENTER)

btn1 = Button(root,text="Apply MD5",command=MD5)
btn1.place(relx=0.6,rely=0.2,anchor=CENTER)
#----mengimpor modul----#
from string import punctuation # mengimpor punctuation dari modul string
from collections import Counter # mengimpor Counter dari modul collections
import random # mengimpor modul random
from htmlFunctions import make_HTML_word, make_HTML_box, print_HTML_file # mengimpor make_HTML_word, make_HTML_box, print_HTML_file dari modul htmlFunctions

#----pembuka dari program sekaligus meminta input nama file yang ingin dibuka dari user----#
print("Program to create word cloud from a text file \nThe result is stored as an HTML file \n")
file_name = input("Please enter the file name: ") # meminta input user untuk nama file
print("\n" + file_name + ": \n50 words in frequency order as (count:word) pairs \n")

#----membuka file dan membersihkan file dari tanda baca dan angka, kemudian membuat semua huruf menjadi lowercase----#
file_inp = open(file_name, "r") # membuka file berdasarkan input user dalam mode "read"
txt_inp = file_inp.read() # membaca seluruh isi file, dan di-assign ke txt_inp
clean_txt_inp = "" # membuat string kosong untuk menyimpan kata-kata yang sudah dibersihkan
digits = "0123456789" # membuat daftar angka untuk dibersihkan
for char in txt_inp:
    for punc in punctuation:
        if char == punc:
            char = char.replace(punc, '') # menghapus karakter jika karakter merupakan tanda baca
    for num in digits:
        if char == num:
            char = char.replace(num, '') # menghapus karakter jika karakter merupakan angka
    char = char.lower() # membuat semua huruf menjadi lowercase
    clean_txt_inp += char #membuat daftar kata-kata yang telah dibersihkan terus ditambahkan ke string seiring loop
    
#----membersihkan file dari kata-kata yang merupakan stop words----#
file_inp_stop = open("stopWords.txt", "r") # membuka file stopWords.txt mode "read"
clean_txt_inp_split = clean_txt_inp.split() # membaca keseluruhan file kemudian men-split kata-kata yang dibersihkan sebelumnya berdasarkan whitespace
txt_inp_stop = file_inp_stop.read().split() # membaca keseluruhan file kemudian men-split kata-kata dalam file stopWords.txt berdasarkan whitespace
for word in txt_inp_stop:
    for another_word in clean_txt_inp_split: 
        if another_word in txt_inp_stop:
            clean_txt_inp_split.remove(another_word) # menghapus kata yang telah dibersihkan sebelumnya jika kata tersebut merupakan stop word
sorted_word_list = sorted(clean_txt_inp_split, reverse = True) # men-sortir kata-kata yang telah dibersihkan dari stop words dari yang terbesar
counter_word = Counter(sorted_word_list).most_common(50) # menghitung jumlah kemunculan kata-kata yang telah diurutkan, dan mengambil top 50

#----mencetak output----#
for i in range((len(counter_word))): 
    print("{:3d} : {:<14s}".format(counter_word[i][1], counter_word[i][0]), end='') # mencetak dengan format value 3 spasi dan key 14 spasi
    if (i+1)%4==0:
        print() # pindah baris jika sudah membuat 4 kolom
print('\n')
holder = input("Please type Enter to continue...") 
file_inp.close() # menutup file_inp
file_inp_stop.close() # menutup file_inp_stop

#----membuat file HTML----#
high_count= counter_word[0][1] # nilai terbesar untuk kemunculan
low_count = counter_word[-1][1] # nilai terkecil untuk kemunculan
counter_word.sort() # mengurutkan berdasarkan abjad
body = '' # membuat string kosong untuk menyimpan body di loop
for word,cnt in counter_word:
    body = body + " " + make_HTML_word(word,cnt,high_count,low_count) #menentukan body untuk box berdasarkan word cloud
box = make_HTML_box(body)  #membuat box di HTML berdasarkan body
file_title = "A Word Cloud of " + file_name
print_HTML_file(box, file_title) # membuat file HTML


 
    



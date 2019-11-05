"""I provide a .zip containing .txt and .docx files
For each file, remove punctuation and stop words
Produce a single .dat file containing the name of the file in quotes, a colon, 
then a list of words separated by commas. 
The list of words per file should be unique. Do not include URLs or phone numbers.
"""
import os
import numpy as np
import nltk
from nltk.corpus import stopwords
import readDocx
import zipfile
import re
with zipfile.ZipFile("week_8_documents.zip","r") as zip_ref:
    zip_ref.extractall()
fileword = open('week_8_document1.docx', 'r')
fileword1 = readDocx.getText('week_8_document1.docx')
filetxt = open('week_8_document2.txt', 'r')
filetxt1 = filetxt.read().replace('\n', '')
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~—–’“”'''
filewordnohttp = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', fileword1, flags=re.MULTILINE)
filetxtnohttp = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', filetxt1, flags=re.MULTILINE)
filewordnohttp1 = re.sub(r'((1-\d{3}-\d{3}-\d{4})|(\(\d{3}\) \d{3}-\d{4})|(\d{3}-\d{3}-\d{4}))$', '', filewordnohttp,flags=re.MULTILINE)
filetxtnohttp1 = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', filetxtnohttp, flags=re.MULTILINE)
file1nopunc = ''.join(c for c in filewordnohttp1 if c not in punctuations).lower()
file2nopunc = ''.join(c for c in filetxtnohttp1 if c not in punctuations).lower()
stopword = stopwords.words('english')
word_tokensdocx = nltk.word_tokenize(file1nopunc)
removing_stopwordsdocx = [word for word in word_tokensdocx if word not in stopword]
word_tokenstext = nltk.word_tokenize(file2nopunc)
removing_stopwordstext = [word for word in word_tokenstext if word not in stopword]
answerdocx = np.array(removing_stopwordsdocx)
finalanswerdocx = np.unique(answerdocx)
answertxt = np.array(removing_stopwordstext)
finalanswertxt = np.unique(answertxt)
final = str(os.path.basename('week_8_document1.docx')) + ":" + str(finalanswerdocx) + "\n" + str(os.path.basename('week_8_document2.txt')) + ":" + str(finalanswertxt)
finalfile = open("finalfile.dat", "w")
finalfile.write(final)
finalfile.close()
finalfile = open("finalfile.dat", "r")
print(finalfile.read())
finalfile.close()
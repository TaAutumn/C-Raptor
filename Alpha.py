import pylatex
import PyPDF2
import aitextgen.aitextgen as ai
import nltk.tokenize as tk
import nltk.stem.porter as stem
from nltk.corpus import stopwords as swords
import nltk
import math
import bs4
from pylatex.utils import italic, bold
import numpy as np
import torch
import torch.nn as nn
from pylatex import Document, Section, Subsection, Tabular, Command
from pylatex import Math, TikZ, Axis, Plot, Figure, Matrix, Alignat
from pylatex.utils import italic
nltk.download('')

print(' ')
print('Loading...')
print('This may take a moment')
pdf_fp_1 = "pdf_data/Classical_Phys.pdf"
pdf1 = open(pdf_fp_1,'rb')
pdf_general_phys = PyPDF2.PdfReader(pdf1)
def all_great_one(file_object,custom_word_filter=False):
    ##Custom Word Filter is to be only used for pdf files like textbooks which have steps or demonstration instructions or figure explanations.
    wfc = ['Step','Figure','Perform','this','Hold','Release','Grab','student','your','Repeat','Record','Try','partner','your','you','Make','Use','Chapter','Switch','?','Compare','Constructing','Drawing','Consider']
    new_book = []
    starting_page=0
    for page in range(file_object.getNumPages()):
        print(' ')
        print('Please wait...')
        print(' ')
        print(' ')
        page2words = file_object.getPage(page+starting_page).extractText()
        sentence_list = tk.sent_tokenize(page2words)
        if custom_word_filter is True:
            new_book.append([])
        nsent = 0
        print('Num Sentences in pg = ',len(sentence_list))
        nrword = 0
        for sentence in sentence_list:
            if custom_word_filter == True:
                word_list = tk.word_tokenize(sentence)
                num_words = len(word_list)
                nsword = 0
                for word in word_list:
                    if word in wfc:
                        nrword+=1
                    elif word not in wfc:
                        nsword+=1
                if nsword == num_words:

                    ##Adds the 'pure' sentences to a new list.
                    ##Pure sentences are the sentences with absolutely no words from the wfc list.
                    new_book[page].append(sentence)
                print(' ')
                print('Total Words Remove: ',nrword)
                print('Stop Sequence')
                input('Press enter to continue')
                print(' ')
            else:
                new_book.append(sentence)
    return new_book
physics_understanding_data=all_great_one(pdf_general_phys,False)

model = ai.aitextgen()
model.save('ai_home')

def training(mdl,data1,data2=[],data3=[],data4=[],data5=[],data6=[],data7=[],data8=[],data9=[],data10=[],learn_rate=0.01):
    mdl.train(data1)


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
phys_dict = {'Classical':'https://arxiv.org/list/physics.class-ph/new',
             ''
            }
f = 'ooga booga'

print(' ')
print('Loading...')
print('This may take a moment')
pdf_fp_1 = r"C:\Users\Shae\PycharmProjects\pythonProject\C-Raptor\PDF Datasets\physics_book.pdf"
pdf1 = open(pdf_fp_1,'rb')
pdf_obj = PyPDF2.PdfReader(pdf1)
def all_great_one(file_object):
    ###Used for training purposes of a physics textbook.
    ##Word Filter Custom (Irrelevant Words)
    wfc = ['Step','Figure','Perform','this','Hold','Release','Grab','student','your','Repeat','Record','Try','partner','your','you','Make','Use','Chapter','Switch','?',
           'Compare','Constructing','Drawing','Consider']
    new_book = []
    starting_page=53
    for page in range(file_object.getNumPages()):
        print(' ')
        print('Please wait...')
        print(' ')
        print(' ')
        page2words = file_object.getPage(page+starting_page).extractText()
        sentence_list = tk.sent_tokenize(page2words)
        new_book.append([])
        nw_bk_pg = new_book[page]
        nsent = 0
        print('Num Sentences in pg = ',len(sentence_list))
        for sentence in sentence_list:
            word_list = tk.word_tokenize(sentence)
            num_words = len(word_list)
            nsword = 0
            for word in word_list:
                if word in wfc:
                    break
                elif word not in wfc:
                    nsword+=1
            if nsword == num_words:
                ##Adds the 'pure' sentences to a new list.
                ##Pure sentences are the sentences with absolutely no words from the wfc list.
                nw_bk_pg.append(sentence)
        print(' ')
        print('|||||||||||||||||||||||||||||||||||||||||||||||||')
        print(nw_bk_pg)
        print('Stop Sequence')
        input('Press enter to continue')
        print('|||||||||||||||||||||||||||||||||||||||||||||||||')
        print(' ')
all_great_one(pdf_obj)

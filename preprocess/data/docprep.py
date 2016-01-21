import math, collections
import logging
import os, glob
import string
import re
import itertools
import numpy
import nltk
from collections import defaultdict
from gensim import corpora, models, similarities
from topia.termextract import tag
from stemming.lovins import stem
from nltk.stem.wordnet import WordNetLemmatizer
import operator

stoplist = []
lmtzr = WordNetLemmatizer()
def main():
    
    path = 'C:\\Users\\shubha\\Downloads\\20NG\\20NG\\preprocess\\talk/'
    fp = open('talk.txt',"w")
    documents = []
    wordn = []
    
    d=""
   
    #training_set=[]
    for file in glob.glob(os.path.join(path, '*')):
        #print file
        
        html = ""

                 
        for line in open(file) :
            html += line         
       
        d+=" "+html
        
    fp.write("%s" % d)
    fp.close()
    
main()

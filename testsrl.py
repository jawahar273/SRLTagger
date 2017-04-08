#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 10:22:51 2017

@author: jawahar
"""

from srlnltk import SennaSRLTagger 
from nltk.tag import SennaTagger
sents = """He killed the man with a knife and murdered him with a dagger.""".split()
path = '/media/jawahar/jon/ubuntu/senna'
from nltk.tag import SennaChunkTagger
from nltk.tag import SennaNERTagger

srltagger = SennaSRLTagger(path)
nertagger = SennaNERTagger(path)
chktagger = SennaChunkTagger(path)
tagger = SennaTagger(path)


#w = s.tag("Are you studying here?".split())
#w = s.tag("""A general interface to the SENNA pipeline that supports any of the operations specified in SUPPORTED OPERATIONS..""".split()) 

#print(tagger.tag(sents))
#print(chktagger.tag(sents))
#print(nertagger.tag(sents))
#print(srltagger.tag(sents))

#s.tag2file("""A general interface to the SENNA pipeline that supports any of the operations specified in SUPPORTED OPERATIONS..""".split())

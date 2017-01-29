#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 10:22:51 2017

@author: jawahar
"""

from srlnltk import SennaSRLTagger 
s = SennaSRLTagger('/media/jawahar/jon/ubuntu/senna')
#w = s.tag("Are you studying here?".split())
w = s.tag("""A general interface to the SENNA pipeline that supports any of the operations specified in SUPPORTED OPERATIONS..""".split())#,file_mode='w')
s.tag2file("""A general interface to the SENNA pipeline that supports any of the operations specified in SUPPORTED OPERATIONS..""".split())
print(w)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: jawahar

misalignment errors:
    This error might caused due to fixed maximum size of the sentences.
    By default it is 1024 token/sentence.
    

"""

orginal_code_url = "http://www.nltk.org/_modules/nltk/classify/senna.html"
abstract_view_of_the_code = "http://www.nltk.org/_modules/nltk/tag/senna.html"

from nltk.classify.senna import Senna
from subprocess import Popen, PIPE
from nltk.compat import text_type, python_2_unicode_compatible
from os import path, sep, environ

@python_2_unicode_compatible
class SennaSRLTagger(Senna):
    
    def __init__(self, path_='', encoding='utf-8'):
        """
        Additional
          line 21: addtional for `SRL` operation
        """
        super(SennaSRLTagger, self).SUPPORTED_OPERATIONS.append('srl')
        super(SennaSRLTagger, self).__init__(path_,  ['srl'], encoding)
        self.operations =  ['srl']
        self._path = path.normpath(path_) + sep
        self._encoding = encoding
        
        exe_file_1 = self.executable(self._path)
        if not path.isfile(exe_file_1):
            # Check for the system environment
            if 'SENNA' in environ:
                #self._path = path.join(environ['SENNA'],'')
                self._path = path.normpath(environ['SENNA']) + sep
                exe_file_2 = self.executable(self._path)
                if not path.isfile(exe_file_2):
                    raise OSError("Senna executable expected at %s or %s but not found" % (exe_file_1,exe_file_2))
        #"""
    def tag_sents(self, sentences):
        
        encoding = self._encoding

        if not path.isfile(self.executable(self._path)):
            raise OSError("Senna executable expected at %s but not found" % self.executable(self._path))


        # Build the senna command to run the tagger
        _senna_cmd = [self.executable(self._path), '-path', self._path, '-usrtokens', '-iobtags']
        _senna_cmd.extend(['-'+op for op in self.operations])

        # Serialize the actual sentences to a temporary string
        _input = '\n'.join((' '.join(x) for x in sentences))+'\n'
        if isinstance(_input, text_type) and encoding:
            _input = _input.encode(encoding)

        # Run the tagger and get the output
        p = Popen(_senna_cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        (stdout, stderr) = p.communicate(input=_input)
        if p.returncode != 0:
            raise RuntimeError('Senna command failed! Details: %s' % stderr)
        return stdout.decode(encoding).split()
        #return tagged_sents       

    def tag_sents2file(self, sentences, file_name, file_mode):
        
        encoding = self._encoding

        if not path.isfile(self.executable(self._path)):
            raise OSError("Senna executable expected at %s but not found" % self.executable(self._path))


        # Build the senna command to run the tagger
        _senna_cmd = [self.executable(self._path), '-path', self._path, '-usrtokens', '-iobtags']
        _senna_cmd.extend(['-'+op for op in self.operations])

        # Serialize the actual sentences to a temporary string
        _input = '\n'.join((' '.join(x) for x in sentences))+'\n'
        if isinstance(_input, text_type) and encoding:
            _input = _input.encode(encoding)

        # Run the tagger and get the output
        file_name = open(str(file_name)+'.txt', file_mode)
        p = Popen(_senna_cmd, stdin=PIPE, stdout=file_name, stderr=PIPE)
        (stdout, stderr) = p.communicate(input=_input)
        # Check the return code.
        if p.returncode != 0:
            raise RuntimeError('Senna command failed! Details: %s' % stderr)
        return p.returncode
        
    def executable(self, base_path):
        """
        There is no change required in this function. 
        """
        return super(SennaSRLTagger, self).executable(base_path)

    def tag(self, tokens):
        return self.tag_sents([tokens])
        
    def tag2file(self, tokens,file_name='testing_file', file_mode='a'):
        '''
          :tokens: tokensized words 
          : return 0: means no errors
        '''
        return self.tag_sents2file([tokens],  file_name, file_mode)
   

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
    
    def __init__(self, path_, encoding='utf-8'):
        """

        """
        if  not super(SennaSRLTagger, self).SUPPORTED_OPERATIONS.count('srl'): 
            super(SennaSRLTagger, self).SUPPORTED_OPERATIONS.append('srl')
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
    def tag_sents_yield(self, sentences, index_s):
        
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
        stdout =  stdout.decode(encoding).split()
        index = stdout.index(index_s)
        length_stdout = len(stdout) 
        for i in range(0, length_stdout, index): 
                yield (index,  stdout[i:i+index])


    def tag_sents(self, sentences, index_s):
        
        encoding = self._encoding
        tagged_sents = []
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
        stdout =  stdout.decode(encoding).split()
        index = stdout.index(index_s) # finding the next word through list index
        length_stdout = len(stdout) 
        for i in range(0, length_stdout, index): 
                tagged_sents.append(( index,  stdout[i:i+index]))

        return tagged_sents   

    def tag_sents2file(self, sentences, file_name, file_mode):
        '''
        :Return: 0 on success on writting file 
        '''
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

    def tag(self, tokens, no_list = False):
        """
         :token: tokenized words
         :no_list: calling a function to generate list or yield object
        """
        if not no_list:
            return self.tag_sents([tokens], tokens[1])

        return self.tag_sents_yield([tokens], tokens[1])

    def tag2file(self, tokens,file_name='testing_file', file_mode='a'):
        '''
          :tokens: tokensized words 
          : return 0: means no errors
        '''
        return self.tag_sents2file([tokens],  file_name, file_mode)
   

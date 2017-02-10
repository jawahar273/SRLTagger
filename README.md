# SRLTagger
Senna is a powerful tool for NLP. Sematic Role Labelling is process using NLP. This process is intergated with Python NLTK

## Requirement

1. NLTK 3.2.1
* Senna

###API

```python
>>> s = SennaSRLTagger()
>>> col_len = len(s.tag('A general interface to the SENNA pipeline that supports any of the operations specified in SUPPORTED OPERATIONS'.split())[0])
>>> col_len
4
>>> #length of the column for a sentence is constant.
[(5, ['A', '-', 'O', 'O', 'B-A0']), (5, ['general', '-', 'O', 'O', 'I-A0']), (5, ['interface', '-', 'O', 'O', 'I-A0']), (5, ['to', '-', 'O', 'O', 'I-A0']), (5, ['the', '-', 'O', 'O', 'I-A0']), (5, ['SENNA', '-', 'O', 'O', 'I-A0']), (5, ['pipeline', '-', 'O', 'O', 'I-A0']), (5, ['that', '-', 'B-R-A0', 'O', 'I-A0']), (5, ['supports', 'supports', 'B-V', 'O', 'I-A0']), (5, ['any', '-', 'B-A1', 'B-A1', 'I-A0']), (5, ['of', '-', 'I-A1', 'I-A1', 'I-A0']), (5, ['the', '-', 'I-A1', 'I-A1', 'I-A0']), (5, ['operations', '-', 'I-A1', 'I-A1', 'I-A0']), (5, ['specified', 'specified', 'O', 'B-V', 'O']), (5, ['in', '-', 'O', 'B-AM-LOC', 'O']), (5, ['SUPPORTED', 'SUPPORTED', 'O', 'I-AM-LOC', 'B-V']), (5, ['OPERATIONS..', '-', 'O', 'I-AM-LOC', 'B-A1'])]
```
### SennaSRKTagger.tag(token, no_list=False)
This method genetare the tagged SRL words on the attribute it has been passed. The sentence should be word tokenize.

1. To generate `no_list` must be `True` and a default one.
* To geneate a `yield` object `no_list` must be `False`.
 
### SennaSRKTagger.tag2file(tokens,file_name='testing_file.txt', file_mode='w')
 Generate text file with given name and file mode for writing the file. If you are using multiple sentence the change the `file_mode` to 'a'. 

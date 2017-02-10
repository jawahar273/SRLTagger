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
```
###SennaSRKTagger.tag(token, no_list=False)
This method genetare the tagged SRL words on the attribute it has been passed. The sentence should be word tokenize.
1. To generate `no_list` must be `True` and a default one.
* To geneate a `yield` object `no_list` must be `False`.
 

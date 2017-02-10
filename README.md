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
>>> length of the column for a sentence is constant.
```

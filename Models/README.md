# Distributional Analysis of Function Words

We have trained various models on test subcorpus (round 2000000 tokens) such as CBOW, Skip-gram, GloVe and AdaGram. Code fore preprocessing and results of training can be seen in file Models.ipynb. It takes pickle file with ruWAC markup and also uses .xls file with sample of sentences from Russian National Corpus. Returns four trained models.

We also decided to use pre-trained BERT to estimate its efficiency. The results can be found in BERT.ipynb. Before launching this notebook you need to download pre-trained multilingual BERT from official BERT repository and download file tokenization.py from this repository.

File 21_century.txt is an example of a parsed text.

tojest.html is a visualisation of the 10 nearest neighbours of "то есть" in CBOW dictionary. It is an output file of Models.ipynb file. Vec2Graph package has been used for visualisation, thus it need to be installed before launching.

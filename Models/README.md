# Distributional Analysis of Function Words

We have trained various models on test subcorpus (round 2000000 tokens) such as CBOW, Skip-gram, GloVe and AdaGram. Code fore preprocessing and results of training can be seen in file Models.ipynb.

We also decided to use pre-trained BERT to estimate its efficiency. The results can be found in BERT.ipynb. Before launching this notebook you need to download pre-trained multilingual BERT and download file tokenization.py from this repository.

File 21_century.txt is an example of a parsed text.

tojest.html is a visualisation of the 10 nearest neighbours of "то есть" in CBOW dictionary. Vec2Graph package has been used for visualisation.

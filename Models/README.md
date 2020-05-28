# Distributional Analysis of Function Words

We have trained various models on test subcorpus (round 2000000 tokens) such as CBOW, Skip-gram, GloVe and AdaGram. Code fore preprocessing and results of training can be seen in file Models.ipynb.

We also decided to use pre-trained BERT to estimate its efficiency. The results can be found in BERT.ipynb. Before launching his notebook you need to download pre-traind multilingual BERT and download file tokenization.py from this repository.

File 21_century.txt is an example of parsed text.

тоесть.html is a visualisation of 10 nearest neighbours of "то есть" in CBOW dictionary. Vec2Graph package has been used for visualisation.

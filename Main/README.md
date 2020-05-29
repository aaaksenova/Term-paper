# Distributional Anaysis of Function Words

Parse_corpus.py is a file for preparing ruWAC tokens and tags as a training corpus.

Model_corpus.py is a function for training CBOW model on preprocessed corpus.

Term_paper.ipynb is the most important code for this project. This code was created and launched in a linghub server and uses CBOW model trained on ruWAC. It requires quite a significant computer perfomance.
There are several work stages in this notebook:

1. Similarity count

    Two functions that estimate cosine similarities of contexts for sentences with "то есть". Results are used in Similarity.ipynb.

2. Classificator "from scratch"

    Our function wich predicts meaning of "то есть" in particular context based on context part similarity.

3. Sklearn Classificators for multilabled classification

4. Sklearn Classificators for binary classification (discourse VS conjunction)

5. Visualisation

# Distributional Anaysis of Function Words

Parse_corpus.py is a file for preparing ruWAC tokens and tags as a training corpus. It processes pickle file with text, morphological and syntactical marcup. Returns .txt file with lemmatized sentences.

Model_corpus.py is a function for training CBOW model on preprocessed corpus. Using .txt file with preprocessed corpus returns .bin file with CBOW model.

Term_paper.ipynb is the most important code for this project. It was created and launched in a linghub server and uses CBOW model trained on ruWAC. It requires quite a significant computer perfomance.
There are several work stages in this notebook:

1. Similarity count

    Two functions that estimate cosine similarities of contexts for sentences with "то есть". Results are used in Similarity.ipynb. Takes .txt file with tokens, lemmas and POS tags as an input. Returns two files with lists of word-to-wotd and context-to-context similarities respectively.

2. From scratch classificator

    Our function wich predicts meaning of "то есть" in particular context based on context part similarity. Takes sentences and their tags as a train set and then uses another .txt file with a list of sentences for prediction as a control set.

3. Sklearn Classificators for multilabled classification

4. Sklearn Classificators for binary classification (discourse VS conjunction)

5. Visualisation

    Returns t-SNE visualisation of word vectors and context vectors as .png images.

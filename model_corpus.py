import gensim
from gensim.models import word2vec
from pprint import pprint

f = 'lemmas.txt'
data = gensim.models.word2vec.LineSentence(f)
model_cbow = gensim.models.Word2Vec(data, size=300, window=5, min_count=5, iter=50)
model_cbow.init_sims(replace=True)
model_path = "to.bin"

print("Saving model...")
model_cbow.wv.save_word2vec_format(model_path, binary=True)

pprint(model_cbow.wv.most_similar("тоесть", topn=50))

# AUTOGENERATED! DO NOT EDIT! File to edit: 01_descriptive_analysis.ipynb (unless otherwise specified).

__all__ = ['describer', 'describer', 'describer']

# Cell
from newstrends import loader

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from collections import Counter
import numpy as np

# Cell
class describer(loader.article_holder):
    "inherit everything from article_holder including init"

    subclass="describer"
    vectorizer=None


# Cell
class describer(describer):
    "Add in vectorize"

    def fitVectorizer(self, vectorizer:CountVectorizer=CountVectorizer, ngram_range=(1,2), max_features=10000):
        try:
            _ = self.df[:1].quickReplace
        except:
            raise Exception("No article data found")

        self.vectorizer=vectorizer(stop_words=self.stopwords, ngram_range=ngram_range, max_features=max_features).fit(self.df.quickReplace)

    def getTopNWords(self, topN = 10, lastDate=None, window=None, source=None):
        " get topN important words for each publication "

        "check if properly formatted"
        if type(self.df) != pd.core.frame.DataFrame:
            raise Exception("Dataframe not loaded")
        if self.vectorizer == None:
            raise Exception("No vectorizer found")


        "Get Dataframe for source and time period"
        sources=source
        if source==None:
            sources=[x for x in self.df.source.unique()]
        df = self.df[self.df.source.isin(sources)]

        "get counts of features from count vectorizer"
        X = self.vectorizer.transform(df.quickReplace)
        vocab = list(self.vectorizer.get_feature_names())
        counts = X.sum(axis=0).A1
        counts = Counter(dict(zip(vocab, counts)))

        return counts.most_common(10)


# Cell
class describer(describer):
    "Now having cooccurances could be nice"

    def generateCoOccurances(self, pubList = ["newyorktimes", "foxnews", "washingtonpost", "cnn", "breitbart", "abcnews", "dailycaller"], verbose=False, topK:"int<100" = 20):
        " get cooccurances of terms in my df, up to 100"

        if type(self.df) != pd.core.frame.DataFrame:
            raise Exception("Dataframe not loaded")
        if self.vectorizer == None:
            raise Exception("No vectorizer found")

        vectorizer = CountVectorizer(stop_words=self.stopwords, max_features=10000).fit(self.df.quickReplace)

        # get the transformed DF
        X = vectorizer.transform(self.df.quickReplace)
        X[X > 0] = 1

        coOccurance = (X.T * X)
        coOccurance.setdiag(0)
        d = coOccurance.todense()

        checkLength = topK*2
        if checkLength > 100:
            checkLength = 100

        top_prs = np.dstack(np.unravel_index(np.argpartition(d.ravel(),-checkLength)[:,-checkLength:],d.shape))[0]

        vals = []
        keys = vectorizer.get_feature_names()
        for pair in top_prs:
            newEntry = [keys[pair[0]], keys[pair[1]]]
            if newEntry not in vals:
                vals.append(newEntry)
            if len(vals) >= topK:
                break

        #So now for each day for each time period I want to math out the co-occurances!
        return vals

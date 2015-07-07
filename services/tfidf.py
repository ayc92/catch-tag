from collections import Counter
from collections import defaultdict
import math


class TfIdfCalculator(object):
    def _get_tf_dict(self, doc):
        """
        Calculate the term frequency for each word in the given document.

        Args:
            doc {list<string>} - The document represented as a list of words.

        Returns:
            A dict mapping word -> tf value
        """
        word_to_tf = Counter()

        for word in doc:
            word_to_tf[word] += 1

        max_count = word_to_tf.most_common(1)[0][1]

        for word, count in word_to_tf.iteritems():
            word_to_tf[word] = 0.5 * (1 + word_to_tf[word] / max_count)

        return word_to_tf

    def _get_idf_dict(self, words, docs):
        """
        Calculate the inverse document frequency for each word in the given list of words.

        Args:
            words {list[string]} - A list of words
            docs {list[list[string]]} - A list of documents represented as lists of words.

        Returns:
            A dict mapping word -> idf value
        """
        word_to_idf = Counter()
        num_docs = len(docs)

        for word in words:
            for doc in docs:
                if word in doc:
                    word_to_idf[word] += 1
            word_to_idf[word] = math.log(num_docs / word_to_idf[word])

        return word_to_idf

    def get_tf_idf(self, docs):
        """
        Calculate the TF-IDF for each document-word pair.

        Args:
            docs {dict[int->list[string]]} - The documents to calculate tf-idf for.

        Returns:
            A dict mapping doc_id -> a dict mapping word -> tf-idf value
        """
        doc_to_tfidf_dict = defaultdict(lambda: {})
        for doc_id, doc in docs.iteritems():
            tf_dict = self._get_tf_dict(doc)
            idf_dict = self._get_idf_dict(tf_dict.keys(), docs.values())

            for word in tf_dict:
                doc_to_tfidf_dict[doc_id][word] = tf_dict[word] * idf_dict[word]

        return doc_to_tfidf_dict

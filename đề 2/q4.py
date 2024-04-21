from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(doc1, doc2):
    vectorizer = TfidfVectorizer().fit_transform([doc1, doc2])
    vectors = vectorizer.toarray()
    csim = cosine_similarity(vectors)
    return csim[0,1]

doc1 = "John lives in Canada"
doc2 = "James lives in America, though he's not from there"

similarity = calculate_similarity(doc1, doc2)
print(f"The similarity between the two documents is {similarity}")
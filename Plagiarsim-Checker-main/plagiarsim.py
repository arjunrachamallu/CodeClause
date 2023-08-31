import os
import docx2txt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# List of file paths
file_paths = [
    "C:\\Users\\arjun\\OneDrive\\Desktop\\text1.docx",
    "C:\\Users\\arjun\\OneDrive\\Desktop\\text2.docx"
]

# Read the contents of the files using docx2txt
sample_contents = [docx2txt.process(file_path) for file_path in file_paths]

# Vectorization using TfidfVectorizer
vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()

vectors = vectorize(sample_contents)
s_vectors = list(zip(file_paths, vectors))

# Define similarity function using cosine_similarity
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

def check_plagiarism():
    results = set()
    global s_vectors
    for sample_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((sample_a, text_vector_a))
        del new_vectors[current_index]
        for sample_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            sample_pair = sorted((sample_a, sample_b))
            score = sample_pair[0], sample_pair[1], sim_score
            results.add(score)
    return results

for data in check_plagiarism():
    print(data)

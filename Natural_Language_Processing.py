import spacy
from pymongo import MongoClient

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.stem_learning

# Fetch student interactions
interactions = db.student_interactions.find()

for interaction in interactions:
    doc = nlp(interaction['question'])
    print(f"Processed Question: {doc.text}")

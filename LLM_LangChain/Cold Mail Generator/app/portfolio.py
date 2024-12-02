import pandas as pd
import uuid
import chromadb


class Portfolio:
    def __init__(self,filepath='resource/my_portfolio.csv'):
        self.cv = pd.read_csv(filepath)
        self.client = chromadb.PersistentClient('vectorstore')
        self.collection = self.client.get_or_create_collection(name='portfolio')

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.cv.iterrows():
                self.collection.add(
                    documents=row['Techstack'],
                    metadatas={
                        "links":row['Links']
                        },
                    ids=[str(uuid.uuid4())]
        )
    
    def query_links(self, skills):
        return self.collection.query(
                    query_texts=skills,
                    n_results=2
                    ).get('metadatas', [])
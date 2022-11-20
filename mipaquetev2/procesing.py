import pickle
from urllib.request import urlopen


def get_pipeline(model=None, path : str = None) -> pickle:
    """
    Obtiene el pipeline desde un modelo o bien desde una URL
    En caso de que se pasen por ambos parámetros, tendrá preferencia el modelo.
    """
    if model:
        return pickle.load(model)
    
    if path:
        return pickle.load(urlopen(path))

def fit(pipeline, X, y):
    """Entrenamiento del pipeline"""
    pipeline.fit(X, y)

def export(pipeline, file):
    """export del pipeline"""
    with open(file, 'wb') as f:
        pickle.dump(pipeline, f)

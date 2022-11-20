from mipaquetev2 import procesing
import pickle
from pathlib import Path
from urllib.request import urlopen



def test_model_export():
    """Comprueba que existe el modeloe exportado"""
    path = "models/titanic_model.pkl"
    pipeline = procesing.get_pipeline()
    procesing.export(pipeline, path)

    assert Path(path).is_file()



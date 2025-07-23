from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class BinaryMapper(BaseEstimator, TransformerMixin):
    def __init__(self, mapping=None):
        # mapping doit être un dict : {valeur: code, ...}
        self.mapping = mapping or {}

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Pour chaque colonne reçue, faire le mapping correspondant
        mapped = []
        for idx, colname in enumerate(X.columns):
            col_map = self.mapping[colname]
            mapped_col = X.iloc[:, idx].map(col_map)
            mapped.append(mapped_col)

        # Concaténer horizontalement et convertir en numpy array
        return np.column_stack(mapped)

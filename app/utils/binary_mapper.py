from sklearn.base import BaseEstimator, TransformerMixin

# Création d'une classe de transformation pour le genre
class BinaryMapper(BaseEstimator, TransformerMixin):
    def __init__(self, mapping=None):
        # mapping doit être un dict : {colonne: {valeur: code, ...}, ...}
        self.mapping = mapping or {} 

    def fit(self, X, y=None):
        return self  # pas d'apprentissage nécessaire

    def transform(self, X):
        X_ = X.copy()
        for col, col_map in self.mapping.items():
            X_[col] = X_[col].map(col_map)
        return X_
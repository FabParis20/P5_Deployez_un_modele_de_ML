from pydantic import BaseModel, conint, confloat
from typing import Literal

class InputData(BaseModel):
    age: conint(ge=18, le=100)
    revenu_mensuel: conint(ge=0)
    genre_binaire: Literal[0, 1]
    statut_marital: str
    departement: str
    poste: str
    nombre_experiences_precedentes: conint(ge=0)
    annee_experience_totale: conint(ge=0)
    annees_dans_l_entreprise: conint(ge=0)
    annees_dans_le_poste_actuel: conint(ge=0)
    satisfaction_employee_environnement: conint(ge=1, le=4)
    note_evaluation_precedente: conint(ge=1, le=4)
    niveau_hierarchique_poste: conint(ge=1, le=10)
    satisfaction_employee_nature_travail: conint(ge=1, le=4)
    satisfaction_employee_equipe: conint(ge=1, le=4)
    satisfaction_employee_equilibre_pro_perso: conint(ge=1, le=4)
    note_evaluation_actuelle: conint(ge=1, le=4)
    augementation_salaire_precedente: confloat(ge=0.0, le=1.0)
    nombre_participation_pee: conint(ge=0)
    nb_formations_suivies: conint(ge=0)
    annees_depuis_la_derniere_promotion: conint(ge=0)
    annes_sous_responsable_actuel: conint(ge=0)
    niveau_education: conint(ge=1, le=5)
    domaine_etude: str
    distance_domicile_travail: confloat(ge=0.0)
    frequence_deplacement_num: Literal[0, 1, 2]  # Aucun=0, Occasionnel=1, Fréquent=2
    taux_de_formation: confloat(ge=0.0)
    tranche_age: Literal["Junior", "Intermédiaire", "Senior"]
    heures_supplementaires_binaire: Literal[0, 1]
    age_revenu: confloat(ge=0.0)
    interaction_distance_heures_sup: confloat(ge=0.0)
    interaction_satisfaction_anciennete: confloat(ge=0.0)
    ratio_sous_responsable: confloat(ge=0.0)
    ratio_stagnation: confloat(ge=0.0)
    satisfaction_moyenne: confloat(ge=0.0, le=4.0)
    surmenage_transports: confloat(ge=0.0)

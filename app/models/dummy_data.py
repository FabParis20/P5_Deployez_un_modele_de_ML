# app/models/dummy_data.py

DUMMY_DATA = {
    # Variables numériques continues (float)
    "revenu_mensuel": 0.0,
    "age": 0.0,
    "annee_experience_totale": 0.0,
    "annees_dans_l_entreprise": 0.0,
    "annees_dans_le_poste_actuel": 0.0,
    "annes_sous_responsable_actuel": 0.0,
    "nombre_participation_pee": 0.0,
    "ratio_stagnation": 0.0,
    "ratio_sous_responsable": 0.0,
    "age_revenu": 0.0,
    "satisfaction_moyenne": 0.0,
    "interaction_satisfaction_anciennete": 0.0,
    "taux_de_formation": 0.0,
    "interaction_distance_heures_sup": 0.0,
    "surmenage_transports": 0.0,
    "revenu_stable": 0.0,
    "distance_domicile_travail": 0.0,
    "nb_formations_suivies": 0.0,
    "delta_eval_x_revenu_stable": 0.0,
    "delta_evaluation": 0.0,
    "nombre_experiences_precedentes": 0.0,
    "annees_depuis_la_derniere_promotion": 0.0,
    "frequence_deplacement_num": 0.0,
    "augmentation_salaire_precedente": 0.0,

    # Variables catégorielles textuelles (OneHotEncoder)
    "statut_marital": "Célibataire",
    "departement": "Consulting",
    "poste": "Consultant",
    "domaine_etude": "Marketing",
    "distance_domicile_travail_qcut": "moyen_loin",
    "tranche_age": "Intermediaire",

    # Ordinal numérique (int)
    "niveau_education": 2,
    "satisfaction_employee_environnement": 3,
    "note_evaluation_precedente": 3,  # ✅ int attendu
    "niveau_hierarchique_poste": 1,
    "satisfaction_employee_nature_travail": 4,
    "satisfaction_employee_equipe": 3,
    "satisfaction_employee_equilibre_pro_perso": 2,
    "note_evaluation_actuelle": 3,    # ✅ int attendu

    # Ordinal texte
    "frequence_deplacement": "Frequent",

    # Binaire texte
    "genre": "M",
    "heures_supplementaires": "Oui",

    # Binaire déjà transformé (pass-through)
    "heures_supplementaires_binaire": 1
}

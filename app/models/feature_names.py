# =============================================
# ✅ Colonnes finales utilisées pour la prédiction
# (celles en sortie du pipeline de transformation)
# =============================================

FEATURE_NAMES = [

    # 1️⃣ MinMaxScaler (24 variables numériques continues normalisées)
    "revenu_mensuel",
    "age",
    "annee_experience_totale",
    "annees_dans_l_entreprise",
    "annees_dans_le_poste_actuel",
    "annes_sous_responsable_actuel",
    "nombre_participation_pee",
    "ratio_stagnation",
    "ratio_sous_responsable",
    "age_revenu",
    "satisfaction_moyenne",
    "interaction_satisfaction_anciennete",
    "taux_de_formation",
    "interaction_distance_heures_sup",
    "surmenage_transports",
    "revenu_stable",
    "distance_domicile_travail",
    "nb_formations_suivies",
    "delta_eval_x_revenu_stable",
    "delta_evaluation",
    "nombre_experiences_precedentes",
    "annees_depuis_la_derniere_promotion",
    "frequence_deplacement_num",
    "augmentation_salaire_precedente",

    # 2️⃣ OneHotEncoder (28 variables catégorielles transformées en dummies)
    "statut_marital_Célibataire",
    "statut_marital_Divorcé(e)",
    "statut_marital_Marié(e)",
    "departement_Commercial",
    "departement_Consulting",
    "departement_Ressources Humaines",
    "poste_Assistant de Direction",
    "poste_Cadre Commercial",
    "poste_Consultant",
    "poste_Directeur Technique",
    "poste_Manager",
    "poste_Représentant Commercial",
    "poste_Ressources Humaines",
    "poste_Senior Manager",
    "poste_Tech Lead",
    "domaine_etude_Autre",
    "domaine_etude_Entrepreunariat",
    "domaine_etude_Infra & Cloud",
    "domaine_etude_Marketing",
    "domaine_etude_Ressources Humaines",
    "domaine_etude_Transformation Digitale",
    "distance_domicile_travail_qcut_loin",
    "distance_domicile_travail_qcut_moyen_loin",
    "distance_domicile_travail_qcut_moyen_proche",
    "distance_domicile_travail_qcut_proche",
    "tranche_age_Intermédiaire",
    "tranche_age_Junior",
    "tranche_age_Senior",

    # 3️⃣ Ordinal Numérique
    "niveau_education",
    "satisfaction_employee_environnement",
    "note_evaluation_precedente",
    "niveau_hierarchique_poste",
    "satisfaction_employee_nature_travail",
    "satisfaction_employee_equipe",
    "satisfaction_employee_equilibre_pro_perso",
    "note_evaluation_actuelle",

    # 4️⃣ Ordinal Texte
    "frequence_deplacement",

    # 5️⃣ BinaryMapper
    "genre_binaire",
    "heures_supplementaires_binaire",

    # 6️⃣ BinaryPass
    "heures_supplementaires_binaire_passthrough"
]


# =============================================
# 🏗️ Colonnes brutes attendues en entrée du pipeline
# (avant toute transformation)
# =============================================

INPUT_FEATURES = [
    "revenu_mensuel",
    "age",
    "annee_experience_totale",
    "annees_dans_l_entreprise",
    "annees_dans_le_poste_actuel",
    "annes_sous_responsable_actuel",
    "nombre_participation_pee",
    "ratio_stagnation",
    "ratio_sous_responsable",
    "age_revenu",
    "satisfaction_moyenne",
    "interaction_satisfaction_anciennete",
    "taux_de_formation",
    "interaction_distance_heures_sup",
    "surmenage_transports",
    "revenu_stable",
    "distance_domicile_travail",
    "nb_formations_suivies",
    "delta_eval_x_revenu_stable",
    "delta_evaluation",
    "nombre_experiences_precedentes",
    "annees_depuis_la_derniere_promotion",
    "frequence_deplacement_num",
    "augmentation_salaire_precedente",
    "statut_marital",
    "departement",
    "poste",
    "domaine_etude",
    "distance_domicile_travail_qcut",
    "tranche_age",
    "niveau_education",
    "satisfaction_employee_environnement",
    "note_evaluation_precedente",
    "niveau_hierarchique_poste",
    "satisfaction_employee_nature_travail",
    "satisfaction_employee_equipe",
    "satisfaction_employee_equilibre_pro_perso",
    "note_evaluation_actuelle",
    "frequence_deplacement",
    "genre",
    "heures_supplementaires",
    "heures_supplementaires_binaire"
]

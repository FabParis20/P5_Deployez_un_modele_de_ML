# -----------------------------------------------
# 📁 Création des dossiers
# -----------------------------------------------

# Crée le dossier sql s’il n’existe pas
if (-Not (Test-Path -Path "sql")) {
    New-Item -ItemType Directory -Path "sql" | Out-Null
}

# Crée le dossier app\db s’il n’existe pas
if (-Not (Test-Path -Path "app\db")) {
    New-Item -ItemType Directory -Path "app\db" -Force | Out-Null
}

# -----------------------------------------------
# 📄 Création des fichiers SQL
# -----------------------------------------------

$files_sql = @(
    "sql\01_create_tables.sql",
    "sql\02_insert_data.sql",
    "sql\03_joins_fusion.sql",
    "sql\04_feature_engineering.sql",
    "sql\05_export_final.sql",
    "sql\06_register_inputs_outputs.sql",
    "sql\README.md"
)

foreach ($file in $files_sql) {
    if (-Not (Test-Path -Path $file)) {
        New-Item -ItemType File -Path $file | Out-Null
    }
}

# -----------------------------------------------
# 🐍 Création des fichiers Python (bonus ORM)
# -----------------------------------------------

$files_py = @(
    "app\db\models.py",
    "app\db\session.py",
    "app\db\insert_data.py",
    "app\db\transformations.py",
    "app\db\__init__.py"
)

foreach ($file in $files_py) {
    if (-Not (Test-Path -Path $file)) {
        New-Item -ItemType File -Path $file | Out-Null
    }
}

Write-Host "✅ Structure PostgreSQL + ORM créée avec succès."

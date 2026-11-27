# TP3 — Intégration Continue (FastAPI)

API **FastAPI** développée dans le cadre du module *Plateforme collaborative et intégration continue (DevOps)*.

## 1. Lancer l'application en local

Activez votre environnement virtuel et installez les dépendances :

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install fastapi uvicorn pytest pytest-cov httpx pylint
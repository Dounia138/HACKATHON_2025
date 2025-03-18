# Projet ERICSSON

## Description
Ce projet est une API basée sur FastAPI qui utilise CrewAI pour assigner des tâches à différents agents. L'API reçoit une requête, effectue une recherche sur le web, résume les résultats et structure l'information sous forme d'article.

## 🚀 Installation et exécution
### Prérequis
- Python 3.9+
- Anaconda (optionnel)
- Pip

### 1️⃣ Installation des dépendances  

```bash

1. Clone le projet :
   ```bash
   git clone https://github.com/ton-repo/hackathon2025.git
   cd hackathon2025/backend
   ```
2. Installe les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
pip install -r requirements.txt

# Démarrer le backend
cd backend
uvicorn main:app --host 127.0.0.1 --port 8080
ou 
cd \HACKATHON_2025\backend
python main.py

Accéder à la documentation interactive :
   - Swagger UI : [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)
   - Redoc : [http://127.0.0.1:8080/redoc](http://127.0.0.1:8080/redoc)

# Démarrer le frontend
cd ../frontend
streamlit run app.py

## Exemples d'utilisation
Requête GET avec un paramètre `query` :
```
GET http://127.0.0.1:8080/query/(la question posé)
```
Réponse JSON :
```json
{
  "response": "Article structuré :\n\nRésumé : L'IA est..."
}
```

## Développement
Si tu modifies le code, assure-toi de redémarrer le serveur avec `uvicorn` pour voir les changements.

## Problèmes connus
- Vérifier que tous les fichiers Python sont bien dans `backend/`
- Si `agents.agent` n'est pas trouvé, assure-toi d'exécuter `uvicorn` depuis `backend/`

## Auteurs
- Dounia MESSAOUI
- Hanane OUMAZIZ
- Syrine ALITI
- Anis GHEBRIOUA
- Anis BOURENNANI
- Hamid ZIDELMAL

## Licence
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

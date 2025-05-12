# flask_devops
module 158 Projet final Devops

### Procédure de changement et builds jenkins

nano app-morattel.py

return "Nouveau test automatique du pipeline Jenkins !"

git add app-morattel.py
git commit -m "Test du pipeline Jenkins"
git push

1. Va sur l’interface Jenkins (http://localhost:8080)
2. Clique sur ton projet ("app-devops").
3. Vérifie que le dernier build est bien lancé et qu’il se termine avec succès (pastille verte).
4. Clique sur le build pour voir les logs ("Console Output") si besoin.

#### Teste l’application Flask
Ouvre un navigateur sur http://localhost:5000 (ou le port configuré dans ton app).
Vérifie que le nouveau message s’affiche.

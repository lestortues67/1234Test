""" 
Date : 23/02/2024 à 17h25 
Auteur : Christian Doriath
Dossier : /Python39/MesDEv/Flask/Flask_codebase2023
Fichier : app.py 
Description : app "codebase" une base de données qui contient TOUTE notre base des connaissances
de code informatique. 
"""
import subprocess

from flask import Flask, request, render_template, session, redirect, url_for, flash, jsonify
from flask_bootstrap import Bootstrap
import locale
locale.setlocale(locale.LC_TIME, "fr_FR")

import gitLibrary

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

bootstrap = Bootstrap(app)


@app.route('/papa', methods=['GET', 'POST'])
def mypapa():
    return render_template('index.html') 


@app.route('/', methods=['GET', 'POST'])
def myindex():
    return render_template('index.html') 

# 05/02/2024
# Sur github on utilise le repo "gittest" : 
# git@github.com:lestortues67/gittest.git
@app.route('/git_update', methods=['POST'])
def my_git_update():
    print("une requete POST arrive ici ...")

    # récupérer les datas POST 
    j = request.get_json()
    print("Les datas POST  : ",j)
    print(" ")
    print(" ")
    print("La branche qui a fait GIT PUSH est : ")
    # refs/heads/master
    print("j['ref'] : ",j['ref'])
    print("j['ref'][11:] : ",j['ref'][11:])

    branchToPull = j['ref'][11:]

    repo = gitLibrary.makeRepo('./')

    print("repo : ",repo)
    print('repo working DIR : ',repo.working_dir)

    brancheExiste = gitLibrary.localBranchIsPresent(repo, branchToPull)
    print("Cette branche existe sur LOCAL ? ")
    print(brancheExiste)
    print(" ")

    if not(brancheExiste):
        # La branche n'existe PAS en LOCAL il faut la créer
        gitLibrary.createBranch(repo, branchToPull)
        print("Création d'une NOUVELLE branche ")

    gitLibrary.pullABranch(repo, branchToPull)
    # re-load the app 

    # Commande Bash à exécuter
    #touch est un mot important pour que cela fonctionne 
    commande = "touch /var/www/gittest_eu_pythonanywhere_com_wsgi.py"

    # Exécution de la commande Bash
    resultat = subprocess.run(commande, shell=True, capture_output=True, text=True)

    # Affichage du résultat
    print("Infos sur re-load :", resultat.stdout)    
    return 'ok', 200

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500       

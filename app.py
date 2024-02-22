"""
Date : 22/02/2024 à 12h06
Auteur : Christian Doriath
Dossier : /Python39/MesDEv/Flask/Flask_codebase2023
Fichier : app.py 
Description : app "codebase" une base de données qui contient TOUTE notre base des connaissances
de code informatique. 
"""
import subprocess
import datetime
import string
from flask import Flask, request, render_template, session, redirect, url_for, flash, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from random import choice 
import locale
locale.setlocale(locale.LC_TIME, "fr_FR")

import time
from logging import FileHandler, WARNING
import uuid

import pytz

import git

import requests


def oldJunk ():
    # http://lestortues67.eu.pythonanywhere.com/
    # http://gittest.eu.pythonanywhere.com/papa2

    #14h57 le 13.02.2024 
    #bravo 
    #test pour PAW à 15h06

    requests.post('http://www.eu.pythonanywhere.com/user/gittest/webapps/gittest.eu.pythonanywhere.com/reload/')

    username = 'gittest'
    token = 'a218716ef32480f67b5081a3a107e64fd2d2121c'

    response = requests.get(
        'https://eu.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
            username=username
        ),
        headers={'Authorization': 'Token {token}'.format(token=token)}
    )

    consolesUsed = requests.get(
        'https://eu.pythonanywhere.com/api/v0/user/{username}/consoles/'.format(
            username=username
        ),
        headers={'Authorization': 'Token {token}'.format(token=token)}
    )

    if consolesUsed.status_code == 200:
        print('Les consoles en cours sont :')
        print(consolesUsed.content)
    else:
        print('Got unexpected status code {}: {!r}'.format(consolesUsed.status_code, consolesUsed.content))

    if response.status_code == 200:
        print('CPU quota info:')
        print(response.content)
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

    # test for git commit C:\Program Files\Git\cmd  

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

bootstrap = Bootstrap(app)


@app.route('/reloader', methods=['GET', 'POST'])
def myreloader():
    # reload the app

    print("Passage dans /reloader RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")

    username = 'gittest'
    token = 'a218716ef32480f67b5081a3a107e64fd2d2121c'

    # response = requests.get(
    #     'https://eu.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
    #     username=username
    #     ),
    #     headers={'Authorization': 'Token {token}'.format(token=token)}
    #     )


    # https://eu.pythonanywhere.com/api/v0/user/gittest/webapps/gittest.eu.pythonanywhere.com/reload/

    #https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
    # r = requests.post('https://httpbin.org/post', data={'key': 'value'})

    rr = requests.post(
        'https://eu.pythonanywhere.com/api/v0/user/{username}/webapps/gittest.eu.pythonanywhere.com/reload/'.format(
        username=username
        ),
        data={'Authorization': 'Token {token}'.format(token=token)}
        )

    print("Voici la réponse à la requete POST : ",rr)
    
    return 'ok'
 


@app.route('/papa3', methods=['GET', 'POST'])
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
    print(j['ref'])

    # repo = git.Repo('./gittest')

    # Existing local git Repo with 'git.Repo(path_to_dir)'
    repo = git.Repo('./')
    print("repo : ",repo)

    print('repo working DIR : ',repo.working_dir)


    origin = repo.remotes.origin # = <git.Remote "origin">
    # >>> type(origin) 
    # >>> <class 'git.remote.Remote'>  

    print("origin : ",origin)
    print("Je suis une nouvelle phrase N°3 à 12h19")
    print("PUSH depuis PC Local à 15h00 **********************************************")
    

    # repo.create_head('main',origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    repo.create_head('master',origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    
    origin.pull()
    print("'origin.pull()' a été fait ...")
    # re-load the app 

    # Commande Bash à exécuter
    #touch est un mot important pour que cela fonctionne 
    commande = "touch /var/www/gittest_eu_pythonanywhere_com_wsgi.py"

    # Exécution de la commande Bash
    resultat = subprocess.run(commande, shell=True, capture_output=True, text=True)

    # Affichage du résultat
    print("Sortie de la commande :", resultat.stdout)

    return 'ok', 200

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500




        

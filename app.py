"""
Date : 07/02/2024 à 16h24
Auteur : Christian Doriath
Dossier : /Python39/MesDEv/Flask/Flask_codebase2023
Fichier : app.py
Description : app "codebase" une base de données qui contient TOUTE notre base des connaissances
de code informatique. 
"""

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


# test for git commit C:\Program Files\Git\cmd  



app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def myindex():
    return render_template('index.html') 

# 05/02/2024
# Sur github on utilise le repo "gittest" : 
# git@github.com:lestortues67/gittest.git
@app.route('/git_update', methods=['POST'])
def my_git_update():
    print("une requete POST arrive ici ...")
    # repo = git.Repo('./gittest')

    # Existing local git Repo with 'git.Repo(path_to_dir)'
    repo = git.Repo('./')
    print("repo : ",repo)

    print('repo working DIR : ',repo.working_dir)


    origin = repo.remotes.origin # = <git.Remote "origin">
    # >>> type(origin)
    # >>> <class 'git.remote.Remote'>

    print("origin : ",origin)
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    print("'origin.pull()' a été fait ...")
    return '', 200

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500




        

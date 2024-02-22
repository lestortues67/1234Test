"""
Date : 22/02/2024 à 9h30
Auteur : Christian Doriath
Dossier : /temp/gittest01
Fichier : test01.py
Description : 
"""
   
import datetime
import string
import pytz
from random import choice
import locale 
locale.setlocale(locale.LC_TIME, "fr_FR")

import time
from logging import FileHandler, WARNING
import os

import requests

from git import Repo


def dateProvider():
    # Fournir immédiatement l'heure et la date de Paris en plusieurs formats : 
    # - en texte long dateLongueTexte. 
    # - un integer pour epoch
    # - un datetime 
    # Utiliser le fuseau horaire local (Paris)
    fuseau_horaire_local = pytz.timezone('Europe/Paris')

    # Obtenir l'heure locale dans le fuseau horaire défini
    heure_locale = datetime.datetime.now(fuseau_horaire_local)

    dateLongueTexte = heure_locale.strftime("%A, %d %B %Y %H:%M:%S")

    epoch = int(heure_locale.timestamp())
    
    return{'date':heure_locale,'texte':dateLongueTexte,'epoch':epoch}

def getActiveBranch(p_repo):
    return p_repo.active_branch.name



def printBranches(p_repo):
    #Afficher le nom des branches 
    lesBranches = p_repo.git.branch()
    # 'lesBranches' est un STRING
    print("Les branches LOCALES sont : ")
    print(lesBranches)
    print("type(lesBranches) : ",type(lesBranches))
    print("")



def printBranches2(p_repo):
    #Afficher le nom des branches
    print("2: Les branches LOCALES sont : ")
    print(p_repo.branches)
    # p_repo.branches <class 'git.util.IterableList'>
    print("type(p_repo.branches) : ",type(p_repo.branches))
    print("dir(p_repo.branches) : ",dir(p_repo.branches))
    print("p_repo.branches.__contains__('papa') : ",p_repo.branches.__contains__('papa'))
    print("p_repo.branches.__contains__('oscar') : ",p_repo.branches.__contains__('oscar'))

    print("")


def printRemoteBranches(p_repo):
    # Execute from the repository root directory
    remote_refs = p_repo.remote().refs
    print("type(p_repo.remote().refs) : ",type(p_repo.remote().refs))
    print("Les branches REMOTE sont : ")
    for refs in remote_refs:
        print(refs.name)
    print("p_repo.remote().refs.__contains__('papa') : ",p_repo.remote().refs.__contains__('papa'))
    print("p_repo.remote().refs.__contains__('oscar') : ",p_repo.remote().refs.__contains__('oscar'))


def remoteBranchIsPresent(p_repo, p_branchName):
    # vérifier si une branche REMOTE existe true/false
    return p_repo.remote().refs.__contains__(p_branchName)
    

def localBranchIsPresent(p_repo, p_branchName):
    # vérifier si une branche existe true/false
    # lesBranches = p_repo.git.branch()
    # return p_branchName in lesBranches
    return p_repo.branches.__contains__(p_branchName)

def createBranch(p_repo, p_branchName):
    # Créer et se déplacer sur la nouvelle branche
    new_branch = p_branchName
    current = p_repo.create_head(new_branch)    
    current.checkout()

def switchToBranch(p_repo, p_branchName):
    # se placer sur une autre branche
    try :
        p_repo.branches[1].checkout()    
        return True
    except Exception as e:
        print("Impossible de changer de branche... "+ str(e))
        print("FIN du message d'erreur... ")
        print(" ")
        return False

def pullABranch(p_repo, p_branchName):
    # git pull sur une branche en particulier
    try :
        repo.git.pull('origin', p_branchName)
        return True
    except Exception as e:
        print("Impossible de faire git pull origin ",p_branchName)
        print("Voici le meessage d'erreur : "+ str(e))
        print("FIN du message d'erreur... ")
        print(" ")
        return False

def makeCommit(p_repo, p_message):
    isDirty = p_repo.is_dirty()
    if isDirty:
        try :
            p_repo.git.commit('-m', p_message, author='christian.doriath@free.fr')
            return True
        except Exception as e:
            print("Impossible de faire ce commit ... ")
            print(str(e))
            print("FIN du message d'erreur... ")
            print(" ")
            return False

    else:
        print("repo is clean (NOT dirty) nothing to commit ! ")
        return False




def getStatus(p_repo):
    s = repo.git.execute("git status")
    # print("repo.git.execute('git status') :",repo.git.execute("git status"))
    return s
    



cwd = os.getcwd()



print("")
print("")
print("SSSSSSSSSSSSSSSSS START SSSSSSSSSSSSSSSSSSSSSSSSSS")
print("")
print("")  

print("L'heure : ",dateProvider()['texte'])

print("Le dir courant est : ",cwd)

# Chemin vers le répertoire Git
# repo_path = '/chemin/vers/votre/repo'
repo_path = './'

# Initialiser l'objet Repo
repo = Repo(repo_path)


print("Git status : ",getStatus(repo))
print("FIN ------------------ Git status ")



# créer une branche 
# createBranch(repo, 'banana') # ok le 20/02/2024 à 13h08


printRemoteBranches(repo)


# Exécuter une commande Git arbitraire
# result = repo.git.execute('votre_commande_git')

printBranches(repo)
printBranches2(repo)

print(" ")
print("Les branches LOCALES contiennent 'claire' : ", localBranchIsPresent(repo, 'claire'))
print("Les branches LOCALES contiennent 'popeye' : ", localBranchIsPresent(repo, 'popeye'))
print("Les branches LOCALES contiennent 'my_branch' : ", localBranchIsPresent(repo, 'my_branch'))




print(" ")
print("Active branch is :  ",getActiveBranch(repo))

print(" ")
isDirty = repo.is_dirty()
print("Is repo dirty ? ", isDirty)
print(" ")

if (makeCommit(repo, "un commit avec gitPython")):
    print("Le commit a été fait, youpi !!")
else:
    print("Le commit n'a PAS été fait...")



print(" ")
print("Index (the STAGE) is :  ",repo.index)
print("The methods of Index (the STAGE) are :  ",dir(repo.index))

print(" ")
print("Head (branch) is :  ",repo.head)
print("Reference branch (with head) is :  ",repo.head.reference)



print(" ")
print("Changer de branche ")
switchToBranch(repo, "p_branchName")








#repo = git.Repo('./')

print('Voici repo : ',repo)
print("")
print('====================================== ')
print("repo.git.execute('git status') :",repo.git.execute("git status"))
print('====================================== ')

r = 'papa'

c = 'git pull origin '

rc = c+r



print("repo.git.execute('git status') :",repo.git.execute("git status"))
print('====================================== ')



remote = repo.remote()
remote_name = remote.name
branch_name = repo.active_branch.name


# http://lestortues67.eu.pythonanywhere.com/
# http://gittest.eu.pythonanywhere.com/papa2

#14h57 le 13.02.2024 
#bravo 
#test pour PAW à 15h06

# requests.post('http://www.eu.pythonanywhere.com/user/gittest/webapps/gittest.eu.pythonanywhere.com/reload/')

# username = 'gittest'
# token = 'a218716ef32480f67b5081a3a107e64fd2d2121c'

# response = requests.get(
#     'https://eu.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
#         username=username
#     ),
#     headers={'Authorization': 'Token {token}'.format(token=token)}
# )

# consolesUsed = requests.get(
#     'https://eu.pythonanywhere.com/api/v0/user/{username}/consoles/'.format(
#         username=username
#     ),
#     headers={'Authorization': 'Token {token}'.format(token=token)}
# )

# if consolesUsed.status_code == 200:
#     print('Les consoles en cours sont :')
#     print(consolesUsed.content)
# else:
#     print('Got unexpected status code {}: {!r}'.format(consolesUsed.status_code, consolesUsed.content))






# if response.status_code == 200:
#     print('CPU quota info:')
#     print(response.content)
# else:
#     print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))






# test for git commit C:\Program Files\Git\cmd  


    # print("une requete POST arrive ici ...")
    # # repo = git.Repo('./gittest')

    # j = request.get_json()
    # print("Les datas RX au format JSON : ",j)

    # try:
    #     print("j['ref'] : ",j['ref'])
    #     print("Vers quelle branche a-t-on 'push' ?' ",j['ref'][11:])
        
    # except:
    #     print("Exception pour print(j['ref'])") 

    # print("************************************************") 

    # print("dir(j) : ",dir(j)) 
    # print("************************************************") 
    # print("type(j) : ",type(j)) 



    # Existing local git Repo with 'git.Repo(path_to_dir)'
    # repo = git.Repo('./') 
    # print("repo : ",repo)

    # print('repo working DIR : ',repo.working_dir)

    # origin = repo.remotes.origin # = <git.Remote "origin">
    # >>> type(origin) 
    # >>> <class 'git.remote.Remote'>  

    # papa = repo.remotes.papa 

    # print("papa : ",papa)
    # print("Je suis une nouvelle phrase N°3 à 12h19")
    # print("PUSH depuis PC Local à 15h00 **********************************************")
    

    # repo.create_head('main',origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    # repo.create_head('master',origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    # repo.create_head('papa',origin.refs.papa).set_tracking_branch(origin.refs.papa).checkout()
    
    #origin.pull()
    # papa.pull()

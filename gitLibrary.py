"""
Date : 22/02/2024 à 16h35
Auteur : Christian Doriath
Dossier : /temp/gittest01
Fichier : test01.py
Description : 
"""
   
import datetime
import pytz
import locale 
locale.setlocale(locale.LC_TIME, "fr_FR")

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
        p_repo.git.pull('origin', p_branchName)
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
    # Pour afficher correctement la valeur retournée utiliser en python 'print'
    return p_repo.git.execute("git status")
    

def makeRepo(p_dir):
    return Repo(p_dir)    

def cmd_git_merge(p_repo, p_branchNameSource, p_branchNameDestination):
    # Merger les branches p_branchNameSource vers p_branchNameDestination

    # Au préalable s'assurer que les noms des branches existent 
    if (localBranchIsPresent(p_repo, p_branchNameSource) and localBranchIsPresent(p_repo, p_branchNameDestination)):
        # Nom des branches à merger
        branche_source = 'nom_de_la_branche_source'
        branche_destination = 'nom_de_la_branche_destination'

        # Accès aux branches
        branche_source = p_repo.branches[p_branchNameSource]
        branche_destination = p_repo.branches[p_branchNameDestination]

        # Effectuer le merge
        p_repo.git.merge(branche_source, branche_destination)
        return True
    else:
        return False

def cmd_git_config(p_repo, p_userName, p_userEmail):
    # Accès à la configuration du dépôt
    config = p_repo.config_writer()

    # Configuration d'une option Git spécifique
    config.set_value('user', 'name', p_userName)
    config.set_value('user', 'email', p_userEmail)

    # Enregistrer les modifications de configuration
    config.release()



    


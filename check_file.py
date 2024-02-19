import os
import pandas as pd
from box_select_file import select_file

def choose_chgt_file() :
    file = select_file("correspondant aux CHARGEMENTS")
    return file

def check_file(dossier):
    # Chemin du dossier contenant le fichier Excel

    # Liste de fichiers dans le dossier
    fichiers_dans_dossier = os.listdir(dossier)

    # Filtrer les fichiers avec le nom commençant par "EXP" et l'extension .xlsx
    fichiers_exp_xlsx = [fichier for fichier in fichiers_dans_dossier if fichier.startswith('EXP') and fichier.endswith('.xlsx')]

    # Importer le premier fichier EXP.xlsx trouvé
    if fichiers_exp_xlsx:
        premier_fichier_exp_xlsx = fichiers_exp_xlsx[0]  # Le premier fichier dans la liste
        chemin_fichier_exp_xlsx = os.path.join(dossier, premier_fichier_exp_xlsx)
        
        # Renvoyer le nom et le chemin du fichier
        print(f"le fichier est : {chemin_fichier_exp_xlsx}")
    else:
        print("Aucun fichier EXP*.xlsx trouvé dans le dossier.")
        chemin_fichier_exp_xlsx = choose_chgt_file()
        
    # Import du fichier Excel
    df = pd.read_excel(chemin_fichier_exp_xlsx, header=None, nrows=4)

    # Vérifier si le mot "chargements" est présent dans les 4 premières lignes
    mot_a_rechercher = 'chargements'
    contient_mot = df.map(lambda cellule: mot_a_rechercher.lower() in str(cellule).lower()).any().any()

    # if contient_mot:
    #     print(f"OK, le fichier correspond aux {mot_a_rechercher}.")
    # else:
    #     print(f"Le fichier ne correspond pas aux {mot_a_rechercher}.")
        
    return pd.read_excel(chemin_fichier_exp_xlsx)



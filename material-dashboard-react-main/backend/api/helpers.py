import os
from .models import SubDivision, Street, Neigbor, SubdividionUsers, AdminUsers, SubdivisionNumberDB
from pathlib import Path
from dynamic_db_router import in_database

"""
This function will search inside subdivision_db directory the database number and will return True if client number is found. 
The value db_number will be stored in a session variable ( db_number ) 
"""
def find_db_in_path_subdivision(request, db_number):
    BASE_DIR = Path(__file__).resolve().parent.parent
    dirt = BASE_DIR / 'subdivions_db'
    dir_list = os.listdir(dirt)
    sep = "."
    found = False
    results = ""
    data_base_list = []
    yourdata=""        
    for l in dir_list:
        strip_db_number = l.split(sep, 1)[0]
        data_base_list.append(strip_db_number)
    if data_base_list:
        if db_number in data_base_list:
            request.session["db_number"] = db_number
            with in_database(request.session["db_number"]):
                quer=AdminUsers.objects.all()
            return True
        else:
            return False
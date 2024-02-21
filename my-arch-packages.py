#!/usr/bin/env python3
#............................
#

import sqlite3
import os
import sys
import argparse
import requests
#----------------

#----------------------------------------\\
# CHANGE TO FIT YOUR SETTINGS
# - - - - - - - - - - - - - - - - - - - - -\\
#
# where should the sqlite3 database be stored?
db_file     = '/home/produnis/archpakete.db'
#----------------------------------------\\

#######################################################################
# DO NOT CHANGE AFTER HERE....
# # # # # # # # # # # # # # # #
#
#-------------------------------------------------------//



# argparse
#---------
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", help="add package to install-list")  							# get argument with "args.add"
parser.add_argument("-d", "--delete", help="delete package from install-list")  					# get argument with "args.delete"
parser.add_argument("-m", "--move", help="move package from/to AUR")  								# get argument with "args.move"
parser.add_argument("-aur", "--AUR", action="store_true", help="set if this package is from AUR")	# get argument with "args.AUR"
parser.add_argument("-p", "--print", action="store_true", help="print intsall command")				# get argument with "args.print"
args = parser.parse_args()
#-------------------------------------------------------//


# colors
#-------
CEND  = '\33[0m'
CPAC  = '\33[36m'
CAUR  = '\33[35m'
CYAY  = '\33[92m'

#----------------------------------------------------------------------------||
# sqlite db
#--------
if not os.path.isfile(db_file):
    conn = sqlite3.connect(db_file)
    conn.close()

# connect to SQLite database
conn = sqlite3.connect(db_file)

# create tabel, if it does not exist
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS archpakete
               (paket TEXT PRIMARY KEY NOT NULL,
                aur TEXT NOT NULL);''')
conn.commit()



#----------------------------------------------------------------------------{}
# functions
#----------
def check_package(package_name):
    # check if packages is from arch repository
    repo_url = f"https://www.archlinux.org/packages/?q={package_name}"
    repo_response = requests.get(repo_url)
    if "0 matching packages found." not in repo_response.text:
        return "Repo"
    # check if package is from AUR
    testpackage = "https://aur.archlinux.org/packages/%s" % ( package_name)
    response = requests.get(testpackage)
    try:
        response.raise_for_status()
        return "Aur"   
    except:
        pass
    # package not found
    return "STOP"
#----------------------------------------------------------------------------{}	




##### MAIN SCRIPT ###########



#----------------------------------------------------------------------------------------\\
# Print list
#-----------
if args.print == True:
	paketliste = "pacman -S "
	aurliste = "yay -S "
	# get all database entries and sort them by categories
	cur = conn.cursor()
	cur.execute("SELECT * FROM archpakete ORDER BY paket ASC")
	results = cur.fetchall()
	for result in results:
		if result[1] == "FALSE":
			paketliste += result[0]
			paketliste += " "
		else:
			aurliste += result[0]
			aurliste += " "	
	print("#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+- ")
	print("# So, you want to install all your pacakges to a fresh Arch, hm?")
	print("# Let's start with non-AUR packages:")
	print("# ----------------------------------")
	print(CPAC + paketliste + CEND)
	print(" ")
	print(" ")
	print("# Time to install 'yay' for easy AUR-installations: ")
	print("# -------------------------------------------------")
	print(CYAY + "git clone https://aur.archlinux.org/yay.git")
	print("cd yay")
	print("makepkg -si" + CEND)
	print(" ")
	print(" ")
	print("# Now you can simply install all these AUR-packages: ")
	print("# --------------------------------------------------")
	print(CAUR + aurliste + CEND)
	print(" ")
	print("# Enjoy, bye ! ")
	print("#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ ")

	sys.exit() # bye bye
#----------------------------------------------------------------------------------------\\





#----------------------------------------------------------------------------------------++
# Add package
#--------------
if args.add:
	paketname = args.add
	# search for words
	cur = conn.cursor()
	cur.execute("SELECT * FROM archpakete WHERE paket=?", (paketname,))
	result = cur.fetchone()

	# check if word was found
	if result is not None:
		print(f"{paketname} is in database and belongs to category FROM AUR = {result[1]}.")
		print("Package is already in the database. Doing nothing...")
	else:
		print(f"{paketname} is not in database.")
		# check if package is from AUR
		fromaur = check_package(paketname)
		if fromaur == "Repo":
			print(f"{paketname} is from the arch repo. Saving package into database.")
			cur.execute("INSERT INTO archpakete (paket, aur) VALUES (?, ?)", (paketname, "FALSE"))
		elif fromaur == "Aur":
			print(f"{paketname} is from AUR. Saving package to db.")
			cur.execute("INSERT INTO archpakete (paket, aur) VALUES (?, ?)", (paketname, "TRUE"))
		else:
			print(f"{paketname} cannot be found. Doing nothing.")
		conn.commit()


		#----------------------------------------	
#------------------------------------------------------------------------------- --------++





#----------------------------------------------------------------------------------------  - -
# delete package
#--------------
if args.delete:
	paketname = args.delete
	cur.execute("DELETE FROM archpakete WHERE paket=?", (paketname,))
	conn.commit()
	if cur.rowcount > 0:
		print(f"{paketname} was deleted from database.")
	else:
		print(f"{paketname} was NOT found in database and thus was NOT deleted.")

#----------------------------------------------------------------------------------------  - -



#----------------------------------------------------------------------------------------  - -
# move package
#--------------
if args.move:
	paketname = args.move


#----------------------------------------------------------------------------------------  - -

cur.close()
conn.close()
#############
# End of File 

import random

#LES VARIABLES

name1 = 'name1'
name2 = 'name2'
name3 = 'name3'
name4 = 'name4'
name5 = 'name5'
name6 = 'name6'


#Tableau avec les variables dedans
names = [name1, name2, name3, name4, name5, name6]

#Variables nombre de groupe
nb_groups = 3

#Variable nombre max de groupe 
max_nb_groups = len(names) // nb_groups

print(names)

#Boucle for each
for i in range(nb_groups):
    
    #Variable selected qui fait une génération aleatoire de groupes avec les elements du tableau names
    #avec en paramètres un nombres maximal de groupe définit dans max_nb_groups
    selected = random.sample(names, k=max_nb_groups)
    
    #print du resulats des groupes aléatoires 
    print("GROUP #%s : %s \n" % (i+1, selected))
    
    for sel in selected:
        names.remove(sel)
        print(sel)

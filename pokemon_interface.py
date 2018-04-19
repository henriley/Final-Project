import requests
import json
import secrets
import sys
import sqlite3
import plotly.plotly as py
import plotly.graph_objs as go
import webbrowser

DBNAME='Pokemon.db'

commands='''
stats <pokemona name>
    This gets all the stats of the entered Pokemon

graph <pokemon name 1> <pokemon name 2> <stat>
    This creates a bar graph of the two different Pokemons' stats. You can compare all six stats
    between two Pokemon.
    ex. graph staraptor snorlax speed will compare the two speeds of Staraptor and Snorlax
    The calls are:
    <pokemon name 1> <pokemon name 2> hp
    <pokemon name 1> <pokemon name 2> attack
    <pokemon name 1> <pokemon name 2> defense
    <pokemon name 1> <pokemon name 2> specialattack
    <pokemon name 1> <pokemon name 2> specialdefense
    <pokemon name 1> <pokemon name 2> speed

type <pokemon name>
    This gets the type(s) of the entered Pokemon

pokedex <pokemon name>
    This gets the National PokeDex number of the entered Pokemon

height weight <pokemon name>
    This gets the height and weight of the Pokemon

all stats <pokemon name>
    This returns PokeDex number, type(s), abilities, height and weight, and all stats of the entered Pokemon

evolutions <pokemon name>
    This gets the evolutionary line of the selected Pokemon

abilities <pokemon name>
    This gets the abilities of the Pokemon

ability info <ability name>
    This gets information about what the ability does in battle

picture <pokemon name>
    This gets some artwork of the entered Pokemon

don't work
    This shows which Pokemon won't work when entered

variations
    This shows the difference for Mega evolutions and Alolan forms

exit
    This exits the program
    '''

initial='''
Please enter all words as lowercase

When entering a pokemon name that has a space in it, please use dashes
    ex. Stats for Mega Metagross would be stats metagross-mega
'''

variations='''abomasnow-mega, absol-mega, aegislash-blade, aegislash-shield, aerodactyl-mega, aggron-mega, alakazam-mega, altaria-mega, ampharos-mega,
audino-mega, banette-mega, basculin-blue-striped,  basculin-red-striped, beedrill-mega, blastoise-mega, blaziken-mega, camerupt-mega,
castform-rainy, castform-snowy, castform-sunny, charizard-mega-x, charizard-mega-y, darmanitan-standard, darmanitan-zen, deoxys-attack,
deoxys-defense, deoxys-normal, deoxys-speed, diancie-mega, diglett-alola, dugtrio-alola,  exeggutor-alola, farfetchd, gallade-mega,
garchomp-mega, gardevoir-mega, gengar-mega, geodude-alola, giratina-altered, giratina-origin, glalie-mega, golem-alola, gourgeist-average,
gourgeist-large, gourgeist-small, gourgeist-super, graveler-alola, grimer-alolamuk-alola, groudon-primal, gyarados-mega, heracross-mega,
houndoom-mega, kangaskhan-mega, keldeo-ordinary, keldeo-resolute, kyogre-primal, kyurem-black, kyurem-white, landorus-incarnate, landorus-therian,
latias-mega, latios-mega, lopunny-mega, lucario-mega, lycanroc-midday, lycanroc-midnight, magearna-original, manectric-mega, marowak-alola,
mawile-mega, medicham-mega, meloetta-aria, meloetta-pirouette, meowstic-female, meowstic-male, meowth-alola, metagross-mega, mewtwo-mega-x,
mewtwo-mega-y, mime-jr, mimikyu-busted, mimikyu-disguised, minior-blue, minior-blue-meteor, minior-green, minior-green-meteor, minior-indigo,
minior-indigo-meteor, minior-orange-meteor, minior-red, minior-orange, minior-red-meteor, minior-violet, minior-violet-meteor, minior-yellow,
minior-yellow-meteor, mr-mime, nidoran-f, nidoran-m, ninetales-alola, oricorio-baile, oricorio-pau, oricorio-pom-pom , oricorio-sensu, persian-alola,
pidgeot-mega, pinsir-mega, pumpkaboo-average, pumpkaboo-large, pumpkaboo-small, pumpkaboo-super, raichu-alola, raticate-alola, rattata-alola, rayquaza-mega,
rotom-fan, rotom-frost, rotom-heat, rotom-mow, rotom-wash, sableye-mega, salamence-mega, sandshrew-alola, sandslash-alola, sceptile-mega, scizor-mega,
sharpedo-mega, shaymin-land, shaymin-sky, slowbro-mega, steelix-mega, swampert-mega, tapu-bulu, tapu-fini, tapu-koko, tapu-lele, thundurus-incarnate,
tornadus-incarnate, tornadus-therian, tornadus-therian, type-null, tyranitar-mega, venusaur-mega, vulpix-alola, wishiwashi-school, wishiwashi-solo,
wormadam-plant, wormadam-sandy, wormadam-trash, zygarde-10, zygarde-50, zygarde-complete
'''

no_work='''
These Pokemon don't work:
poipole
zeraora
naganadel
stakataka
blacephalon
greninja-battle-bond
'''

user_input=''
while user_input!='exit':
    if user_input=='':
        print('--'*40)
        print(commands)
        print('--'*40)
        print(initial)
        print('--'*40)
        print(no_work)
        print('--'*40)
    user_input=input("Input a command. Enter 'help' to see a list of commands: ")
    if user_input=='help':
        print(commands)

    elif 'stats' in user_input and 'all' not in user_input:
        if len(user_input.split())==1:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")
            continue
        try:
            boi=user_input.split()
            conn=sqlite3.connect(DBNAME)
            cur=conn.cursor()
            query='''
                SELECT HP, Attack, Defense, SpecialAttack, SpecialDefense, Speed
                FROM PokemonStats
                WHERE Name = (?)
            '''
            params=(boi[-1],)
            cur.execute(query, params)

            for row in cur:
                stats='HP: '+str(row[0])+'\n'+'Attack: '+str(row[1])+'\n'+'Defense: '+str(row[2])+'\n'+'Special Attack: ' \
                +str(row[3])+'\n'+'Special Defense: '+str(row[4])+'\n'+'Speed: '+str(row[5])

            conn.commit()
            conn.close()

            print(stats)
        except:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")

    elif 'evolutions' in user_input:
        if len(user_input.split())==1:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")
            continue
        try:
            boi=user_input.split()
            conn=sqlite3.connect(DBNAME)
            cur=conn.cursor()
            try:
                query='''
                    SELECT Stage1, Stage2, Stage3, Stage4, Stage5, Stage6, Stage7, Stage8, Stage9
                    FROM Evolutions
                    WHERE Stage1 = (?)
                '''
                params=(boi[-1],)
                cur.execute(query, params)

                evolutions=[]
                for row in cur:
                    if row[0]!=None:
                        evolutions+=[row[0]]
                    if row[1]!=None:
                        evolutions+=[row[1]]
                    if row[2]!=None:
                        evolutions+=[row[2]]
                    if row[3]!=None:
                        evolutions+=[row[3]]
                    if row[4]!=None:
                        evolutions+=[row[4]]
                    if row[5]!=None:
                        evolutions+=[row[5]]
                    if row[6]!=None:
                        evolutions+=[row[6]]
                    if row[7]!=None:
                        evolutions+=[row[7]]
                    if row[8]!=None:
                        evolutions+=[row[8]]

                    evolutions_=''
                    num=1
                    for x in evolutions:
                        evolutions_+=str(num)+'. '+x+'\n'
                        num+=1

                    print(evolutions_)
            except:
                pass
            try:
                query='''
                    SELECT Stage1, Stage2, Stage3, Stage4, Stage5, Stage6, Stage7, Stage8, Stage9
                    FROM Evolutions
                    WHERE Stage2 = (?)
                '''
                params=(boi[-1],)
                cur.execute(query, params)

                evolutions=[]
                for row in cur:
                    if row[0]!=None:
                        evolutions+=[row[0]]
                    if row[1]!=None:
                        evolutions+=[row[1]]
                    if row[2]!=None:
                        evolutions+=[row[2]]
                    if row[3]!=None:
                        evolutions+=[row[3]]
                    if row[4]!=None:
                        evolutions+=[row[4]]
                    if row[5]!=None:
                        evolutions+=[row[5]]
                    if row[6]!=None:
                        evolutions+=[row[6]]
                    if row[7]!=None:
                        evolutions+=[row[7]]
                    if row[8]!=None:
                        evolutions+=[row[8]]

                    evolutions_=''
                    num=1
                    for x in evolutions:
                        evolutions_+=str(num)+'. '+x+'\n'
                        num+=1

                    print(evolutions_)
            except:
                pass
            try:
                query='''
                    SELECT Stage1, Stage2, Stage3, Stage4, Stage5, Stage6, Stage7, Stage8, Stage9
                    FROM Evolutions
                    WHERE Stage3 = (?)
                '''
                params=(boi[-1],)
                cur.execute(query, params)

                evolutions=[]
                for row in cur:
                    if row[0]!=None:
                        evolutions+=[row[0]]
                    if row[1]!=None:
                        evolutions+=[row[1]]
                    if row[2]!=None:
                        evolutions+=[row[2]]
                    if row[3]!=None:
                        evolutions+=[row[3]]
                    if row[4]!=None:
                        evolutions+=[row[4]]
                    if row[5]!=None:
                        evolutions+=[row[5]]
                    if row[6]!=None:
                        evolutions+=[row[6]]
                    if row[7]!=None:
                        evolutions+=[row[7]]
                    if row[8]!=None:
                        evolutions+=[row[8]]

                    evolutions_=''
                    num=1
                    for x in evolutions:
                        evolutions_+=str(num)+'. '+x+'\n'
                        num+=1
                    print(evolutions_)
            except:
                pass
            try:
                query='''
                    SELECT Stage1, Stage2, Stage3, Stage4, Stage5, Stage6, Stage7, Stage8, Stage9
                    FROM Evolutions
                    WHERE Stage4 = (?)
                '''
                params=(boi[-1],)
                cur.execute(query, params)

                evolutions=[]
                for row in cur:
                    if row[0]!=None:
                        evolutions+=[row[0]]
                    if row[1]!=None:
                        evolutions+=[row[1]]
                    if row[2]!=None:
                        evolutions+=[row[2]]
                    if row[3]!=None:
                        evolutions+=[row[3]]
                    if row[4]!=None:
                        evolutions+=[row[4]]
                    if row[5]!=None:
                        evolutions+=[row[5]]
                    if row[6]!=None:
                        evolutions+=[row[6]]
                    if row[7]!=None:
                        evolutions+=[row[7]]
                    if row[8]!=None:
                        evolutions+=[row[8]]

                    evolutions_=''
                    num=1
                    for x in evolutions:
                        evolutions_+=str(num)+'. '+x+'\n'
                        num+=1
                    print(evolutions_)
            except:
                pass
            try:
                query='''
                    SELECT Stage1, Stage2, Stage3, Stage4, Stage5, Stage6, Stage7, Stage8, Stage9
                    FROM Evolutions
                    WHERE Stage5 = (?)
                '''
                params=(boi[-1],)
                cur.execute(query, params)

                evolutions=[]
                for row in cur:
                    if row[0]!=None:
                        evolutions+=[row[0]]
                    if row[1]!=None:
                        evolutions+=[row[1]]
                    if row[2]!=None:
                        evolutions+=[row[2]]
                    if row[3]!=None:
                        evolutions+=[row[3]]
                    if row[4]!=None:
                        evolutions+=[row[4]]
                    if row[5]!=None:
                        evolutions+=[row[5]]
                    if row[6]!=None:
                        evolutions+=[row[6]]
                    if row[7]!=None:
                        evolutions+=[row[7]]
                    if row[8]!=None:
                        evolutions+=[row[8]]

                    evolutions_=''
                    num=1
                    for x in evolutions:
                        evolutions_+=str(num)+'. '+x+'\n'
                        num+=1
                    print(evolutions_)
            except:
                pass
            try:
                query='''
                    SELECT Stage1, Stage2, Stage3, Stage4, Stage5, Stage6, Stage7, Stage8, Stage9
                    FROM Evolutions
                    WHERE Stage6 = (?)
                '''
                params=(boi[-1],)
                cur.execute(query, params)

                evolutions=[]
                for row in cur:
                    if row[0]!=None:
                        evolutions+=[row[0]]
                    if row[1]!=None:
                        evolutions+=[row[1]]
                    if row[2]!=None:
                        evolutions+=[row[2]]
                    if row[3]!=None:
                        evolutions+=[row[3]]
                    if row[4]!=None:
                        evolutions+=[row[4]]
                    if row[5]!=None:
                        evolutions+=[row[5]]
                    if row[6]!=None:
                        evolutions+=[row[6]]
                    if row[7]!=None:
                        evolutions+=[row[7]]
                    if row[8]!=None:
                        evolutions+=[row[8]]

                    evolutions_=''
                    num=1
                    for x in evolutions:
                        evolutions_+=str(num)+'. '+x+'\n'
                        num+=1
                    print(evolutions_)
            except:
                pass
            try:
                query='''
                    SELECT Stage1, Stage2, Stage3, Stage4, Stage5, Stage6, Stage7, Stage8, Stage9
                    FROM Evolutions
                    WHERE Stage7 = (?)
                '''
                params=(boi[-1],)
                cur.execute(query, params)

                evolutions=[]
                for row in cur:
                    if row[0]!=None:
                        evolutions+=[row[0]]
                    if row[1]!=None:
                        evolutions+=[row[1]]
                    if row[2]!=None:
                        evolutions+=[row[2]]
                    if row[3]!=None:
                        evolutions+=[row[3]]
                    if row[4]!=None:
                        evolutions+=[row[4]]
                    if row[5]!=None:
                        evolutions+=[row[5]]
                    if row[6]!=None:
                        evolutions+=[row[6]]
                    if row[7]!=None:
                        evolutions+=[row[7]]
                    if row[8]!=None:
                        evolutions+=[row[8]]

                    evolutions_=''
                    num=1
                    for x in evolutions:
                        evolutions_+=str(num)+'. '+x+'\n'
                        num+=1
                    print(evolutions_)
            except:
                pass
            try:
                query='''
                    SELECT Stage1, Stage2, Stage3, Stage4, Stage5, Stage6, Stage7, Stage8, Stage9
                    FROM Evolutions
                    WHERE Stage8 = (?)
                '''
                params=(boi[-1],)
                cur.execute(query, params)

                evolutions=[]
                for row in cur:
                    if row[0]!=None:
                        evolutions+=[row[0]]
                    if row[1]!=None:
                        evolutions+=[row[1]]
                    if row[2]!=None:
                        evolutions+=[row[2]]
                    if row[3]!=None:
                        evolutions+=[row[3]]
                    if row[4]!=None:
                        evolutions+=[row[4]]
                    if row[5]!=None:
                        evolutions+=[row[5]]
                    if row[6]!=None:
                        evolutions+=[row[6]]
                    if row[7]!=None:
                        evolutions+=[row[7]]
                    if row[8]!=None:
                        evolutions+=[row[8]]

                    evolutions_=''
                    num=1
                    for x in evolutions:
                        evolutions_+=str(num)+'. '+x+'\n'
                        num+=1
                    print(evolutions_)
            except:
                pass
            try:
                query='''
                    SELECT Stage1, Stage2, Stage3, Stage4, Stage5, Stage6, Stage7, Stage8, Stage9
                    FROM Evolutions
                    WHERE Stage9 = (?)
                '''
                params=(boi[-1],)
                cur.execute(query, params)

                evolutions=[]
                for row in cur:
                    if row[0]!=None:
                        evolutions+=[row[0]]
                    if row[1]!=None:
                        evolutions+=[row[1]]
                    if row[2]!=None:
                        evolutions+=[row[2]]
                    if row[3]!=None:
                        evolutions+=[row[3]]
                    if row[4]!=None:
                        evolutions+=[row[4]]
                    if row[5]!=None:
                        evolutions+=[row[5]]
                    if row[6]!=None:
                        evolutions+=[row[6]]
                    if row[7]!=None:
                        evolutions+=[row[7]]
                    if row[8]!=None:
                        evolutions+=[row[8]]

                    evolutions_=''
                    num=1
                    for x in evolutions:
                        evolutions_+=str(num)+'. '+x+'\n'
                        num+=1
                    print(evolutions_)
            except:
                pass
        except:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")

        conn.commit()
        conn.close()

    elif 'height weight' in user_input:
        if len(user_input.split())==2:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")
            continue
        try:
            boi=user_input.split()
            conn=sqlite3.connect(DBNAME)
            cur=conn.cursor()
            query='''
                SELECT Height, Weight
                FROM PokemonStats
                WHERE Name = (?)
            '''
            params=(boi[-1],)
            cur.execute(query, params)

            for row in cur:
                specs='Height: '+row[0]+'\n'+'Weight: '+row[1]

            conn.commit()
            conn.close()

            print(specs)
        except:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")

    elif 'abilities' in user_input:
        if len(user_input.split())==1:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")
            continue
        try:
            boi=user_input.split()
            conn=sqlite3.connect(DBNAME)
            cur=conn.cursor()
            query='''
                SELECT Ability1, Ability2, HiddenAbility
                FROM PokemonStats
                WHERE Name = (?)
            '''
            params=(boi[-1],)
            cur.execute(query, params)

            specs=''
            for row in cur:
                specs+='Ability 1: '+row[0]
                if row[1]!=None:
                    specs+='\n'+'Ability 2: '+row[1]
                if row[2]!=None:
                    specs+='\n'+'Hidden Ability: '+row[2]

            conn.commit()
            conn.close()

            print(specs)
        except:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")

    elif 'ability info' in user_input:
        if len(user_input.split())==2:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")
            continue
        try:
            boi=user_input.split()
            conn=sqlite3.connect(DBNAME)
            cur=conn.cursor()
            query='''
                SELECT AbilityInfo
                FROM Abilities
                WHERE AbilityName = (?)
            '''
            params=(boi[-1],)
            cur.execute(query, params)

            specs=''
            for row in cur:
                print(row[0])

            conn.commit()
            conn.close()
        except:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")

    elif 'type' in user_input:
        if len(user_input.split())==1:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")
            continue
        try:
            boi=user_input.split()
            conn=sqlite3.connect(DBNAME)
            cur=conn.cursor()
            query='''
                SELECT Type1, Type2
                FROM PokemonStats
                WHERE Name = (?)
            '''
            params=(boi[-1],)
            cur.execute(query, params)

            stats=''
            for row in cur:
                stats+='Type 1: '+str(row[0])
                if row[1]!=None:
                    stats+='\n'+'Type 2: '+str(row[1])

            conn.commit()
            conn.close()

            print(stats)
        except:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")

    elif 'pokedex' in user_input:
        if len(user_input.split())==1:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")
            continue
        try:
            boi=user_input.split()
            conn=sqlite3.connect(DBNAME)
            cur=conn.cursor()
            query='''
                SELECT PokeDexNumber
                FROM PokemonStats
                WHERE Name = (?)
            '''
            params=(boi[-1],)
            cur.execute(query, params)

            stats=''
            for row in cur:
                print('Number: '+str(row[0]))

            conn.commit()
            conn.close()

            print(stats)
        except:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")

    elif 'all stats' in user_input:
        if len(user_input.split())==2:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")
            continue
        try:
            boi=user_input.split()
            conn=sqlite3.connect(DBNAME)
            cur=conn.cursor()
            query='''
                SELECT PokeDexNumber, Type1, Type2, Ability1, Ability2, HiddenAbility, HP, Attack, Defense, SpecialAttack, SpecialDefense, Speed
                FROM PokemonStats
                WHERE Name = (?)
            '''
            params=(boi[-1],)
            cur.execute(query, params)

            stats=''
            for row in cur:
                print(boi[-1])
                print('--'*10)
                print('Number: '+str(row[0]))
                print('Type 1: '+str(row[1]))
                print('Type 2: '+str(row[2]))
                print('Ability 1: '+str(row[3]))
                print('Ability 2: '+str(row[4]))
                print('Hidden Ability: '+str(row[5]))
                print('HP: '+str(row[6]))
                print('Attack: '+str(row[7]))
                print('Defense: '+str(row[8]))
                print('Special Attack: '+str(row[9]))
                print('Special Defense: '+str(row[10]))
                print('Speed: '+str(row[11]))

            conn.commit()
            conn.close()

            print(stats)
        except:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")

    elif 'variations' in user_input:
        print(variations)

    elif 'picture' in user_input:
        if len(user_input.split())==1:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")
            continue
        try:
            boi=user_input.split()
            conn=sqlite3.connect(DBNAME)
            cur=conn.cursor()
            query='''
                SELECT DeviantURL
                FROM DeviantArt
                WHERE Name = (?)
            '''
            params=(boi[-1],)
            cur.execute(query, params)

            for row in cur:
                if row[0]==None:
                    print("Sorry, there isn't a picture for this Pokemon.")
                else:
                    webbrowser.open_new(row[0])

            conn.commit()
            conn.close()

        except:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")

    elif "don't work" in user_input:
        print(no_work)

    elif 'graph' in user_input:
        if len(user_input.split())<4:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")
            continue
        try:
            boi=user_input.split()
            conn=sqlite3.connect(DBNAME)
            cur=conn.cursor()
            if boi[-1]=='speed':
                query='''
                    SELECT Speed
                    FROM PokemonStats
                    WHERE Name = (?)
                '''
                params=(boi[1],)
                cur.execute(query, params)

                title='Pokemon '+boi[-1].capitalize()
                stat=[]
                for row in cur:
                    stat+=[row[0]]

                query='''
                    SELECT Speed
                    FROM PokemonStats
                    WHERE Name = (?)
                '''
                params=(boi[2],)
                cur.execute(query, params)

                stats=[]
                for row in cur:
                    stats+=[row[0]]

                conn.commit()
                conn.close()

                trace1 = go.Bar(
                    x=[boi[1]],
                    y=stat,
                    name='Pokemon 1'
                )
                trace2 = go.Bar(
                    x=[boi[2]],
                    y=stats,
                    name='Pokemon 2'
                )
                data = [trace1, trace2]
                layout = go.Layout(
                    barmode='group',
                    title=title,
                    xaxis=dict(
                title='Pokemon Name',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )), yaxis=dict(
                title=boi[-1].capitalize(),
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f')))
                fig = go.Figure(data=data, layout=layout)
                py.plot(fig, filename='grouped-bar')
            if boi[-1]=='attack':
                query='''
                    SELECT Attack
                    FROM PokemonStats
                    WHERE Name = (?)
                '''
                params=(boi[1],)
                cur.execute(query, params)

                title='Pokemon '+boi[-1].capitalize()
                stat=[]
                for row in cur:
                    stat+=[row[0]]

                query='''
                    SELECT Attack
                    FROM PokemonStats
                    WHERE Name = (?)
                '''
                params=(boi[2],)
                cur.execute(query, params)

                stats=[]
                for row in cur:
                    stats+=[row[0]]

                conn.commit()
                conn.close()

                trace1 = go.Bar(
                    x=[boi[1]],
                    y=stat,
                    name='Pokemon 1'
                )
                trace2 = go.Bar(
                    x=[boi[2]],
                    y=stats,
                    name='Pokemon 2'
                )
                data = [trace1, trace2]
                layout = go.Layout(
                    barmode='group',
                    title=title,
                    xaxis=dict(
                title='Pokemon Name',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )), yaxis=dict(
                title=boi[-1].capitalize(),
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f')))
                fig = go.Figure(data=data, layout=layout)
                py.plot(fig, filename='grouped-bar')
            if boi[-1]=='defense':
                query='''
                    SELECT Defense
                    FROM PokemonStats
                    WHERE Name = (?)
                '''
                params=(boi[1],)
                cur.execute(query, params)

                title='Pokemon '+boi[-1].capitalize()
                stat=[]
                for row in cur:
                    stat+=[row[0]]

                query='''
                    SELECT Defense
                    FROM PokemonStats
                    WHERE Name = (?)
                '''
                params=(boi[2],)
                cur.execute(query, params)

                stats=[]
                for row in cur:
                    stats+=[row[0]]

                conn.commit()
                conn.close()

                trace1 = go.Bar(
                    x=[boi[1]],
                    y=stat,
                    name='Pokemon 1'
                )
                trace2 = go.Bar(
                    x=[boi[2]],
                    y=stats,
                    name='Pokemon 2'
                )
                data = [trace1, trace2]
                layout = go.Layout(
                    barmode='group',
                    title=title,
                    xaxis=dict(
                title='Pokemon Name',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )), yaxis=dict(
                title=boi[-1].capitalize(),
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f')))
                fig = go.Figure(data=data, layout=layout)
                py.plot(fig, filename='grouped-bar')
            if boi[-1]=='hp':
                query='''
                    SELECT HP
                    FROM PokemonStats
                    WHERE Name = (?)
                '''
                params=(boi[1],)
                cur.execute(query, params)

                title='Pokemon '+boi[-1].upper()
                stat=[]
                for row in cur:
                    stat+=[row[0]]

                query='''
                    SELECT HP
                    FROM PokemonStats
                    WHERE Name = (?)
                '''
                params=(boi[2],)
                cur.execute(query, params)

                stats=[]
                for row in cur:
                    stats+=[row[0]]

                conn.commit()
                conn.close()

                trace1 = go.Bar(
                    x=[boi[1]],
                    y=stat,
                    name='Pokemon 1'
                )
                trace2 = go.Bar(
                    x=[boi[2]],
                    y=stats,
                    name='Pokemon 2'
                )
                data = [trace1, trace2]
                layout = go.Layout(
                    barmode='group',
                    title=title,
                    xaxis=dict(
                title='Pokemon Name',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )), yaxis=dict(
                title=boi[-1].upper(),
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f')))
                fig = go.Figure(data=data, layout=layout)
                py.plot(fig, filename='grouped-bar')
            if boi[-1]=='specialattack':
                query='''
                    SELECT SpecialAttack
                    FROM PokemonStats
                    WHERE Name = (?)
                '''
                params=(boi[1],)
                cur.execute(query, params)

                title='Pokemon Special Attack'
                stat=[]
                for row in cur:
                    stat+=[row[0]]

                query='''
                    SELECT SpecialAttack
                    FROM PokemonStats
                    WHERE Name = (?)
                '''
                params=(boi[2],)
                cur.execute(query, params)

                stats=[]
                for row in cur:
                    stats+=[row[0]]

                conn.commit()
                conn.close()

                trace1 = go.Bar(
                    x=[boi[1]],
                    y=stat,
                    name='Pokemon 1'
                )
                trace2 = go.Bar(
                    x=[boi[2]],
                    y=stats,
                    name='Pokemon 2'
                )
                data = [trace1, trace2]
                layout = go.Layout(
                    barmode='group',
                    title=title,
                    xaxis=dict(
                title='Pokemon Name',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )), yaxis=dict(
                title=title,
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f')))
                fig = go.Figure(data=data, layout=layout)
                py.plot(fig, filename='grouped-bar')
            if boi[-1]=='specialdefense':
                query='''
                    SELECT SpecialDefense
                    FROM PokemonStats
                    WHERE Name = (?)
                '''
                params=(boi[1],)
                cur.execute(query, params)

                title='Pokemon Special Defense'
                stat=[]
                for row in cur:
                    stat+=[row[0]]

                query='''
                    SELECT SpecialDefense
                    FROM PokemonStats
                    WHERE Name = (?)
                '''
                params=(boi[2],)
                cur.execute(query, params)

                stats=[]
                for row in cur:
                    stats+=[row[0]]

                conn.commit()
                conn.close()

                trace1 = go.Bar(
                    x=[boi[1]],
                    y=stat,
                    name='Pokemon 1'
                )
                trace2 = go.Bar(
                    x=[boi[2]],
                    y=stats,
                    name='Pokemon 2'
                )
                data = [trace1, trace2]
                layout = go.Layout(
                    barmode='group',
                    title=title,
                    xaxis=dict(
                title='Pokemon Name',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )), yaxis=dict(
                title=title,
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f')))
                fig = go.Figure(data=data, layout=layout)
                py.plot(fig, filename='grouped-bar')
        except:
            print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")

    elif user_input=='exit':
        print('Happy Training!')
        break

    else:
        print("That isn't valid. Maybe type in 'variations' or 'help' if you're having trouble.")

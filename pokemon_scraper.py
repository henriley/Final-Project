import requests
import json
from secrets import *
import codecs
import sys
import sqlite3

sys.stdout=codecs.getwriter('utf-8')(sys.stdout.buffer)

DBNAME='Pokemon.db'

try:
    fref=open('cache_data.json', 'r')
    data=fref.read()
    CACHE_DICT=json.loads(data)
    fref.close()
except:
    CACHE_DICT={}

class apizzle:

	def __init__(self, baseurl, pokemon):
		self.totalurl='/'.join([baseurl,pokemon])

	def __str__(self):
		return str(self.totalurl)

def get_data_using_cache(url,param=None):
    unique_identifier=url

    if url in CACHE_DICT:
        print('Getting from cache...')
        return CACHE_DICT[unique_identifier]
    else:
        if param==None:
            print("Requesting new data...")
            resp=requests.get(url)
            CACHE_DICT[unique_identifier]=resp.text
            fref=open('cache_data.json','w')
            dumped_data=json.dumps(CACHE_DICT)
            fref.write(dumped_data)
            fref.close()
            return CACHE_DICT[unique_identifier]
        else:
            unique_identifier=url+str(param)
            print("Requesting new data...")
            resp=requests.get(url,param)
            CACHE_DICT[unique_identifier]=json.loads(resp.content.decode('utf-8'))
            fref=open('cache_data.json','w')
            dumped_data=json.dumps(CACHE_DICT)
            fref.write(dumped_data)
            fref.close()
            return CACHE_DICT[unique_identifier]

def auth():
    request = 'https://www.deviantart.com/oauth2/token'
    params = {
        'grant_type' : 'client_credentials',
        'client_id': int(client_id),
        'client_secret': client_secret
    }
    r = get_data_using_cache(request, params)
    return r

def get_deviant(pokemon):
    if pokemon=='metagross-mega':
        pokemon='mega metagross'
    request = 'https://www.deviantart.com/api/v1/oauth2/browse/popular'
    params = {
        'q' : pokemon,
        'access_token': auth()['access_token']
    }
    r = get_data_using_cache(request, params)
    return r['results'][0]['url']

def get_pokemon_data(pokemon):
    totalurl=apizzle("https://pokeapi.co/api/v2/pokemon", pokemon)
    req=get_data_using_cache(totalurl.__str__())
    poke_data=json.loads(req)
    # poke=json.dumps(poke_data, indent=2)
    return poke_data

def get_pokemon_species(pokemon):
    totalurl=apizzle('https://pokeapi.co/api/v2/pokemon-species', pokemon)
    req=get_data_using_cache(totalurl.__str__())
    poke_data=json.loads(req)

    return poke_data

def get_pokemon_speed(pokemon):
    poke_data=get_pokemon_data(pokemon)

    return poke_data['stats'][0]['base_stat']

def get_pokemon_special_defense(pokemon):
    poke_data=get_pokemon_data(pokemon)

    return poke_data['stats'][1]['base_stat']

def get_pokemon_special_attack(pokemon):
    poke_data=get_pokemon_data(pokemon)

    return poke_data['stats'][2]['base_stat']

def get_pokemon_defense(pokemon):
    poke_data=get_pokemon_data(pokemon)

    return poke_data['stats'][3]['base_stat']

def get_pokemon_attack(pokemon):
    poke_data=get_pokemon_data(pokemon)

    return poke_data['stats'][4]['base_stat']

def get_pokemon_hp(pokemon):
    poke_data=get_pokemon_data(pokemon)

    return poke_data['stats'][5]['base_stat']

def get_pokemon_heightYweight(pokemon):
    poke_data=get_pokemon_data(pokemon)
    #WEIGHT IS IN KILOGRAMS. HEIGHT IS IN METERS.
    return {'height':str(round(int(poke_data['height'])*0.1, 2))+' meters', 'weight':str(round(int(poke_data['weight'])*0.1, 2))+' kilograms'}

def get_pokedex_number(pokemon):
    poke_data=get_pokemon_data(pokemon)

    if 'venusaur' in pokemon:
        return get_pokemon_data('venusaur')['id']
    elif 'charizard' in pokemon:
        return get_pokemon_data('charizard')['id']
    elif 'blastoise' in pokemon:
        return get_pokemon_data('blastoise')['id']
    elif 'alakazam' in pokemon:
        return get_pokemon_data('alakazam')['id']
    elif 'gengar' in pokemon:
        return get_pokemon_data('gengar')['id']
    elif 'kangaskhan' in pokemon:
        return get_pokemon_data('kangaskhan')['id']
    elif 'pinsir' in pokemon:
        return get_pokemon_data('pinsir')['id']
    elif 'gyarados' in pokemon:
        return get_pokemon_data('gyarados')['id']
    elif 'aerodactyl' in pokemon:
        return get_pokemon_data('aerodactyl')['id']
    elif 'mewtwo' in pokemon:
        return get_pokemon_data('mewtwo')['id']
    elif 'ampharos' in pokemon:
        return get_pokemon_data('ampharos')['id']
    elif 'scizor' in pokemon:
        return get_pokemon_data('scizor')['id']
    elif 'heracross' in pokemon:
        return get_pokemon_data('heracross')['id']
    elif 'houndoom' in pokemon:
        return get_pokemon_data('houndoom')['id']
    elif 'tyranitar' in pokemon:
        return get_pokemon_data('tyranitar')['id']
    elif 'blaziken' in pokemon:
        return get_pokemon_data('blaziken')['id']
    elif 'gardevoir' in pokemon:
        return get_pokemon_data('gardevoir')['id']
    elif 'mawile' in pokemon:
        return get_pokemon_data('mawile')['id']
    elif 'aggron' in pokemon:
        return get_pokemon_data('aggron')['id']
    elif 'medicham' in pokemon:
        return get_pokemon_data('medicham')['id']
    elif 'banette' in pokemon:
        return get_pokemon_data('banette')['id']
    elif 'absol' in pokemon:
        return get_pokemon_data('absol')['id']
    elif 'garchomp' in pokemon:
        return get_pokemon_data('garchomp')['id']
    elif 'lucario' in pokemon:
        return get_pokemon_data('lucario')['id']
    elif 'abomasnow' in pokemon:
        return get_pokemon_data('abomasnow')['id']
    elif 'latias' in pokemon:
        return get_pokemon_data('latias')['id']
    elif 'latios' in pokemon:
        return get_pokemon_data('latios')['id']
    elif 'swampert' in pokemon:
        return get_pokemon_data('swampert')['id']
    elif 'sceptile' in pokemon:
        return get_pokemon_data('sceptile')['id']
    elif 'sableye' in pokemon:
        return get_pokemon_data('sableye')['id']
    elif 'altaria' in pokemon:
        return get_pokemon_data('altaria')['id']
    elif 'gallade' in pokemon:
        return get_pokemon_data('gallade')['id']
    elif 'audino' in pokemon:
        return get_pokemon_data('audino')['id']
    elif 'sharpedo' in pokemon:
        return get_pokemon_data('sharpedo')['id']
    elif 'slowbro' in pokemon:
        return get_pokemon_data('slowbro')['id']
    elif 'steelix' in pokemon:
        return get_pokemon_data('steelix')['id']
    elif 'pidgeot-' in pokemon:
        return get_pokemon_data('pidgeot')['id']
    elif 'glalie' in pokemon:
        return get_pokemon_data('glalie')['id']
    elif 'diancie' in pokemon:
        return get_pokemon_data('diancie')['id']
    elif 'metagross' in pokemon:
        return get_pokemon_data('metagross')['id']
    elif 'rayquaza' in pokemon:
        return get_pokemon_data('rayquaza')['id']
    elif 'camerupt' in pokemon:
        return get_pokemon_data('camerupt')['id']
    elif 'lopunny' in pokemon:
        return get_pokemon_data('lopunny')['id']
    elif 'salamence' in pokemon:
        return get_pokemon_data('salamence')['id']
    elif 'beedrill' in pokemon:
        return get_pokemon_data('beedrill')['id']
    elif 'wormadam' in pokemon:
        return get_pokemon_data('wormadam-plant')['id']
    elif 'meowstic' in pokemon:
        return get_pokemon_data('meowstic-male')['id']
    elif 'aegislash' in pokemon:
        return get_pokemon_data('aegislash-shield')['id']
    elif 'basculin' in pokemon:
        return get_pokemon_data('basculin-red-striped')['id']
    elif 'pumpkaboo' in pokemon:
        return get_pokemon_data('pumpkaboo-average')['id']
    elif 'darmanitan' in pokemon:
        return get_pokemon_data('darmanitan-standard')['id']
    elif 'gourgeist' in pokemon:
        return get_pokemon_data('gourgeist-average')['id']
    elif 'giratina' in pokemon:
        return get_pokemon_data('giratina-altered')['id']
    elif 'shaymin' in pokemon:
        return get_pokemon_data('shaymin-land')['id']
    elif 'deoxys' in pokemon:
        return get_pokemon_data('deoxys-normal')['id']
    elif 'tornadus' in pokemon:
        return get_pokemon_data('tornadus-incarnate')['id']
    elif 'thundurus' in pokemon:
        return get_pokemon_data('thundurus-incarnate')['id']
    elif 'landorus' in pokemon:
        return get_pokemon_data('landorus-incarnate')['id']
    elif 'keldeo' in pokemon:
        return get_pokemon_data('keldeo-ordinary')['id']
    elif 'kyurem' in pokemon:
        return get_pokemon_data('kyurem')['id']
    elif 'rotom' in pokemon:
        return get_pokemon_data('rotom')['id']
    elif 'manectric' in pokemon:
        return get_pokemon_data('manectric')['id']
    elif 'kyogre' in pokemon:
        return get_pokemon_data('kyogre')['id']
    elif 'groudon' in pokemon:
        return get_pokemon_data('groudon')['id']
    elif 'meloetta' in pokemon:
        return get_pokemon_data('meloetta-aria')['id']
    elif 'castform' in pokemon:
        return get_pokemon_data('castform')['id']
    elif 'rattata' in pokemon:
        return get_pokemon_data('rattata')['id']
    elif 'raticate' in pokemon:
        return get_pokemon_data('raticate')['id']
    elif 'raichu' in pokemon:
        return get_pokemon_data('raichu')['id']
    elif 'oricorio' in pokemon:
        return get_pokemon_data('oricorio-baile')['id']
    elif 'lycanroc' in pokemon:
        return get_pokemon_data('lycanroc-midday')['id']
    elif 'wishiwashi' in pokemon:
        return get_pokemon_data('wishiwashi-solo')['id']
    elif 'minior' in pokemon:
        return get_pokemon_data('minior-red-meteor')['id']
    elif 'mimikyu' in pokemon:
        return get_pokemon_data('mimikyu-disguised')['id']
    elif 'zygarde' in pokemon:
        return get_pokemon_data('zygarde')['id']
    elif 'magearna' in pokemon:
        return get_pokemon_data('magearna')['id']
    elif 'marowak' in pokemon:
        return get_pokemon_data('marowak')['id']
    elif 'exeggutor' in pokemon:
        return get_pokemon_data('exeggutor')['id']
    elif 'muk' in pokemon:
        return get_pokemon_data('muk')['id']
    elif 'grimer' in pokemon:
        return get_pokemon_data('grimer')['id']
    elif 'golem' in pokemon:
        return get_pokemon_data('golem')['id']
    elif 'graveler' in pokemon:
        return get_pokemon_data('graveler')['id']
    elif 'geodude' in pokemon:
        return get_pokemon_data('geodude')['id']
    elif 'persian' in pokemon:
        return get_pokemon_data('persian')['id']
    elif 'meowth' in pokemon:
        return get_pokemon_data('meowth')['id']
    elif 'dugtrio' in pokemon:
        return get_pokemon_data('dugtrio')['id']
    elif 'diglett' in pokemon:
        return get_pokemon_data('diglett')['id']
    elif 'ninetales' in pokemon:
        return get_pokemon_data('ninetales')['id']
    elif 'vulpix' in pokemon:
        return get_pokemon_data('vulpix')['id']
    elif 'sandslash' in pokemon:
        return get_pokemon_data('sandslash')['id']
    elif 'sandshrew' in pokemon:
        return get_pokemon_data('sandshrew')['id']
    else:
        return poke_data['id']

def get_pokemon_ability(pokemon):
    poke_data=get_pokemon_data(pokemon)

    abilities={}
    for x in poke_data['abilities']:
        if x['slot']==1:
            abilities['ability1']=x['ability']['name']
        if x['slot']==2:
            abilities['ability2']=x['ability']['name']
        if x['slot']==3:
            abilities['hidden_ability']=x['ability']['name']

    return abilities

def get_pokemon_ability_id(pokemon):
    poke_data=get_pokemon_data(pokemon)

    abilities={}
    for x in poke_data['abilities']:
        if x['slot']==1:
            abilities['ability1']={x['ability']['name']:x['ability']['url'].split('/')[-2]}
        if x['slot']==2:
            abilities['ability2']={x['ability']['name']:x['ability']['url'].split('/')[-2]}
        if x['slot']==3:
            abilities['hidden_ability']={x['ability']['name']:x['ability']['url'].split('/')[-2]}

    return abilities

def get_pokemon_ability_id_2(pokemon):
    poke_data=get_pokemon_data(pokemon)

    abilities=[]
    for x in poke_data['abilities']:
        if x['slot']==1:
            abilities.append(x['ability']['url'].split('/')[-2])
        if x['slot']==2:
            abilities.append(x['ability']['url'].split('/')[-2])
        if x['slot']==3:
            abilities.append(x['ability']['url'].split('/')[-2])

    return abilities

def get_pokemon_ability_info(ability):
    totalurl=apizzle("https://pokeapi.co/api/v2/ability", ability)
    req=get_data_using_cache(totalurl.__str__())
    poke_data=json.loads(req)
    # poke=json.dumps(poke_data, indent=2)

    return poke_data['effect_entries'][0]['effect']

def get_pokemon_evolutions(pokemon):
    if 'venusaur' in pokemon:
        pokemon='venusaur'
    elif 'charizard' in pokemon:
        pokemon='charizard'
    elif 'blastoise' in pokemon:
        pokemon='blastoise'
    elif 'alakazam' in pokemon:
        pokemon='alakazam'
    elif 'gengar' in pokemon:
        pokemon='gengar'
    elif 'kangaskhan' in pokemon:
        pokemon='kangaskhan'
    elif 'pinsir' in pokemon:
        pokemon='pinsir'
    elif 'gyarados' in pokemon:
        pokemon='gyarados'
    elif 'aerodactyl' in pokemon:
        pokemon='aerodactyl'
    elif 'mewtwo' in pokemon:
        pokemon='mewtwo'
    elif 'ampharos' in pokemon:
        pokemon='ampharos'
    elif 'scizor' in pokemon:
        pokemon='scizor'
    elif 'heracross' in pokemon:
        pokemon='heracross'
    elif 'houndoom' in pokemon:
        pokemon='houndoom'
    elif 'tyranitar' in pokemon:
        pokemon='tyranitar'
    elif 'blaziken' in pokemon:
        pokemon='blaziken'
    elif 'gardevoir' in pokemon:
        pokemon='gardevoir'
    elif 'mawile' in pokemon:
        pokemon='mawile'
    elif 'aggron' in pokemon:
        pokemon='aggron'
    elif 'medicham' in pokemon:
        pokemon='medicham'
    elif 'banette' in pokemon:
        pokemon='banette'
    elif 'absol' in pokemon:
        pokemon='absol'
    elif 'garchomp' in pokemon:
        pokemon='garchomp'
    elif 'lucario' in pokemon:
        pokemon='lucario'
    elif 'abomasnow' in pokemon:
        pokemon='abomasnow'
    elif 'latias' in pokemon:
        pokemon='latias'
    elif 'latios' in pokemon:
        pokemon='latios'
    elif 'swampert' in pokemon:
        pokemon='swampert'
    elif 'sceptile' in pokemon:
        pokemon='sceptile'
    elif 'sableye' in pokemon:
        pokemon='sableye'
    elif 'altaria' in pokemon:
        pokemon='altaria'
    elif 'gallade' in pokemon:
        pokemon='gallade'
    elif 'audino' in pokemon:
        pokemon='audino'
    elif 'sharpedo' in pokemon:
        pokemon='sharpedo'
    elif 'slowbro' in pokemon:
        pokemon='slowbro'
    elif 'steelix' in pokemon:
        pokemon='steelix'
    elif 'pidgeot-' in pokemon:
        pokemon='pidgeot'
    elif 'glalie' in pokemon:
        pokemon='glalie'
    elif 'diancie' in pokemon:
        pokemon='diancie'
    elif 'metagross' in pokemon:
        pokemon='metagross'
    elif 'rayquaza' in pokemon:
        pokemon='rayquaza'
    elif 'camerupt' in pokemon:
        pokemon='camerupt'
    elif 'lopunny' in pokemon:
        pokemon='lopunny'
    elif 'salamence' in pokemon:
        pokemon='salamence'
    elif 'beedrill' in pokemon:
        pokemon='beedrill'
    elif 'wormadam' in pokemon:
        pokemon='wormadam'
    elif 'meowstic' in pokemon:
        pokemon='meowstic'
    elif 'aegislash' in pokemon:
        pokemon='aegislash'
    elif 'basculin' in pokemon:
        pokemon='basculin'
    elif 'pumpkaboo' in pokemon:
        pokemon='pumpkaboo'
    elif 'darmanitan' in pokemon:
        pokemon='darmanitan'
    elif 'gourgeist' in pokemon:
        pokemon='gourgeist'
    elif 'giratina' in pokemon:
        pokemon='giratina'
    elif 'shaymin' in pokemon:
        pokemon='shaymin'
    elif 'deoxys' in pokemon:
        pokemon='deoxys'
    elif 'tornadus' in pokemon:
        pokemon='tornadus'
    elif 'thundurus' in pokemon:
        pokemon='thundurus'
    elif 'landorus' in pokemon:
        pokemon='landorus'
    elif 'keldeo' in pokemon:
        pokemon='keldeo'
    elif 'kyurem' in pokemon:
        pokemon='kyurem'
    elif 'rotom' in pokemon:
        pokemon='rotom'
    elif 'manectric' in pokemon:
        pokemon='manectric'
    elif 'kyogre' in pokemon:
        pokemon='kyogre'
    elif 'groudon' in pokemon:
        pokemon='groudon'
    elif 'meloetta' in pokemon:
        pokemon='meloetta'
    elif 'castform' in pokemon:
        pokemon='castform'
    elif 'rattata' in pokemon:
        pokemon='rattata'
    elif 'raticate' in pokemon:
        pokemon='raticate'
    elif 'raichu' in pokemon:
        pokemon='raichu'
    elif 'oricorio' in pokemon:
        pokemon='oricorio'
    elif 'lycanroc' in pokemon:
        pokemon='lycanroc'
    elif 'wishiwashi' in pokemon:
        pokemon='wishiwashi'
    elif 'minior' in pokemon:
        pokemon='minior'
    elif 'mimikyu' in pokemon:
        pokemon='mimikyu'
    elif 'zygarde' in pokemon:
        pokemon='zygarde'
    elif 'magearna' in pokemon:
        pokemon='magearna'
    elif 'marowak' in pokemon:
        pokemon='marowak'
    elif 'exeggutor' in pokemon:
        pokemon='exeggutor'
    elif 'muk' in pokemon:
        pokemon='muk'
    elif 'grimer' in pokemon:
        pokemon='grimer'
    elif 'golem' in pokemon:
        pokemon='golem'
    elif 'graveler' in pokemon:
        pokemon='graveler'
    elif 'geodude' in pokemon:
        pokemon='geodude'
    elif 'persian' in pokemon:
        pokemon='persian'
    elif 'meowth' in pokemon:
        pokemon='meowth'
    elif 'dugtrio' in pokemon:
        pokemon='dugtrio'
    elif 'diglett' in pokemon:
        pokemon='diglett'
    elif 'ninetales' in pokemon:
        pokemon='ninetales'
    elif 'vulpix' in pokemon:
        pokemon='vulpix'
    elif 'sandslash' in pokemon:
        pokemon='sandslash'
    elif 'sandshrew' in pokemon:
        pokemon='sandshrew'

    totalurl=apizzle('https://pokeapi.co/api/v2/pokemon-species', pokemon)
    req=get_data_using_cache(totalurl.__str__())
    poke_data=json.loads(req)

    evourl=poke_data['evolution_chain']['url']
    req2=get_data_using_cache(evourl)
    poke_data2=json.loads(req2)
    # poke=json.dumps(poke_data2, indent=2)

    chain={}
    bain=[]
    try:
        bain.append(poke_data2['chain']['species']['name'])
    except:
        pass
    try:
        for x in poke_data2['chain']['evolves_to']:
            bain.append(x['species']['name'])
    except:
        pass
    try:
        for x in poke_data2['chain']['evolves_to'][0]['evolves_to']:
            bain.append(x['species']['name'])
    except:
        pass

    za=get_pokemon_species(pokemon)['evolution_chain']['url']
    id_evo=za.split('/')

    if id_evo[-2] not in chain:
        chain[id_evo[-2]]=bain

    return chain

def get_pokemon_evolutions_id(pokemon):
    if 'venusaur' in pokemon:
        pokemon='venusaur'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'charizard' in pokemon:
        pokemon='charizard'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'blastoise' in pokemon:
        pokemon='blastoise'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'alakazam' in pokemon:
        pokemon='alakazam'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'gengar' in pokemon:
        pokemon='gengar'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'kangaskhan' in pokemon:
        pokemon='kangaskhan'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'pinsir' in pokemon:
        pokemon='pinsir'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'gyarados' in pokemon:
        pokemon='gyarados'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'aerodactyl' in pokemon:
        pokemon='aerodactyl'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'mewtwo' in pokemon:
        pokemon='mewtwo'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'ampharos' in pokemon:
        pokemon='ampharos'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'scizor' in pokemon:
        pokemon='scizor'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'heracross' in pokemon:
        pokemon='heracross'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'houndoom' in pokemon:
        pokemon='houndoom'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'tyranitar' in pokemon:
        pokemon='tyranitar'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'blaziken' in pokemon:
        pokemon='blaziken'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'gardevoir' in pokemon:
        pokemon='gardevoir'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'mawile' in pokemon:
        pokemon='mawile'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'aggron' in pokemon:
        pokemon='aggron'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'medicham' in pokemon:
        pokemon='medicham'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'banette' in pokemon:
        pokemon='banette'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'absol' in pokemon:
        pokemon='absol'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'garchomp' in pokemon:
        pokemon='garchomp'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'lucario' in pokemon:
        pokemon='lucario'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'abomasnow' in pokemon:
        pokemon='abomasnow'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'latias' in pokemon:
        pokemon='latias'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'latios' in pokemon:
        pokemon='latios'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'swampert' in pokemon:
        pokemon='swampert'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'sceptile' in pokemon:
        pokemon='sceptile'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'sableye' in pokemon:
        pokemon='sableye'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'altaria' in pokemon:
        pokemon='altaria'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'gallade' in pokemon:
        pokemon='gallade'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'audino' in pokemon:
        pokemon='audino'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'sharpedo' in pokemon:
        pokemon='sharpedo'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'slowbro' in pokemon:
        pokemon='slowbro'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'steelix' in pokemon:
        pokemon='steelix'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'pidgeot-' in pokemon:
        evourl=get_pokemon_species('pidgeot')['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'glalie' in pokemon:
        pokemon='glalie'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'diancie' in pokemon:
        pokemon='diancie'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'metagross' in pokemon:
        pokemon='metagross'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'rayquaza' in pokemon:
        pokemon='rayquaza'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'camerupt' in pokemon:
        pokemon='camerupt'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'lopunny' in pokemon:
        pokemon='lopunny'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'salamence' in pokemon:
        pokemon='salamence'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'beedrill' in pokemon:
        pokemon='beedrill'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'wormadam' in pokemon:
        pokemon='wormadam'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'meowstic' in pokemon:
        pokemon='meowstic'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'aegislash' in pokemon:
        pokemon='aegislash'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'basculin' in pokemon:
        pokemon='basculin'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'pumpkaboo' in pokemon:
        pokemon='pumpkaboo'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'darmanitan' in pokemon:
        pokemon='darmanitan'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'gourgeist' in pokemon:
        pokemon='gourgeist'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'giratina' in pokemon:
        pokemon='giratina'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'shaymin' in pokemon:
        pokemon='shaymin'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'deoxys' in pokemon:
        pokemon='deoxys'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'tornadus' in pokemon:
        pokemon='tornadus'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'thundurus' in pokemon:
        pokemon='thundurus'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'landorus' in pokemon:
        pokemon='landorus'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'keldeo' in pokemon:
        pokemon='keldeo'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'kyurem' in pokemon:
        pokemon='kyurem'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'rotom' in pokemon:
        pokemon='rotom'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'manectric' in pokemon:
        pokemon='manectric'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'kyogre' in pokemon:
        pokemon='kyogre'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'groudon' in pokemon:
        pokemon='groudon'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'meloetta' in pokemon:
        pokemon='meloetta'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'castform' in pokemon:
        pokemon='castform'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'rattata' in pokemon:
        pokemon='rattata'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'raticate' in pokemon:
        pokemon='raticate'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'raichu' in pokemon:
        pokemon='raichu'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'oricorio' in pokemon:
        pokemon='oricorio'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'lycanroc' in pokemon:
        pokemon='lycanroc'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'wishiwashi' in pokemon:
        pokemon='wishiwashi'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'minior' in pokemon:
        pokemon='minior'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'mimikyu' in pokemon:
        pokemon='mimikyu'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'zygarde' in pokemon:
        pokemon='zygarde'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'magearna' in pokemon:
        pokemon='magearna'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'marowak' in pokemon:
        pokemon='marowak'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'exeggutor' in pokemon:
        pokemon='exeggutor'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'muk' in pokemon:
        pokemon='muk'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'grimer' in pokemon:
        pokemon='grimer'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'golem' in pokemon:
        pokemon='golem'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'graveler' in pokemon:
        pokemon='graveler'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'geodude' in pokemon:
        pokemon='geodude'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'persian' in pokemon:
        pokemon='persian'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'meowth' in pokemon:
        pokemon='meowth'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'dugtrio' in pokemon:
        pokemon='dugtrio'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'diglett' in pokemon:
        pokemon='diglett'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'ninetales' in pokemon:
        pokemon='ninetales'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'vulpix' in pokemon:
        pokemon='vulpix'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'sandslash' in pokemon:
        pokemon='sandslash'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    elif 'sandshrew' in pokemon:
        pokemon='sandshrew'
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]
    else:
        evourl=get_pokemon_species(pokemon)['evolution_chain']['url']
        id_evo=evourl.split('/')
        return id_evo[-2]

def get_pokemon_type(pokemon):
    poke_data=get_pokemon_data(pokemon)

    types={}
    for x in poke_data['types']:
        if x['slot']==1:
            types['type1']=x['type']['name']
        if x['slot']==2:
            types['type2']=x['type']['name']
    return types

def init_db_1():
    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()

    # Drop tables
    statement='''
        DROP TABLE IF EXISTS 'PokemonStats';
    '''
    cur.execute(statement)
    conn.commit()

    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()

    statement='''
        CREATE TABLE 'PokemonStats'(
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'Name' TEXT,
            'PokeDexNumber' INTEGER,
            'Type1' TEXT,
            'Type2' TEXT,
            'Ability1' TEXT,
            'Ability1Id' INTEGER,
            'Ability2' TEXT,
            'Ability2Id' INTEGER,
            'HiddenAbility' TEXT,
            'HiddenAbilityId' INTEGER,
            'Height' INTEGER,
            'Weight' INTEGER,
            'HP' INTEGER,
            'Attack' INTEGER,
            'SpecialAttack' INTEGER,
            'Defense' INTEGER,
            'SpecialDefense' INTEGER,
            'Speed' INTEGER,
            'EvolutionId' INTEGER
        );
    '''
    cur.execute(statement)
    conn.commit()

    conn.close()

def init_db_2():
    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()

    # Drop tables
    statement='''
        DROP TABLE IF EXISTS 'Abilities';
    '''
    cur.execute(statement)
    conn.commit()

    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()

    statement='''
        CREATE TABLE 'Abilities'(
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'AbilityName' TEXT,
            'AbilityInfo' TEXT,
            'AbilityId' INTEGER
        );
    '''
    cur.execute(statement)
    conn.commit()

    conn.close()

def init_db_3():
    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()

    # Drop tables
    statement='''
        DROP TABLE IF EXISTS 'Evolutions';
    '''
    cur.execute(statement)
    conn.commit()

    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()

    statement='''
        CREATE TABLE 'Evolutions'(
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'Stage1' TEXT,
            'Stage2' TEXT,
            'Stage3' TEXT,
            'Stage4' TEXT,
            'Stage5' TEXT,
            'Stage6' TEXT,
            'Stage7' TEXT,
            'Stage8' TEXT,
            'Stage9' TEXT,
            'EvolutionId' INTEGER
        );
    '''
    cur.execute(statement)
    conn.commit()

    conn.close()

def init_db_4():
    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()

    # Drop tables
    statement='''
        DROP TABLE IF EXISTS 'DeviantArt';
    '''
    cur.execute(statement)
    conn.commit()

    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()

    statement='''
        CREATE TABLE 'DeviantArt'(
            'Id' INTEGER,
            'Name' TEXT,
            'DeviantURL' TEXT
        );
    '''
    cur.execute(statement)
    conn.commit()

    conn.close()

def insert_stuff_1(pokemon_list):
    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()

    for x in pokemon_list:
        try:
            insertion=(None, x, get_pokedex_number(x), get_pokemon_type(x)['type1'], None, \
            get_pokemon_ability(x)['ability1'], None, None, None, None, None, get_pokemon_heightYweight(x)['height'], \
            get_pokemon_heightYweight(x)['weight'], get_pokemon_hp(x), get_pokemon_attack(x), get_pokemon_special_attack(x), \
            get_pokemon_defense(x), get_pokemon_special_defense(x), get_pokemon_speed(x), get_pokemon_evolutions_id(x))
            statement='INSERT INTO "PokemonStats" '
            statement+='VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            cur.execute(statement, insertion)
        except:
            pass

    conn.commit()
    conn.close()

def insert_stuff_2(pokemon_list):
    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()

    liss=[]

    for x in pokemon_list:
        for x in get_pokemon_ability_id_2(x):
            if int(x) not in liss:
                liss.append(int(x))

    for x in liss:
        try:
            insertion=(None, None, None, x)
            statement='INSERT INTO "Abilities" '
            statement+='VALUES (?, ?, ?, ?)'
            cur.execute(statement, insertion)
        except:
            pass

    conn.commit()
    conn.close()

def insert_stuff_3(pokemon_list):
    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()

    diss=[]

    for x in pokemon_list:
        if int(get_pokemon_evolutions_id(x)) not in diss:
            diss.append(int(get_pokemon_evolutions_id(x)))

    for x in diss:
        try:
            insertion=(None, None, None, None, None, None, None, None, None, None, x)
            statement='INSERT INTO "Evolutions" '
            statement+='VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            cur.execute(statement, insertion)
        except:
            pass

    conn.commit()
    conn.close()

def insert_stuff_4():
    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()
    query='''
        SELECT Id, Name
        FROM PokemonStats
    '''
    cur.execute(query)

    all_abs={}
    for row in cur:
        all_abs[row[1]]=row[0]

    for x in all_abs:
        try:
            insertion=(all_abs[x], x, None)
            statement='INSERT INTO "DeviantArt" '
            statement+='VALUES (?, ?, ?)'
            cur.execute(statement, insertion)
        except:
            pass

    conn.commit()
    conn.close()

def update_stuff_1(pokemon_list):
    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()

    for x in pokemon_list:
        try:
            insert='''
            UPDATE PokemonStats
            SET Ability2 = (?)
            WHERE Name = (?)
            '''
            params=(get_pokemon_ability(x)['ability2'], x,)
            cur.execute(insert, params)
            conn.commit()
        except:
            pass
        try:
            insert='''
            UPDATE PokemonStats
            SET HiddenAbility = (?)
            WHERE Name = (?)
            '''
            params=(get_pokemon_ability(x)['hidden_ability'], x,)
            cur.execute(insert, params)
            conn.commit()
        except:
            pass
        try:
            insert='''
            UPDATE PokemonStats
            SET Type2 = (?)
            WHERE Name = (?)
            '''
            params=(get_pokemon_type(x)['type2'], x,)
            cur.execute(insert, params)
            conn.commit()
        except:
            pass
        try:
            insert='''
            UPDATE PokemonStats
            SET Ability1Id = (?)
            WHERE Ability1 = (?)
            '''
            params=(list(get_pokemon_ability_id(x)['ability1'].values())[0], list(get_pokemon_ability_id(x)['ability1'].keys())[0],)
            cur.execute(insert, params)
            conn.commit()
        except:
            pass
        try:
            insert='''
            UPDATE PokemonStats
            SET Ability2Id = (?)
            WHERE Ability2 = (?)
            '''
            params=(list(get_pokemon_ability_id(x)['ability2'].values())[0], list(get_pokemon_ability_id(x)['ability2'].keys())[0],)
            cur.execute(insert, params)
            conn.commit()
        except:
            pass
        try:
            insert='''
            UPDATE PokemonStats
            SET HiddenAbilityId = (?)
            WHERE HiddenAbility = (?)
            '''
            params=(list(get_pokemon_ability_id(x)['hidden_ability'].values())[0], list(get_pokemon_ability_id(x)['hidden_ability'].keys())[0],)
            cur.execute(insert, params)
            conn.commit()
        except:
            pass
    conn.close()

def update_stuff_2():
    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()
    query='''
        SELECT *
        FROM PokemonStats
    '''
    cur.execute(query)


    all_abs={}
    for x in cur:
        if x[5] not in all_abs:
            all_abs[x[5]]=x[6]
        if x[7] not in all_abs and x[7]!=None:
            all_abs[x[7]]=x[8]
        if x[9] not in all_abs and x[9]!=None:
            all_abs[x[9]]=x[10]

    for x in all_abs:
        insert='''
        UPDATE Abilities
        SET AbilityName = (?)
        WHERE AbilityId =(?)
        '''
        params=(x, all_abs[x],)
        cur.execute(insert, params)

    for x in all_abs:
        insert='''
        UPDATE Abilities
        SET AbilityInfo = (?)
        WHERE AbilityId =(?)
        '''
        params=(get_pokemon_ability_info(x), all_abs[x],)
        cur.execute(insert, params)

    conn.commit()
    conn.close()

def update_stuff_3(pokemon_list):
    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()

    piss=[]
    for x in pokemon_list:
        try:
            if get_pokemon_evolutions(x) in piss:
                pass
            else:
                piss.append(get_pokemon_evolutions(x))
        except:
            pass

    try:
        for x in piss:
            insert='''
            UPDATE Evolutions
            SET Stage1 = (?)
            WHERE EvolutionId = (?)
            '''
            params=(list(x.values())[0][0], list(x.keys())[0],)
            cur.execute(insert, params)
    except:
        pass
    try:
        for x in piss:
            if len(list(x.values())[0])>1:
                insert='''
                UPDATE Evolutions
                SET Stage2 = (?)
                WHERE EvolutionId = (?)
                '''
                params=(list(x.values())[0][1], list(x.keys())[0],)
                cur.execute(insert, params)
    except:
        pass
    try:
        for x in piss:
            if len(list(x.values())[0])>2:
                insert='''
                UPDATE Evolutions
                SET Stage3 = (?)
                WHERE EvolutionId = (?)
                '''
                params=(list(x.values())[0][2], list(x.keys())[0],)
                cur.execute(insert, params)
    except:
        pass
    try:
        for x in piss:
            if len(list(x.values())[0])>3:
                insert='''
                UPDATE Evolutions
                SET Stage4 = (?)
                WHERE EvolutionId = (?)
                '''
                params=(list(x.values())[0][3], list(x.keys())[0],)
                cur.execute(insert, params)
    except:
        pass
    try:
        for x in piss:
            if len(list(x.values())[0])>4:
                insert='''
                UPDATE Evolutions
                SET Stage5 = (?)
                WHERE EvolutionId = (?)
                '''
                params=(list(x.values())[0][4], list(x.keys())[0],)
                cur.execute(insert, params)
    except:
        pass
    try:
        for x in piss:
            if len(list(x.values())[0])>5:
                insert='''
                UPDATE Evolutions
                SET Stage6 = (?)
                WHERE EvolutionId = (?)
                '''
                params=(list(x.values())[0][5], list(x.keys())[0],)
                cur.execute(insert, params)
    except:
        pass
    try:
        for x in piss:
            if len(list(x.values())[0])>6:
                insert='''
                UPDATE Evolutions
                SET Stage7 = (?)
                WHERE EvolutionId = (?)
                '''
                params=(list(x.values())[0][6], list(x.keys())[0],)
                cur.execute(insert, params)
    except:
        pass
    try:
        for x in piss:
            if len(list(x.values())[0])>7:
                insert='''
                UPDATE Evolutions
                SET Stage8 = (?)
                WHERE EvolutionId = (?)
                '''
                params=(list(x.values())[0][7], list(x.keys())[0],)
                cur.execute(insert, params)
    except:
        pass
    try:
        for x in piss:
            if len(list(x.values())[0])>8:
                insert='''
                UPDATE Evolutions
                SET Stage9 = (?)
                WHERE EvolutionId = (?)
                '''
                params=(list(x.values())[0][8], list(x.keys())[0],)
                cur.execute(insert, params)
    except:
        pass

    conn.commit()
    conn.close()

def update_stuff_4(pokemon_list):
    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()

    for x in pokemon_list:
        try:
            insert='''
            UPDATE DeviantArt
            SET DeviantURL = (?)
            WHERE Name = (?)
            '''
            params=(get_deviant(x), x,)
            cur.execute(insert, params)
            conn.commit()
        except:
            pass

pokemon_list=['bulbasaur', 'chikorita', 'treecko', 'turtwig', 'victini', 'chespin', 'rowlet', \
'ivysaur', 'bayleef', 'grovyle', 'grotle', 'snivy', 'quilladin', 'dartrix', \
'venusaur',	'meganium', 'sceptile',	'torterra', 'servine', 'chesnaught', 'decidueye', \
'charmander', 'cyndaquil', 'pansear', 'torchic', 'chimchar', 'serperior', 'fennekin', 'litten', \
'charmeleon', 'quilava', 'combusken', 'monferno', 'tepig', 'braixen', 'torracat', \
'charizard', 'typhlosion', 'blaziken', 'infernape', 'pignite', 'delphox', 'incineroar', \
'squirtle', 'totodile', 'mudkip', 'piplup', 'emboar', 'froakie', 'popplio', \
'wartortle', 'oshawott', 'frogadier', 'brionne', 'croconaw', 'marshtomp', 'prinplup', 'goomy', \
'blastoise', 'feraligatr', 'swampert', 'empoleon', 'gliscor', 'dewott', 'greninja', 'primarina', \
'caterpie', 'sentret', 'poochyena', 'starly', 'samurott', 'bunnelby', 'pikipek', \
'metapod', 'furret', 'mightyena', 'staravia', 'patrat', 'diggersby', 'trumbeak', \
'butterfree', 'hoothoot', 'zigzagoon', 'staraptor', 'watchog', 'fletchling', 'toucannon', \
'weedle', 'noctowl', 'linoone', 'bidoof', 'lillipup', 'fletchinder', 'yungoos', \
'kakuna', 'ledyba', 'wurmple', 'bibarel', 'herdier', 'talonflame', 'gumshoos', \
'beedrill', 'ledian', 'silcoon', 'kricketot', 'stoutland', 'scatterbug', 'grubbin', \
'pidgey', 'spinarak', 'beautifly', 'kricketune', 'purrloin', 'spewpa', 'charjabug', \
'pidgeotto', 'ariados', 'cascoon', 'shinx', 'liepard', 'vivillon', 'vikavolt', \
'pidgeot', 'crobat', 'dustox', 'luxio', 'pansage', 'litleo', 'crabrawler', \
'rattata', 'chinchou', 'lotad', 'luxray', 'simisage', 'pyroar', 'crabominable', \
'raticate', 'lanturn', 'lombre', 'budew', 'flabebe', 'oricorio-baile', \
'spearow', 'pichu', 'ludicolo', 'roserade', 'simisear', 'floette', 'cutiefly', \
'fearow', 'cleffa', 'seedot', 'cranidos', 'panpour', 'florges', 'ribombee', \
'ekans', 'igglybuff', 'nuzleaf', 'rampardos', 'simipour', 'skiddo', 'rockruff', \
'arbok', 'togepi', 'shiftry', 'shieldon', 'munna', 'gogoat', 'lycanroc-midday', \
'pikachu', 'togetic', 'taillow', 'bastiodon', 'musharna', 'pancham', 'wishiwashi-solo', \
'raichu', 'natu', 'swellow', 'burmy', 'pidove', 'pangoro', 'mareanie', \
'sandshrew', 'xatu', 'wingull', 'tranquill', 'furfrou', 'toxapex', \
'sandslash', 'mareep', 'pelipper', 'mothim', 'unfezant', 'espurr', 'mudbray', \
'flaaffy', 'ralts', 'combee', 'blitzle', 'mudsdale', 'crustle', 'noibat', \
'nidorina', 'ampharos', 'surskit', 'buizel', 'boldore', 'fomantis', 'machop', 'ursaring', 'swalot', 'drapion', \
'nidorino', 'azumarill', 'masquerain', 'floatzel', 'gigalith', 'spritzee', 'lurantis', \
'nidoking', 'sudowoodo', 'shroomish', 'cherubi', 'woobat', 'aromatisse', 'morelull', \
'clefairy', 'politoed', 'breloom', 'cherrim', 'swoobat', 'swirlix', 'shiinotic', \
'clefable', 'hoppip', 'slakoth', 'shellos', 'drilbur', 'slurpuff', 'salandit', \
'vulpix', 'skiploom', 'vigoroth', 'gastrodon', 'excadrill', 'inkay', 'salazzle', \
'ninetales', 'jumpluff', 'slaking', 'ambipom', 'audino', 'malamar', 'stufful', \
'jigglypuff', 'aipom', 'nincada', 'drifloon', 'timburr', 'binacle', 'bewear', \
'wigglytuff', 'sunkern', 'ninjask', 'drifblim', 'gurdurr', 'barbaracle', 'bounsweet', \
'zubat', 'sunflora', 'shedinja', 'buneary', 'conkeldurr', 'skrelp', 'steenee', \
'golbat', 'yanma', 'whismur', 'lopunny', 'tympole', 'dragalge', 'tsareena', \
'oddish', 'wooper', 'loudred', 'mismagius', 'palpitoad', 'clauncher', 'comfey', \
'gloom', 'quagsire', 'exploud', 'honchkrow', 'seismitoad', 'clawitzer', 'oranguru', \
'vileplume', 'espeon', 'makuhita', 'glameow', 'throh', 'helioptile', 'passimian', \
'paras', 'umbreon', 'hariyama', 'purugly', 'sawk', 'heliolisk', 'wimpod', \
'parasect', 'murkrow', 'azurill', 'chingling', 'sewaddle', 'tyrunt', 'golisopod', \
'venonat', 'slowking', 'nosepass', 'stunky', 'swadloon', 'tyrantrum', 'sandygast', \
'venomoth', 'misdreavus', 'skitty', 'skuntank', 'leavanny', 'amaura', 'palossand', \
'diglett', 'unown', 'delcatty', 'bronzor', 'venipede', 'aurorus', 'pyukumuku', \
'dugtrio', 'wobbuffet', 'sableye', 'bronzong', 'whirlipede', 'sylveon', \
'meowth', 'girafarig', 'mawile', 'bonsly', 'scolipede', 'hawlucha', 'silvally', \
'persian', 'pineco', 'aron', 'cottonee', 'dedenne', \
'psyduck', 'forretress', 'lairon', 'happiny', 'whimsicott', 'carbink', 'komala', \
'golduck', 'dunsparce', 'aggron', 'chatot', 'petilil', 'turtonator', \
'mankey', 'gligar', 'meditite', 'spiritomb', 'lilligant', 'sliggoo', 'togedemaru', \
'primeape', 'steelix', 'medicham', 'gible', 'goodra', \
'growlithe', 'snubbull', 'electrike', 'gabite', 'sandile', 'klefki', 'bruxish', \
'arcanine', 'granbull', 'manectric', 'garchomp', 'krokorok', 'phantump', 'drampa', \
'poliwag', 'qwilfish', 'plusle', 'munchlax', 'krookodile', 'trevenant', 'dhelmise', \
'poliwhirl', 'scizor', 'minun', 'riolu', 'darumaka', 'jangmo-o', \
'poliwrath', 'shuckle', 'volbeat', 'lucario', 'hakamo-o', \
'abra', 'heracross', 'illumise', 'hippopotas', 'maractus', 'bergmite', 'kommo-o', \
'kadabra', 'sneasel', 'roselia', 'hippowdon', 'dwebble', 'avalugg', \
'alakazam', 'teddiursa', 'gulpin', 'skorupi', 'scraggy', 'noivern', \
'machoke', 'slugma', 'carvanha', 'croagunk', 'scrafty', 'xerneas', \
'machamp', 'magcargo', 'sharpedo', 'toxicroak', 'sigilyph', 'yveltal', 'cosmog', \
'bellsprout', 'swinub', 'wailmer', 'carnivine', 'yamask', 'zygarde', 'cosmoem', \
'weepinbell', 'piloswine', 'wailord', 'finneon', 'cofagrigus', 'diancie', 'solgaleo', \
'victreebel', 'corsola', 'numel', 'lumineon', 'tirtouga', 'hoopa', 'lunala', \
'tentacool', 'remoraid', 'camerupt', 'mantyke', 'carracosta', 'volcanion', 'nihilego', \
'tentacruel', 'octillery', 'torkoal', 'snover', 'archen', 'buzzwole', \
'geodude', 'delibird', 'spoink', 'abomasnow', 'archeops', 'pheromosa', \
'graveler', 'mantine', 'grumpig', 'weavile', 'trubbish', 'xurkitree', \
'golem', 'skarmory', 'spinda', 'magnezone', 'garbodor', 'celesteela', \
'ponyta', 'houndour', 'trapinch', 'lickilicky', 'zorua', 'kartana', \
'rapidash', 'houndoom', 'vibrava', 'rhyperior', 'zoroark', 'guzzlord', \
'slowpoke', 'kingdra', 'flygon', 'tangrowth', 'minccino', 'necrozma', \
'slowbro', 'phanpy', 'cacnea', 'electivire', 'cinccino', 'magearna', \
'magnemite', 'donphan', 'cacturne', 'magmortar', 'gothita', 'marshadow', \
'magneton', 'porygon2', 'swablu', 'togekiss', 'gothorita', \
'stantler', 'altaria', 'yanmega', 'gothitelle', \
'doduo', 'smeargle', 'zangoose', 'leafeon', 'solosis', \
'dodrio', 'tyrogue', 'seviper', 'glaceon', 'duosion', \
'seel', 'hitmontop', 'lunatone', 'reuniclus', \
'dewgong', 'smoochum', 'solrock', 'mamoswine', 'ducklett', \
'grimer', 'elekid', 'barboach', 'porygon-z', 'swanna', \
'muk', 'magby', 'whiscash', 'gallade', 'vanillite', \
'shellder', 'miltank', 'corphish', 'probopass', 'vanillish', \
'cloyster', 'blissey', 'crawdaunt', 'dusknoir', 'vanilluxe', \
'gastly', 'raikou', 'baltoy', 'froslass', 'deerling', \
'haunter', 'entei', 'claydol', 'rotom', 'sawsbuck', \
'gengar', 'suicune', 'lileep', 'uxie', 'emolga', \
'onix', 'larvitar', 'cradily', 'mesprit', 'karrablast', \
'drowzee', 'pupitar', 'anorith', 'azelf', 'escavalier', \
'hypno', 'tyranitar', 'armaldo', 'dialga', 'foongus', \
'krabby', 'lugia', 'feebas', 'palkia', 'amoonguss', \
'kingler', 'ho-oh', 'milotic', 'heatran', 'frillish', \
'voltorb', 'celebi', 'castform', 'regigigas', 'jellicent', \
'electrode', 'kecleon', 'alomomola', \
'exeggcute', 'shuppet', 'cresselia', 'joltik', \
'exeggutor', 'banette', 'phione', 'galvantula', \
'cubone', 'duskull', 'manaphy', 'ferroseed', \
'marowak', 'dusclops', 'darkrai', 'ferrothorn', \
'hitmonlee', 'tropius', 'klink', 'hitmonchan', 'chimecho', 'arceus', 'klang', 'lickitung', 'absol', 'klinklang', \
'koffing', 'wynaut', 'tynamo', 'weezing', 'snorunt', 'eelektrik', \
'rhyhorn', 'glalie', 'eelektross', 'rhydon', 'spheal', 'elgyem', \
'chansey', 'sealeo', 'beheeyem', 'tangela', 'walrein', 'litwick', \
'kangaskhan', 'clamperl', 'lampent', 'horsea', 'huntail', 'chandelure', \
'gorebyss', 'axew', 'goldeen', 'relicanth', 'fraxure', 'luvdisc', 'haxorus', 'cryogonal', \
'scyther', 'beldum', 'shelmet', 'jynx', 'metang', 'accelgor', \
'electabuzz', 'metagross', 'stunfisk', 'magmar', 'regirock', 'mienfoo', \
'pinsir', 'regice', 'mienshao', 'tauros', 'registeel', 'druddigon', \
'magikarp', 'latias', 'golett', 'gyarados', 'latios', 'golurk', \
'lapras', 'kyogre', 'pawniard', 'ditto', 'groudon', 'bisharp', \
'eevee', 'rayquaza', 'bouffalant', 'vaporeon', 'jirachi', 'rufflet', \
'jolteon', 'braviary', 'flareon', 'vullaby', \
'porygon', 'mandibuzz', 'omanyte', 'heatmor', 'omastar', 'durant', \
'kabuto', 'deino', 'kabutops', 'zweilous', 'aerodactyl', 'hydreigon', \
'snorlax', 'larvesta', 'articuno', 'volcarona', 'zapdos', 'cobalion', \
'moltres', 'terrakion', 'dratini', 'virizion', 'dragonair', \
'dragonite', 'mewtwo', 'reshiram', 'mew', 'zekrom', 'kyurem', 'genesect', \
'oricorio-sensu','oricorio-pau','oricorio-pom-pom','lycanroc-midnight', \
'wishiwashi-school','wormadam-plant','wormadam-sandy','wormadam-trash','nidoran-f', \
'nidoran-m','meowstic-female','meowstic-male','aegislash-shield','aegislash-blade','type-null', \
'mr-mime','mime-jr','minior-red-meteor','minior-orange-meteor','minior-yellow-meteor','minior-green-meteor', \
'minior-blue-meteor','minior-indigo-meteor','minior-violet-meteor','minior-red','minior-orange','minior-yellow', \
'minior-green','minior-blue','minior-indigo','minior-violet','basculin-red-striped','basculin-blue-striped', \
'mimikyu-busted','mimikyu-disguised','pumpkaboo-small','pumpkaboo-average','pumpkaboo-large','pumpkaboo-super', \
'darmanitan-zen','darmanitan-standard','gourgeist-small','gourgeist-average','gourgeist-large','gourgeist-super', \
'tapu-koko','tapu-lele','tapu-bulu','tapu-fini','farfetchd','giratina-altered', \
'giratina-origin','shaymin-land','shaymin-sky','deoxys-normal','deoxys-attack','deoxys-defense', \
'deoxys-speed','tornadus-therian','tornadus-incarnate','thundurus-therian','thundurus-incarnate','landorus-therian', \
'landorus-incarnate','keldeo-ordinary','keldeo-resolute','kyurem-black','kyurem-white','rotom-heat', \
'rotom-wash','rotom-frost','rotom-fan','rotom-mow','venusaur-mega','charizard-mega-x', \
'charizard-mega-y','blastoise-mega','alakazam-mega','gengar-mega','kangaskhan-mega','pinsir-mega', \
'gyarados-mega','aerodactyl-mega','mewtwo-mega-x','mewtwo-mega-y','ampharos-mega','scizor-mega', \
'heracross-mega','houndoom-mega','tyranitar-mega','blaziken-mega','gardevoir-mega','mawile-mega', \
'aggron-mega','medicham-mega','manectric-mega','banette-mega','absol-mega','garchomp-mega', \
'lucario-mega','abomasnow-mega','latias-mega','latios-mega','swampert-mega','sceptile-mega', \
'sableye-mega','altaria-mega','gallade-mega','audino-mega','sharpedo-mega','slowbro-mega', \
'steelix-mega','pidgeot-mega','glalie-mega','diancie-mega','metagross-mega','kyogre-primal', \
'groudon-primal','rayquaza-mega','camerupt-mega','lopunny-mega','salamence-mega','beedrill-mega', \
'meloetta-aria','meloetta-pirouette','castform-sunny','castform-rainy','castform-snowy','zygarde-10', \
'zygarde-50','zygarde-complete','magearna-original','rattata-alola','raticate-alola','raichu-alola', \
'sandshrew-alola','sandslash-alola','vulpix-alola','ninetales-alola','diglett-alola','dugtrio-alola', 'meowth-alola', \
'persian-alola','geodude-alola','graveler-alola','golem-alola','grimer-alola','muk-alola','exeggutor-alola','marowak-alola']

init_db_1()
init_db_2()
init_db_3()
init_db_4()
insert_stuff_1(pokemon_list)
insert_stuff_2(pokemon_list)
insert_stuff_3(pokemon_list)
insert_stuff_4()
update_stuff_1(pokemon_list)
update_stuff_2()
update_stuff_3(pokemon_list)
update_stuff_4(pokemon_list)

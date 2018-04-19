# Final-Project
My program uses two files to run. One of them is the pokemon_scraper.py and the other is pokemon_interface.py. pokemon_scraper.py gets all the necessary data for my database and sets up all the tables. The necessary data comes from a restful API and one API that requires OAuth2 to access. My program will help all trainers who want to learn more about Pokemon for training and battling purposes.

restful PokeAPI -- https://pokeapi.co/api/v2/
OAuth2 API DeviantArt to get token -- https://www.deviantart.com/oauth2/token

The DeviantArt API needs a client_id and a client_secret. The access token needs to be reauthorized every hour to get the data. You can go to https://www.deviantart.com/developers/http/v1/20160316 to get the id and secret. You'll need to create an account and create a developer account to do so. You can import the keys by creating a secrets.py.

secrets.py needs to be imported into all of my files.

I am also using plotly which will need a key and will need to be put in secrets.py.

In pokemon_scraper, I have all of the init_db, insert_stuff, and update_stuff functions are used to create and insert data into my database. The get_pokemon_data and the get_pokemon_species functions are the main functions that use the PokeAPI to get the data for all other functions to propagate my database. The get_deviant function is used to get the DeviantArt URLs and to reauthorize my OAuth every time. pokemon_list is the list used for all function inputs. It is a list of all Pokemon that can and will be entered into my functions to get my data for the database. Finally, apizzle is the class that is used in all my PokeAPI calls to create URLs.

Plotly is used in pokemon_interface only when the graph command is called.

For the pokemon_interface commands:
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

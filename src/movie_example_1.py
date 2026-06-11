from paths import *
from owlready2 import *

PREDEFINED_ONTOLOGIES["http://purl.org/nemo/gufo#"] = PATH_TO_MY_GUFO

onto_movies = get_ontology(PATH_TO_MY_ONTO).load()

print(onto_movies.base_iri)

# Instâncias de gêneros
action = onto_movies.Action()
drama = onto_movies.Drama()
scifi = onto_movies.SciFi()
romance = onto_movies.Romance()
comedy = onto_movies.Comedy()
horror = onto_movies.Horror()

# Ficção científica + ação
matrix = onto_movies.Movie("matrix")
matrix.belongs_To_Genre = [action, scifi]

star_wars = onto_movies.Movie("star_wars")
star_wars.belongs_To_Genre = [action, scifi]

terminator = onto_movies.Movie("terminator")
terminator.belongs_To_Genre = [action, scifi]

avatar = onto_movies.Movie("avatar")
avatar.belongs_To_Genre = [action, scifi]

# Ficção científica + drama
interstellar = onto_movies.Movie("interstellar")
interstellar.belongs_To_Genre = [scifi, drama]

arrival = onto_movies.Movie("arrival")
arrival.belongs_To_Genre = [scifi, drama]

# Ação
john_wick = onto_movies.Movie("john_wick")
john_wick.belongs_To_Genre = [action]

mad_max = onto_movies.Movie("mad_max")
mad_max.belongs_To_Genre = [action]

gladiator = onto_movies.Movie("gladiator")
gladiator.belongs_To_Genre = [action, drama]

# Comédia
superbad = onto_movies.Movie("superbad")
superbad.belongs_To_Genre = [comedy]

the_mask = onto_movies.Movie("the_mask")
the_mask.belongs_To_Genre = [comedy]

hangover = onto_movies.Movie("hangover")
hangover.belongs_To_Genre = [comedy]

# Comédia + romance
notting_hill = onto_movies.Movie("notting_hill")
notting_hill.belongs_To_Genre = [comedy, romance]

crazy_rich_asians = onto_movies.Movie("crazy_rich_asians")
crazy_rich_asians.belongs_To_Genre = [comedy, romance]

# Drama
forrest_gump = onto_movies.Movie("forrest_gump")
forrest_gump.belongs_To_Genre = [drama]

green_mile = onto_movies.Movie("green_mile")
green_mile.belongs_To_Genre = [drama]

whiplash = onto_movies.Movie("whiplash")
whiplash.belongs_To_Genre = [drama]

# Romance
the_notebook = onto_movies.Movie("the_notebook")
the_notebook.belongs_To_Genre = [romance]

pride_and_prejudice = onto_movies.Movie("pride_and_prejudice")
pride_and_prejudice.belongs_To_Genre = [romance]

# Drama + Romance
titanic = onto_movies.Movie("titanic")
titanic.belongs_To_Genre = [drama, romance]

# Terror
it = onto_movies.Movie("it")
it.belongs_To_Genre = [horror]

conjuring = onto_movies.Movie("conjuring")
conjuring.belongs_To_Genre = [horror]

insidious = onto_movies.Movie("insidious")
insidious.belongs_To_Genre = [horror]

# Terror + ficção científica
alien = onto_movies.Movie("alien")
alien.belongs_To_Genre = [horror, scifi]

# Terror + ação
predator = onto_movies.Movie("predator")
predator.belongs_To_Genre = [horror, action]

#Comedia + Ação
jumanji = onto_movies.Movie("jumanji")
jumanji.belongs_To_Genre = [comedy, action]

sync_reasoner_hermit()
for i in range(1, 11): print('\n')

resultados = list(default_world.sparql("""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX : <http://example.com/MovieExample#>

    SELECT ?movie
    WHERE {
        ?movie rdf:type :ActionMovie .
    }
"""))

for movie in resultados:
    print(movie[0].name)
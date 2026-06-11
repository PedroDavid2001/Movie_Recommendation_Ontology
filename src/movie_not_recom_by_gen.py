from paths import *
from owlready2 import *

PREDEFINED_ONTOLOGIES["http://purl.org/nemo/gufo#"] = PATH_TO_MY_GUFO

onto_movies = get_ontology(PATH_TO_MY_ONTO).load()

print(onto_movies.base_iri)

# =================================================================
# Instâncias de gêneros
action = onto_movies.Action('action')
drama = onto_movies.Drama('drama')
scifi = onto_movies.SciFi('scifi')
romance = onto_movies.Romance('romance')
comedy = onto_movies.Comedy('comedy')
horror = onto_movies.Horror('horror')

# =================================================================
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

# =================================================================
# lista de usuários
alice = onto_movies.User("alice")
bob = onto_movies.User("bob")
carol = onto_movies.User("carol")
david = onto_movies.User("david")
eve = onto_movies.User("eve")
frank = onto_movies.User("frank")
grace = onto_movies.User("grace")
henry = onto_movies.User("henry")
ivy = onto_movies.User("ivy")
jack = onto_movies.User("jack")

# =================================================================
# Alice gosta de SciFi e Action
p1 = onto_movies.Positive_Genre_Preference("p1")
p1.mediatesUser = [alice]
p1.mediatesGenre = [scifi]

p2 = onto_movies.Positive_Genre_Preference("p2")
p2.mediatesUser = [alice]
p2.mediatesGenre = [action]

# Bob gosta de Action
p3 = onto_movies.Positive_Genre_Preference("p3")
p3.mediatesUser = [bob]
p3.mediatesGenre = [action]

# Carol gosta de Drama
p4 = onto_movies.Positive_Genre_Preference("p4")
p4.mediatesUser = [carol]
p4.mediatesGenre = [drama]

# David gosta de Horror
p5 = onto_movies.Positive_Genre_Preference("p5")
p5.mediatesUser = [david]
p5.mediatesGenre = [horror]

# Eve gosta de Romance
p6 = onto_movies.Positive_Genre_Preference("p6")
p6.mediatesUser = [eve]
p6.mediatesGenre = [romance]

# Frank gosta de Comedy
p7 = onto_movies.Positive_Genre_Preference("p7")
p7.mediatesUser = [frank]
p7.mediatesGenre = [comedy]

# Grace gosta de SciFi
p8 = onto_movies.Positive_Genre_Preference("p8")
p8.mediatesUser = [grace]
p8.mediatesGenre = [scifi]

# Henry não gosta de Horror
n1 = onto_movies.Negative_Genre_Preference("n1")
n1.mediatesUser = [henry]
n1.mediatesGenre = [horror]

# Ivy não gosta de Romance
n2 = onto_movies.Negative_Genre_Preference("n2")
n2.mediatesUser = [ivy]
n2.mediatesGenre = [romance]

n3 = onto_movies.Negative_Genre_Preference("n3")
n3.mediatesUser = [alice]
n3.mediatesGenre = [horror]

n4 = onto_movies.Negative_Genre_Preference("n4")
n4.mediatesUser = [bob]
n4.mediatesGenre = [romance]

sync_reasoner_hermit()

usuario = bob
for i in range(1, 11): print('\n')

query = f"""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://example.com/MovieExample#>

SELECT DISTINCT ?genre ?movie
WHERE {{

    ?pref rdf:type :Negative_Genre_Preference .

    ?pref :mediatesUser <{usuario.iri}> .
    ?pref :mediatesGenre ?genre .

    ?movie :belongs_To_Genre ?genre .
}}
"""

generos = set()
filmes = set()

for genre, movie in default_world.sparql(query):
    generos.add(genre.name)
    filmes.add(movie.name)

#EXIBICAO
print(
    f"{usuario.name} NÃO gosta dos gêneros: "
    f"{{{', '.join(sorted(generos))}}}"
)

print(
    f"Então NÃO vou recomendar: "
    f"{{{', '.join(sorted(filmes))}}}"
)

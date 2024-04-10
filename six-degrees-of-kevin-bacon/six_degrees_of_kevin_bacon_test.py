from six_degrees_of_kevin_bacon import build_graph, get_bacon_nr

source_actor = "Shane Carruth"
movies = {
    "Swiss Army Man": {
        "Daniel Radcliffe",
        "Paul Dano",
        "Shane Carruth",
        "Antonia Ribero",
        "Mary Elizabeth Winstead",
    },
    "Stir of Echoes": {
        "Illeana Douglas",
        "Kevin Bacon",
        "Zachary David Cope",
        "Kathryn Erbe",
    },
    "Grindhouse": {
        "Kurt Russell",
        "Tracie Thoms",
        "Vanessa Ferlito",
        "Sydney Tamiia Poitier",
        "Tom Savini",
        "Zoë Bell",
        "Rose McGowan",
        "Rosario Dawson",
        "Mary Elizabeth Winstead",
    },
    "Frost/Nixon": {"Kevin Bacon", "Frank Langella", "Michael Sheen", "Sam Rockwell"},
    "Friday the 13th": {
        "Jeannine Taylor",
        "Kevin Bacon",
        "Betsy Palmer",
        "Tom Savini",
        "Adrienne King",
        "Robbi Morgan",
    },
}


g = build_graph(movies)

bacon_nr = get_bacon_nr(source_actor, g)

print(bacon_nr)

# Define the Room class.
"""
    Représente une pièce dans un jeu d'aventure textuel.

    Une pièce est définie par un nom, une description, et des sorties possibles vers d'autres pièces.
    Chaque sortie est associée à une direction (ex: "nord", "sud").

    Attributs:
        name (str): Le nom de la pièce.
        description (str): Une description textuelle de la pièce.
        exits (dict): Un dictionnaire associant une direction à une autre pièce (Room).

    Méthodes:
        get_exit(direction): Retourne la pièce dans la direction spécifiée, ou None si elle n'existe pas.
        get_exit_string(): Retourne une chaîne de caractères listant les sorties disponibles.
        get_long_description(): Retourne une description détaillée de la pièce, incluant les sorties.

    Exceptions:
        Aucune exception n'est levée par cette classe.

    Exemples:
        >>> salle = Room("Cave", "dans un sous-sol froid et sombre.")
        >>> salle.get_exit_string()
        'Sorties: '
        >>> salle.exits["nord"] = Room("Couloir", "dans un long couloir peu éclairé.")
        >>> salle.get_exit("nord").name
        'Couloir'
        >>> print(salle.get_long_description())
        Vous êtes dans un sous-sol froid et sombre.
        <BLANKLINE>
        Sorties: nord,
        <BLANKLINE>
    """

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"

# Define the Player class.
"""
    Représente un joueur dans un jeu d'aventure textuel.

    Le joueur peut se déplacer entre les pièces et interagir avec l'environnement.

    Attributs:
        name (str): Le nom du joueur.
        current_room (Room): La pièce actuelle où se trouve le joueur.

    Méthodes:
        move(direction): Déplace le joueur dans la direction spécifiée, si possible.

    Exceptions:
        Aucune exception n'est levée par cette classe.

    Exemples:
        >>> salle1 = Room("Salle 1", "dans une salle vide.")
        >>> salle2 = Room("Salle 2", "dans une salle avec une porte au nord.")
        >>> salle1.exits["nord"] = salle2
        >>> joueur = Player("Axelle")
        >>> joueur.current_room = salle1
        >>> joueur.move("nord")
        Vous êtes dans une salle avec une porte au nord.
        <BLANKLINE>
        Sorties: nord,
        <BLANKLINE>
        True
        >>> joueur.move("est")
        Aucune porte dans cette direction !
        <BLANKLINE>
        False
    """
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    
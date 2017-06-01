class Point:
    """Represents a point"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """
        What to be returned when the Point is converted to a string
        :return: "x,y"
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __repr__(self):
        """
        How the Point look like in debug mode
        """
        return self.__str__()

    def __eq__(self, other):
        """
        Equivalence between 2 points
        :param other: 
        :return: 
        """
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """
        Non equivalence
        :param other: 
        :return: 
        """
        return not self == other


def create_point(x, y):
    """
    Creates a point location on the screen
    :param x: x
    :param y: y
    :return: point
    """
    return Point(x, y)

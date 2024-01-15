#!/usr/bin/python3
"""Square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectanglel"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__initializes Square.

        Args:
            size(int): size of the square
            x: x variable
            y: y variable

        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ strign representation of square"""

        return "[Square]" + " (" + str(self.id) + ") " + str(self.x) + "/" +\
            str(self.y) + " - " + str(self.width)

    @property
    def size(self):
        """size getter"""

        return super().width

    @size.setter
    def size(self, size):
        super(Square, Square).width.__set__(self, size)
        super(Square, Square).height.__set__(self, size)

    def update(self, *args, **kwargs):
        """Magic variables usage.

        Args:
            args: non-keyword arguments
            kwargs: key-worded arguments

        """
        if args is not None and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        if args is None or len(args) == 0:
            if kwargs is not None and len(kwargs) != 0:
                for k in kwargs:
                    if k == 'id':
                        self.id = kwargs[k]
                    if k == 'size':
                        self.size = kwargs[k]
                    if k == 'x':
                        self.x = kwargs[k]
                    if k == 'y':
                        self.y = kwargs[k]

    def to_dictionary(self):
        """dictionary represention of square"""

        kwargs = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return dict(**kwargs)

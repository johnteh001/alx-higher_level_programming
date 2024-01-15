#!/usr/bin/python3
""" Rectangle """

from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter.

        Raises:
            TypeError: If width is not integer
            ValueError: If width is <= 0

        """

        return self.__width

    @width.setter
    def width(self, width):
        """sets the width of the rectangle"""

        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """Gets the height of rectangle.

        Raises:
            TypeError: If height is not an integer
            ValueError: if height <= 0

        """

        return self.__height

    @height.setter
    def height(self, height):
        """sets the rectangle height."""

        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """Gets the x value

        Raises:
            TypeError: If x is not an integer
            ValueError: If x is less than zero

        """

        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x value"""

        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """Y getter

        Raises:
            TypeError: If y is not an integer
            ValueError: if y is less than zero

        """

        return self.__y

    @y.setter
    def y(self, y):
        """Sets y value"""

        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """Finds the area"""
        return self.__height * self.__width

    def display(self):
        """Prints Rectangle with #"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """String representatoin of Rectangle"""

        return "[Rectangle] (" + str(self.id) + ") " + str(self.__x) +\
            "/" + str(self.__y) + " - " +\
            str(self.__width) + "/" +\
            str(self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute

        Args:
            args: list of arguments.

    """
        if args is not None and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        if args is None or len(args) == 0:
            if kwargs is not None and len(kwargs) > 0:
                for k in kwargs:
                    if k == "id":
                        self.id = kwargs[k]
                        continue
                    if k == "width":
                        self.width = kwargs[k]
                        continue
                    if k == "height":
                        self.height = kwargs[k]
                        continue
                    if k == "x":
                        self.x = kwargs[k]
                        continue
                    if k == "y":
                        self.y = kwargs[k]

    def to_dictionary(self):
        """Gives dictionary represention of rectangle"""

        kwargs = {'x': self.x, 'y': self.y, 'id': self.id,
                  'height': self.height, 'width': self.width}
        return dict(**kwargs)

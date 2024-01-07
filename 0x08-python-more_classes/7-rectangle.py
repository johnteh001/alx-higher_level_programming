#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle class gives basic description of a rectangle

    Attributes:
        number_of_instances(int): instances of the rectangle objects created

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Obtains and sets the width of rectangle.

        Raises:
            TypeError: When the widht is not integer
            ValueError: When width < 0

        """

        return self.__width

    @width.setter
    def width(self, value):
        """sets width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Obtains the height of the rectangle.

        Raises:
            TypeError: when height is not integer.
            ValueError: When height < 0

        """

        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of rectangle height"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Determines the area of rectangle

        Returns:
            are of rectangle

        """
        return self.__width * self.__height

    def perimeter(self):
        """Determines the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        per = 2 * (self.__width + self.__height)
        return per

    def __str__(self):
        """Prints the square using # string

        Returns:
            # string repsentation of the rectangle

        """

        if self.__width == 0 or self.__height == 0:
            return ''
        new_rec = []
        for i in range(self.__height):
            for j in range(self.__width):
                new_rec.append(str(self.print_symbol))
            if i != self.__height - 1:
                new_rec.append('\n')
        return ''.join(new_rec)

    def __repr__(self):
        """For internal reprsentation of rectangle"""

        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"

    def __del__(self):
        """Deletes the object instance"""

        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

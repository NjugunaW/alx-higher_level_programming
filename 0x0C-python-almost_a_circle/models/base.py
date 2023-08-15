#!/usr/bin/python3

"""
A Class Base
"""
import json
import csv
import turtle

class Base:
    """
    This is the class that will be the base of all other classes in this project.
    The goal of this project is to manage attributes in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the class constructor
        Args:
            id (int): Integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method returns a JSON string.
        Args:
            list_dictionaries:
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This method writes the JSON into a file.
        Args:
            list_objs:
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """This method returns a list from a JSON string.
        Args:
            json_string:
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This method returns a class from a dictionary of attributes.
        Args:
            **dictionary: Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """This method returns a list of classes instantiated from a JSON file string.
        Reads from `<cls.__name__>.json`.
        Returns:
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This method saves a list of objects to a file.
        Args:
            list_objs:
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """This method loads files.
        Returns:
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """This method draws Rectangles and Squares using the turtle module.
        Args:
            list_rectangles:
            list_squares:
        """
        stylus = turtle.Turtle()
        stylus.screen.bgcolor("burgundy")
        stylus.pensize(3)
        stylus.shape("hexagon")

        stylus.color("magenta")
        for rect in list_rectangles:
            stylus.showturtle()
            stylus.up()
            stylus.goto(rect.x, rect.y)
            stylus.down()
            for i in range(2):
                stylus.forward(rect.width)
                stylus.left(90)
                stylus.forward(rect.height)
                stylus.left(90)
            stylus.hideturtle()

        stylus.color("cyan")
        for sq in list_squares:
            stylus.showturtle()
            stylus.up()
            stylus.goto(sq.x, sq.y)
            stylus.down()
            for i in range(2):
                stylus.forward(sq.width)
                stylus.left(90)
                stylus.forward(sq.height)
                stylus.left(90)
            stylus.hideturtle()

        turtle.exitonclick()


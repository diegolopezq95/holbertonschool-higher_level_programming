#!/usr/bin/python3
""" This module creates an empty class Square that defines a square
Example:
    ./100-main.py test file
Private instance attribute:
    size
"""


class Node:
    """ Empty class Node
    """
    def __init__(self, data, next_node=None):
        """
        Instantiation
        Args:
            data: data inside the node
            next_node: next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        data getter. Returns the data of the linked list
        """
        return (self.__size)

    @data.setter
    def data(self, value):
        """
        data setter. Sets the data of the linked list
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        next_node getter. Returns the next_node of the list
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        next_node setter. Sets the next_node of the list
        """
        if next_node is not None and type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """ Empty class Node
    """
    def __init__(self):
        """
        Instantiation
        Args:
            head: head node
        """
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)

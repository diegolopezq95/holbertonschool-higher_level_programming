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
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        data getter. Returns the data of the linked list
        """
        return (self.__data)

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
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
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
        """
        Inserts a node sorted
        """
        tmp = self.__head
        if self.__head is None:
            self.__head = Node(value, None)
        elif self.__head.data > value:
            self.__head = Node(value, tmp)
        else:
            while tmp is not None:
                if tmp.next_node is None:
                    tmp.next_node = Node(value)
                    break
                if tmp.next_node.data > value:
                    tmp.next_node = Node(value, tmp.next_node)
                    break
                tmp = tmp.next_node

    def __str__(self):
        """
        Returns linked list
        """
        tmp = self.__head
        linkedlist = []
        while tmp is not None:
            linkedlist.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(linkedlist))

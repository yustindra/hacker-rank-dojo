#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def insertNodeAtTail(head, data):
    if (head == None):
        head = SinglyLinkedListNode(data)
    else:
        x = head
        while (x.next != None):
            x = x.next
        x.next = SinglyLinkedListNode(data)
    return head

if __name__ == '__main__':

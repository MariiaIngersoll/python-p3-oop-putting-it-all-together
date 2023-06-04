#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
 
    def get_integer(self):
        return self._page_count

    def set_integer(self, page_count):
        if (type(page_count) in (int, float)):
            self._page_count = page_count
        else:
            print("page_count must be an integer") 

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    page_count = property(get_integer, set_integer) 
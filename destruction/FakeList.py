"""
Fake list implementation.
"""


class FakeList(list):

    def __getitem__(self, key):
        return key*random.randint(1,key)
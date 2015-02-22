from math import sqrt


class Vector2(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = sqrt(x*x + y*y)

# ----------------------------------------------------------------------------
# Operator Functions
# ----------------------------------------------------------------------------
    def __add__(self, other):
        try:
            return Vector2(self.x + other[0], self.y + other[1])
        except KeyError:
            try:
                return Vector2(self[0] + other['x'], self[1] + other['y'])
            except KeyError:
                return NotImplemented
        except IndexError:
            return NotImplemented

    def __sub__(self, other):
        return Vector2(self[0] - other[0], self[1] - other[1])

    def __mul__(self, other):
        raise NotImplementedError
        # Return dot product

    def __len__(self):
        return self.length

    def __getitem__(self, item):
        item_type = type(item)

        if item_type is str:
            if item == 'x':
                return self.x
            elif item == 'y':
                return self.y
            else:
                raise KeyError
        elif item_type is int:
            if item == 0:
                return self.x
            elif item == 1:
                return self.y
            else:
                raise IndexError
        else:
            raise TypeError

    def rotate(self, degrees):
        raise NotImplementedError

    def normalize(self):
        raise NotImplementedError

    def
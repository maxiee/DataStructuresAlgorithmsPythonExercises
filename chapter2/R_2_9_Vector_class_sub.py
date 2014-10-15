__author__ = 'maxiee'

class Vector:
    """
    Represent a vector in a multidimensional space.
    """

    def __init__(self,d):
        """
        Create d-dimensional vector of zeros.
        :param d:
        :return:
        """
        self._coords = [0] * d

    def __len__(self):
        """

        :return: the dimision of the vector.
        """
        return len(self._coords)

    def __getitem__(self, j):
        """

        :param j:
        :return: Return jth coordinate of vector.
        """
        return self._coords[j]

    def __setitem__(self, j, val):
        """
        Set jth coordinate of vector to given value.
        :param j:
        :param val:
        :return:
        """
        self._coords[j] = val

    def __add__(self, other):
        """
        Return sum of two vectors.
        :param other:
        :return:
        """
        if len(self) != len(other):     # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        """
        Return subtract of two vectors.
        :param other:
        :return:
        """
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __eq__(self, other):
        """
        Return True if vector has same coordinates as other.
        :param other:
        :return:
        """
        return self._coords == other._coords

    def __ne__(self, other):
        """
        Return True if vector differs from other.
        :param other:
        :return:
        """
        return not self == other

    def __str__(self):
        """
        Produce string representation of vector.
        :return:
        """
        return '<' + str(self._coords)[1:-1] + '>'  # conver to str first, then remove '[' and ']'

if __name__ == "__main__":
    # test
    v1 = Vector(3)
    v1.__setitem__(0, 1)
    v1.__setitem__(1, 2)
    v1.__setitem__(2, 3)
    v2 = Vector(3)
    v2.__setitem__(0, 1)
    v2.__setitem__(1, 2)
    v2.__setitem__(2, 3)
    print(v1.__add__(v2).__str__())
    print(v1.__sub__(v2).__str__())
class Vector:

    def __init__(self, vector):
        self.vector = vector
        self.vectorlen = len(vector)

    def __len__(self):
        return self.vectorlen

    def __getitem__(self, i):
        return self.vector[i]

    def __setitem__(self, i, val):
        self.vector[i] = val

    def __eq__(self, vector):
        if isinstance(vector, Vector):
            return self.vector == vector.vector
        return False

    def __str__(self):
        return str(tuple(self.vector)).replace(' ', '')

    def equals(self, vector):
        return self == vector

    def add(self, vector):
        if len(vector) != self.vectorlen:
            raise Exception('Vectors length differs')
        result = Vector(self.vector[:])
        for i, element in enumerate(vector):
            result[i] += element
        return result

    def subtract(self, vector):
        if len(vector) != self.vectorlen:
            raise Exception('Vectors length differs')
        result = Vector(self.vector[:])
        for i, element in enumerate(vector):
            result[i] -= element
        return result

    def dot(self, vector):
        if len(vector) != self.vectorlen:
            raise Exception('Vectors length differs')
        result = 0
        for i, element in enumerate(vector):
            result += element * self.vector[i]
        return result

    def norm(self):
        result = 0
        for element in self.vector:
            result += element**2
        return result**0.5

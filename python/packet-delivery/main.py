class DimensionsOutOfBound(Exception):

    def __init__(self, dimension, value, limit):
        self.str = "Package {}=={} out of bound, should be: " \
                "0 < {} <= {}".format(
                        dimension,
                        value,
                        dimension,
                        limit
                        )

    def __str__(self):
        return self.str

class Package(object):

    limits = {
        "length": 350,
        "width":  300,
        "height": 150,
        "weight": 40
    }

    def __init__(self, length, width, height, weight=None):
        self.length = length
        self.width  = width
        self.height = height
        if weight:
            self.weight = weight

    def __setattr__(self, attribute, value):
        if not (0 < value <= Package.limits[attribute]):
            raise DimensionsOutOfBound(attribute, value, self.limits[attribute])
        self.__dict__[attribute] = value

    @property
    def volume(self):
        return self.width * self.height * self.length


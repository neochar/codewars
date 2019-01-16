class Package(object):

    def __init__(self, length, width, height, weight=None):
        self._length = length
        self._width  = width
        self._height = height
        self._weight = weight

    @property
    def volume(self):
        return self._length * self._width * self._height

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value <= 0 or value > 350:
            raise DimensionsOutOfBoundError('Package length==% out of bound, should be: 0 < length <= 350'.format(value))
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if 0 >= value > 300:
            raise DimensionsOutOfBoundError('Package width==% out of bound, should be: 0 < width <= 300'.format(value))
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if 0 >= value > 150:
            raise DimensionsOutOfBoundError('Package height==% out of bound, should be: 0 < height <= 150'.format(value))
        self._height = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if 0 >= value > 40:
            raise DimensionsOutOfBoundError('Package weight==% out of bound, should be: 0 < weight <= 40'.format(value))
        self._weight = value

p = Package(0.2, 0.1, 0.2)
p.length = -20
print(p.length)

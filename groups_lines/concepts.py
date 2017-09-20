
import math
import collections
import uuid

Point = collections.namedtuple(
    'Point',
    ['x', 'y'])


DirectionCosines = collections.namedtuple(
    'DirectionCosines',
    ['rel_x', 'rel_y'])


Sector = collections.namedtuple(
    'Sector',
    ['start', 'end', 'get_direction_cosines'])


class Vector:

    __slots__ = ('id', 'start', 'end', 'coordinates')

    def __init__(self, start, end, id=None):
        self.id = uuid.uuid4().hex if id is None else id
        self.start = start
        self.end = end

        x = self.end.x - self.start.x
        y = self.end.y - self.start.y
        self.coordinates = Point(x, y)

    def serialize(self):
        template = '{} {} {} {} {}'

        return template.format(
            self.id,
            self.start.x,
            self.start.y,
            self.end.x,
            self.end.y)

    @property
    def length(self):
        x, y = self.coordinates.x, self.coordinates.y
        return math.sqrt(x * x + y * y)

    @property
    def angle(self):

        end = Point(
            self.end.x - self.start.x,
            self.end.y - self.start.y)

        dir_cos = DirectionCosines(
            end.x / self.length,
            end.y / self.length)

        angle_rel_x = math.acos(dir_cos.rel_x)
        angle_rel_y = math.acos(dir_cos.rel_y)

        delta = math.sin(angle_rel_x) - math.sin(angle_rel_y + math.pi / 2)

        if delta < 0.001:
            return angle_rel_x

        else:
            return 2 * math.pi - angle_rel_x

    def __repr__(self):
        template = 'Vector(id={}, start={}, end={})'
        res = template.format(self.id, self.start, self.end)
        return res


class LineGroup:

    '''Class implements group of lines which have fault from given angle or
       from given angle plus-minus pi/2 or from given angle plus pi less than
       or equal to 1 degree in both sides'''

    FAULT = math.radians(1)

    first_quart = (lambda angle:
        DirectionCosines(math.cos(angle), math.cos(math.pi / 2 - angle)))

    other_quarts = (lambda angle:
        DirectionCosines(math.cos(angle), math.cos(angle - math.pi / 2)))

    DIRECTION_COSINES = (first_quart, *[other_quarts] * 3)

    def __init__(self, angle):

        main_angles = (
            angle,
            angle + math.pi / 2,
            angle + math.pi,
            angle + 3 * math.pi / 2)

        self.sectors = []
        angles_and_dir_coses = zip(main_angles, self.DIRECTION_COSINES)

        for angle, direction_cosines in angles_and_dir_coses:
            sector_start, sector_end = angle - self.FAULT, angle + self.FAULT
            sector = Sector(sector_start, sector_end, direction_cosines)
            self.sectors.append(sector)

        self.vectors = []

    def correct_sectors(self, angle):
        if sector for sector in self.sectors if angle in sector:
            sector

    def __contains__(self, angle):
        return any(angle in sector for sector in self.sectors)

    def __repr__(self):

        res_str = 'LineGroup(id={} '.format(self.id)

        for sector in self.sectors:
            sector_start = math.degrees(sector.start)
            sector_end = math.degrees(sector.end)
            sector_str = '[{}, {}]'.format(sector_start, sector_end)
            res_str += sector_str + ', '

        return res_str + ')'

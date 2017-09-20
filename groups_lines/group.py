
from groups_lines.concepts import (
    Vector,
    Point)


class VectorsGroupper:

    ''' Class divides all given vectors into several groups by
        its angle relational positive Ox direction.'''

    def __init__(self, vectors):
        super().__init__()

        self.groups = None
        self.angles = {}

        for vector in vectors:
            self.angles[vector.id] = vector.angle

    @classmethod
    def from_file(cls, file_name):

        with open(file_name, 'r') as file:
            serialized_vectors = file.readlines()

        vectors = []

        for vector in serialized_vectors:
            splitted = vector.split()

            vector_id = splitted[0]

            coordinates = tuple(float(coordinate) for coordinate in splitted[1:])
            start = Point(*coordinates[:2])
            end = Point(*coordinates[2:])

            instance = Vector(id=vector_id, start=start, end=end)
            vectors.append(instance)

        return cls(vectors=vectors)

    def group_by_angle(self):
        sorted_angles = sorted(self.angles.values())
        initial_angle = sorted_angles[0]

        for angle in sorted_angles[1:]:




            initial_angle = get_initial_angele(angle)



    def __repr__(self):

        res = 'VectorSplitter(\n'

        for vector_id, angle in self.angles.items():
            vector_str = 'Vector(id={} angle={})\n'.format(vector_id, angle)
            res += vector_str

        res += ')'
        return res

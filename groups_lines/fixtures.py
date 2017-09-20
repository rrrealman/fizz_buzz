
import random
import math
import uuid
from .concepts import Point
from .concepts import Vector
from .concepts import LineGroup


class GenerateGroupFixture:

    def __init__(self, group):
        self.group = group
        self.vectors = []

    def generate_vectors(self, nvectors=None):

        nvectors = random.randint(10, 100) if nvectors is None else nvectors

        for nvector in range(nvectors):
            sector = random.choice(self.group.sectors)
            angle = random.uniform(sector.start, sector.end)

            vector_length = random.uniform(1, 100)
            dir_cos = sector.get_direction_cosines(angle)
            end_x = vector_length * dir_cos.rel_x
            end_y = vector_length * dir_cos.rel_y

            delta_x = random.uniform(-100, 100)
            delta_y = random.uniform(-100, 100)

            start = Point(delta_x, delta_y)
            end = Point(end_x + delta_x, end_y + delta_y)

            vector = Vector(start, end)

            self.vectors.append(vector)

    @property
    def serialized_vectors(self):

        vectors = []

        for vector in self.vectors:
            vectors.append(vector.serialize())

        return vectors

    @property
    def vector_ids(self):
        return [vector.id for vector in self.group.vectors]


def generate_groups(ngroups=None):

    ngroups = random.randint(10, 30) if ngroups is None else ngroups
    fixture_groups = {}
    initial_angles = list(range(1, 45))

    for group_number in range(ngroups):

        angle = random.choice(initial_angles)
        initial_angles.remove(angle)
        fixture_group = GenerateGroupFixture(group=LineGroup(angle))

        fixture_group.generate_vectors(nvectors=random.randint(10, 100))
        group_id = uuid.uuid4().hex

        fixture_groups[group_id] = fixture_group

    return fixture_groups


def generate_fixtures(fixture_groups):

    reference_groups = {}
    serialized_vectors = []

    for group_id, fixture_group in fixture_groups.items():
        reference_groups[group_id] = fixture_group.vector_ids

        serialized_vectors.extend(fixture_group.serialized_vectors)

    random.shuffle(serialized_vectors)
    return serialized_vectors, reference_groups


def write_vectors_file(file_name, lines):

    with open(file_name, 'w') as file:
        file.writelines('\n'.join(lines))

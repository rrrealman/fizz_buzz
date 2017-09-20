
import os
import uuid

from groups_lines.fixtures import (
    generate_fixtures,
    write_vectors_file,
    generate_groups)

from groups_lines.group import VectorsGroupper


def run_tests():
    groups = generate_groups()
    serialized_vectors, reference_groups = generate_fixtures(groups)

    file_name = uuid.uuid4().hex
    write_vectors_file(file_name=file_name, lines=serialized_vectors)

    # testing

    vectors_grouper = VectorsGroupper.from_file(file_name=file_name)
    vectors_grouper.group_by_angle()
    # assert vectors_grouper.groups == reference_groups
    print(vectors_grouper)

    # end testing

    os.remove(file_name)


if __name__ == '__main__':
    run_tests()
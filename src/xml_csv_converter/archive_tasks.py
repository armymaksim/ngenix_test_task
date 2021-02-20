import os
from typing import List
from uuid import uuid4
from zipfile import ZipFile

from .constants import (
    WORK_DIR,
    ZIP_SUFFIX,
    ZIP_COUNT,
    FILES_PER_ARCHIVE,
    XML_SUFFIX,
)
from .file_structure import XMLFileStructure
from .xml_tasks import generate_xml, parse_xml


def generate_archives():
    for _ in range(ZIP_COUNT):
        _create_archive()


def parse_archives() -> List[XMLFileStructure]:
    all_data = []
    for file_name in os.listdir(WORK_DIR):
        if file_name.endswith(ZIP_SUFFIX):
            all_data.extend(
                _parse_archive(
                    os.path.join(WORK_DIR, file_name)
                )
            )
    return all_data



def _parse_archive(file_path: str):
    result = []
    with ZipFile(file_path, 'r') as zipf:
        for filename in zipf.filelist:
            with zipf.open(filename, 'r') as xmlf:
                result.append(parse_xml(
                    xmlf.read().decode())
                )

    return result


def _create_archive():
    if not os.path.exists(WORK_DIR):
        os.mkdir(WORK_DIR)
    uuid_hex = uuid4().hex
    name = f'{uuid_hex}{ZIP_SUFFIX}'
    path = os.path.join(WORK_DIR, name)
    with ZipFile(path, 'w') as zipf:
        for i in range(FILES_PER_ARCHIVE):
            zipf.writestr(
                f'{uuid_hex}_{i}{XML_SUFFIX}',
                generate_xml()
            )

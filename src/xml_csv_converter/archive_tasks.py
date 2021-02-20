import os
from typing import List
from uuid import uuid4
from zipfile import ZipFile
from multiprocessing import Pool, cpu_count

from .constants import (
    WORK_DIR,
    ZIP_SUFFIX,
    ZIP_COUNT,
    FILES_PER_ARCHIVE,
    XML_SUFFIX,
)
from .file_structure import XMLFileStructure
from .xml_tasks import generate_xml, parse_xml
import logging


logger = logging.getLogger()


def generate_archives():
    _cleanup()
    for _ in range(ZIP_COUNT):
        _create_archive()


def parse_archives() -> List[XMLFileStructure]:
    with Pool(processes=cpu_count()) as pool:
        procs_res = [
            pool.apply_async(
                _parse_archive,
                (os.path.join(WORK_DIR, file_name),)
            )
            for file_name in os.listdir(WORK_DIR)
            if file_name.endswith(ZIP_SUFFIX)
        ]

        all_data = []
        for res in procs_res:
            all_data.extend(res.get())

    return all_data


def _cleanup():
    for filename in filter(
        lambda x: x.endswith('.zip'),
        os.listdir(WORK_DIR)
    ):
        os.unlink(os.path.join(WORK_DIR, filename))


def _parse_archive(file_path: str):
    logger.info(f'process_id={os.getpid()}')
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

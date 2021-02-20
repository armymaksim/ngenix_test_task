import csv
import datetime
import os
from typing import Dict, Any, Iterable
from .constants import CSV_SUFFIX, ID, LEVEL, OBJECT_NAME, WORK_DIR
from .file_structure import XMLFileStructure
import logging


logger = logging.getLogger()


def create_report1(data: Iterable[XMLFileStructure]) -> str:
    fields = [ID, LEVEL]
    data_generator = (
        {
            ID: xmlfile.tag_id,
            LEVEL: xmlfile.tag_level,
        }
        for xmlfile in data
    )
    report_name = f'report_1_{datetime.datetime.now().isoformat()}{CSV_SUFFIX}'

    return _write_report(data_generator, fields, report_name)


def create_report2(data: Iterable[XMLFileStructure]) -> str:
    fields = [ID, OBJECT_NAME]
    data_generator = (
        {
            ID: xmlfile.tag_id,
            OBJECT_NAME: object_name,
        }
        for xmlfile in data
        for object_name in xmlfile.object_names
    )
    report_name = f'report_2_{datetime.datetime.now().isoformat()}{CSV_SUFFIX}'

    return _write_report(data_generator, fields, report_name)


def _write_report(
    data: Iterable[Dict[str, Any]],
    fields: Iterable[str],
    report_name: str
) -> str:
    report_path = os.path.join(WORK_DIR, report_name)

    if os.path.exists(report_path):
        logger.warning(f'{report_path} already exists, recreating!')
        os.unlink(report_path)

    with open(report_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

    return report_path

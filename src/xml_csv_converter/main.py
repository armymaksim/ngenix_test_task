from .csv_tasks import create_report1, create_report2
from .archive_tasks import generate_archives, parse_archives
import logging


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger()


def create_reports() -> None:
    data = parse_archives()
    report_name1 = create_report1(data)
    logger.info(f'{report_name1} created')
    report_name2 = create_report2(data)
    logger.info(f'{report_name2} created')


def run() -> None:
    generate_archives()
    create_reports()

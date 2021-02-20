import os
import freezegun as freezegun
import pytest
from xml_csv_converter import constants, generate_archives, create_reports


@pytest.fixture()
def cleanup():
    for filename in filter(
        lambda x: x.endswith('.zip'),
        os.listdir(constants.WORK_DIR)
    ):
        os.unlink(os.path.join(constants.WORK_DIR, filename))


def test_generate_xml(cleanup):
    generate_archives()
    assert len(
        list(
            filter(
                lambda x: x.endswith('.zip'),
                os.listdir(constants.WORK_DIR)
            )
        )
    ) == 50


@freezegun.freeze_time('2021-02-15')
def test_create_report(cleanup):
    generate_archives()
    create_reports()
    assert len(
        list(
            filter(
                lambda x: x.endswith('.csv'),
                os.listdir(constants.WORK_DIR)
            )
        )
    ) == 2
    assert os.path.exists(
        '/tmp/report_1_2021-02-15T00:00:00.csv'
    )
    assert os.path.exists(
        '/tmp/report_2_2021-02-15T00:00:00.csv'
    )
    with open(
        '/tmp/report_1_2021-02-15T00:00:00.csv', 'r'
    ) as f:
        len(f.readlines(5002))

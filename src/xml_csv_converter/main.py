from .csv_tasks import create_report1, create_report2
from .archive_tasks import generate_archives, parse_archives

def create_reports():
    data = parse_archives()
    report_name1 = create_report1(data)
    print(f'{report_name1} created')
    report_name2 = create_report2(data)
    print(f'{report_name2} created')


if __name__ == '__main__':
    generate_archives()
    create_reports()


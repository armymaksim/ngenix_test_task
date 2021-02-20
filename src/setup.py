from setuptools import setup, find_packages

setup(
    name='xml_csv_converter',
    version='0.0.1',
    include_package_data=True,
    packages=find_packages(),
    url='',
    license='None',
    author='mkozlov',
    author_email='army.maksim@gmail.com',
    description='ngninx_test_task',
    entry_points={
        'console_scripts':
            [
                'generate_xml = xml_csv_converter.main:generate_archives',
                'convert_xml = xml_csv_converter.main:create_reports',
                'all_in_one = xml_csv_converter.main:run'
            ]
        }
)

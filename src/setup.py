from setuptools import setup, find_packages

setup(
    name='xml_csv_converter',
    version='0.0.1',
    include_package_data=True,
    install_requires=[
        'pytest==4',
        'freezegun>=1.1.0'
    ],
    packages=find_packages(),
    license='None',
    author='mkozlov',
    author_email='army.maksim@gmail.com',
    description='ngninx_test_task',
    entry_points={
        'console_scripts':
            [
                'generate_xml = xml_csv_converter.main:generate_archives',
                'create_reports = xml_csv_converter.main:create_reports',
                'all_in_one = xml_csv_converter.main:run'
            ]
        }
)

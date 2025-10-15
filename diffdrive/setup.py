from setuptools import find_packages, setup

package_name = 'diffdrive'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lantos',
    maintainer_email='lantos@todo.todo',
    description='Egyszerű diffdrive vezérlő node (cmd_vel publikálás)',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'diffdrive_control = diffdrive.diffdrive_control:main'
        ],
    },
)

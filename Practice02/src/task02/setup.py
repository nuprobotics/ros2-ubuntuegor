from setuptools import find_packages, setup

package_name = 'task02'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml', 'launch/task02.launch', 'config/task02.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bnt',
    maintainer_email='me@bnt.to',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sender = task02.sender:main'
        ],
    },
)

from setuptools import find_packages, setup

package_name = 'delivery_core'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nguyen',
    maintainer_email='vonhatnguyen777@gmail.com',
    description='Delivery Robot Package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'delivery_logic = delivery_core.delivery_logic:main',
        ],
    },
)

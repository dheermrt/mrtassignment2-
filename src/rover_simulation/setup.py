from setuptools import find_packages, setup

package_name = 'rover_simulation'

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
    maintainer='dhher',
    maintainer_email='dhher@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['obstacle_avoidance_node = rover_simulation.obstacle_avoidance_node:main','rover_navigation_node=rover_simulation.rover_navigation_node:main',
        ],
    },
)

from setuptools import find_packages, setup

package_name = 'rover_odometry'

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
    maintainer_email='dheer968793@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['velocity=rover_odometry.velocitypublisher:main',
                            'coordinate=rover_odometry.velocitysubscriber:main',
        ],
    },
)

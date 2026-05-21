from setuptools import setup, find_packages

package_name = 'ur10_motion'

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
    maintainer='user',
    maintainer_email='user@example.com',
    description='UR10 3-point motion',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ur10_3point = ur10_motion.ur10_3point_node:main',
        ],
    },
)

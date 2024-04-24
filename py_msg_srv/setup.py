from setuptools import setup

package_name = 'py_msg_srv'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sajin',
    maintainer_email='sajinsathananthan@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "prsn_status_publisher = py_msg_srv.prsn_status_publisher:main",
            "calculate_area = py_msg_srv.rectangle_area_srv:main"
        ],
    },
)

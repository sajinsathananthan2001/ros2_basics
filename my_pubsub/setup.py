from setuptools import setup

package_name = 'my_pubsub'

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
            "hlo_wld_node = my_pubsub.hello_world:main",
            "draw_circle_node = my_pubsub.publisher:main",
            "pose_subscriber = my_pubsub.subscriber:main"

        ],
    },
)

from setuptools import find_packages, setup

package_name = 'arduinobot_py_examples'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['tests']),  # Assuming 'tests' is the directory to exclude
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mariselvam',
    maintainer_email='your-email@example.com',  # Replace with actual email
    description='A package with examples for ArduinoBot integration',
    license='MIT',  # Replace with your actual license
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'simple_publisher = arduinobot_py_examples.simple_publisher:main',
        'simple_subscriber = arduinobot_py_examples.simple_subscriber:main',
        'simple_parameter = arduinobot_py_examples.simple_parameter:main',
    ],
}

)

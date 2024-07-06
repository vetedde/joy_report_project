from setuptools import setup, find_packages

setup(
    version='1.0.0',
    description='A description of your project',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/yourusername/joy_report_project',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add any dependencies your project requires here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
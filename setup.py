from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='django-db-seed-kit',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=5.0.0',
    ],
    setup_requires=['wheel'],
    python_requires='>=3.10',
    license='MIT',
    description='A Django app to create seed data for your models.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cristhian-cervantes-mediaaerea/django-db-seed-kit',
    author='cristiancer',
    author_email='cristianbcer27@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 5.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ],
    keywords=['Django', 'models', 'seed', 'data', 'fixtures']
)

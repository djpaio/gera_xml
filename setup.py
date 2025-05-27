from setuptools import setup, find_packages

setup(
    name='gerar-xml-dda',
    version='1.0.0',
    description='Gerador de XML a partir de XSD via interface gráfica (tkinter)',
    author='Deivid Jhonatan Paio',
    author_email='deividjpaio@gmail.com',
    packages=find_packages(where='gerar_xml_dda'),
    package_dir={'': 'gerar_xml_dda'},
    include_package_data=True,
    install_requires=[
        'tk'
    ],
    entry_points={
        'console_scripts': [
            'gerar-xml-dda=app:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
    ],
    python_requires='>=3.8',
)

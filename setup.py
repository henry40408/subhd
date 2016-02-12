from setuptools import setup

setup(
    name="subhd",
    version="1.0.2",
    description="Yet another SubHD.com download client",
    author="Heng-Yi Wu",
    author_email="henry40408@gmail.com",
    url="https://github.com/henry40408/subhd",
    install_requires=[
        "beautifulsoup4==4.4.1",
        "inflect==0.2.5",
        "OpenCC==0.2",
        "rarfile==2.7",
        "requests==2.9.1",
        "tabulate==0.7.5"
    ],
    scripts=[
        "bin/subhd"
    ]
)

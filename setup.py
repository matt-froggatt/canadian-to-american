from setuptools import setup

setup(
        name="catoam",
        version="1.0",
        py_modules=["catoam"],
        install_requires=[
            "click",
        ],
        entry_points='''
            [console_scripts]
            catoam=catoam:translate
        ''',
)

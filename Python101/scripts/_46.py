from cx_Freeze import setup, Executalbe

setup(name='distme',
    version='0.1',
    description='Parse stuff',
    executalbe = [Excutable('_39.py')]
)


# use cx_Freeze to build executable package without setup environment

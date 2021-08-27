from setuptools import find_packages, setup

setup(
    name='mcts_kds',
    packages=find_packages(include=['mcts','nim','players','utils']),
    description='MCTS Library',
    version = 1.0,
    download_url = "https://github.com/madisonmussari/mcts_kds/archive/refs/tags/v1.tar.gz",
    author='Madison Mussari, supervised by Pedro Rangel',
    tests_require=['pytest==4.4.1'],
    test_suite='test',
)

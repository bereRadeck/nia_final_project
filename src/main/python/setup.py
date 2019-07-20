from setuptools import find_packages, setup

setup(
    name='${project.artifactId}',
    version='${project.version.asPython}',
    description='cliplister-data-generator',
    author='Mats Richter, Berenike Radeck',
    author_email='mrichter@agile-im.de',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "aim-pioc==0.0.5",
        "Cython==0.29.3",
        "pybind11==2.2.4",
        "scipy==1.2.0",
        "scikit-learn==0.20",
        "Pillow",
        "scikit-image",
        "numpy==1.16.0",
        "pandas==0.22.0",
        "opencv-python",
        "matplotlib==3.0.2",
        "pylint",
        "jupyter==1.0.0",
        "pytest-cov==2.6.1",
        "pytest-pythonpath==0.7.3",
        "hypothesis",
        "shap",
        "jupyterlab",
        "xgboost",
        "sympy",
        "seaborn"
        ],
        #scripts=['scripts/clean_data.py', 'scripts/create_dataset.py', 'get_test_data.py']
)

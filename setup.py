from setuptools import find_packages, setup

setup(
    name="m4i-data-management",
    version="1.0.0",
    author="Aurelius Enterprise",
    packages=find_packages(),
    python_requires="~=3.7",
    install_requires=[
        "avro",
        "confluent_kafka",
        "dict_hash",
        "elasticsearch",
        "fastavro",
        "pandas",
        "pytest",
        "requests",
        "typing_extensions",
        "m4i_atlas_core"
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov"
        ]
    }
)

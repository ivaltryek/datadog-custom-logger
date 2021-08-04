import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# setup(name="datadog-logger",
#       version="0.1.0",
#       description="Python logging handler for DataDog Logs",
#       url="https://github.com/meet86/datadog-custom-logger",
#       packages=["datadog_custom_logger"],
#       install_requires=["datadog-api-client"])

setuptools.setup(
    name="datadog-custom-logger",
    version="1.1.0",
    author="Meet Vasani",
    author_email="meet.vasani86@gmail.com",
    description="Logger Tool for Datadog logs monitoring",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/meet86/datadog-custom-logger",
    packages=setuptools.find_packages(),
    zip_safe=True,
    install_requires=["datadog-api-client"],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)

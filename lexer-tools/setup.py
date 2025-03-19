from setuptools import setup, find_packages

setup(
    name="lexer-tools",  # Package name
    version="1.1.1",  # Version number
    description="Lexer Tools is a student-friendly resource designed to simplify ML & NLP concepts",
    author="SeventyThree",
    author_email="73@gmail.com",
    packages=find_packages(),  # Automatically find packages
    include_package_data=True,  # Include non-Python files
    package_data={
        "lexer_tools": ["data/*.txt"],  # Include all .txt files in the data folder
    },
    install_requires=[],  # Add dependencies if needed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Python version requirement
)
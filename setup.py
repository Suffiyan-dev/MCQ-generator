from setuptools import setup, find_packages
setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Suffiyan",
    author_email="suffiyanusman123@gmail.com",
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages(),
)
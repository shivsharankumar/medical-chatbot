from setuptools import setup, find_packages
setup(
    name='medical-chatbot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'langchain',
        'flask',
        'sentence-transformers',
        'pypdf',
        'python-dotenv',
        'langchain-pinecone',
        'langchain-openai',
        'langchain-community'
    ],
    description='A medical chatbot that provides information and assistance to users.',
    author='Shiv Sharan Kumar', 
    author_email='shivsharan47@gmail.com'
)     
from setuptools import setup, find_packages

setup(
    name="ProjetoAplicado1",  # Nome do projeto
    version="0.1.0",  # Versão do projeto
    description="Análise de produtos best-sellers da Amazon",  # Descrição do projeto
    author="Andria Silva",  # Nome do autor
    author_email="10441204@mackenzista.com.br",  # Email do autor
    url="https://github.com/andriasilvac/ProjetoAplicado1",  # URL do repositório GitHub
    packages=find_packages(where="src"),  # Encontre pacotes dentro do diretório "src"
    package_dir={"": "src"},  # Mapeie o diretório "src" para o projeto
    install_requires=[  # Dependências necessárias
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "scikit-learn>=0.24.0",
    ],
    include_package_data=True,  # Incluir outros arquivos descritos no MANIFEST.in
    python_requires=">=3.7",  # Versão mínima do Python
)

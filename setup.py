from setuptools import setup, find_packages

# Carregar conteúdo do README.md
with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

# Carregar requisitos do requirements.txt
with open("requirements.txt") as requirements_file:
    requirements = [line.strip() for line in requirements_file.readlines() if line.strip() and not line.startswith("#")]

setup(
    name="cursos-api",
    version="0.1",
    description="API de cursos",
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(),  # Isso ainda incluirá pacotes se você quiser
    include_package_data=True,
    package_data={
        "": [  # Use "" para incluir arquivos de qualquer diretório
            "api/v1/endpoints/*.py",  # Inclui todos os arquivos .py dentro de endpoints
            "core/*.py",              # Inclui todos os arquivos .py dentro de core
            "models/*.py",            # Inclui todos os arquivos .py dentro de models
            "schemas/*.py",           # Inclui todos os arquivos .py dentro de schemas
            "services/crud.py",       # Inclui o arquivo crud.py da pasta services
            "gui/*.py",               # Inclui todos os arquivos .py dentro de gui
            "criar_tabelas.py",       # Inclui criar_tabelas.py
            "main.py",                # Inclui main.py
        ]
    },
    install_requires=requirements,
)

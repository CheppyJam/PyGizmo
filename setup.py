from setuptools import setup, find_packages

setup(
    name="PyGizmo",  # Название вашего пакета
    version="0.0.1",  # Версия
    author="SherryJam",
    author_email="chep@spworlds.ru",
    description="Gizmo API wrapper for Python",
    packages=find_packages(),  # Автоматический поиск модулей
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        'requests'
    ],
)

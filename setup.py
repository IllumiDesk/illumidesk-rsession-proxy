import setuptools

setuptools.setup(
    name="illumidesk-rsession-proxy",
    version='0.1.0',
    url="https://github.com/illumidesk/illumidesk-rsession-proxy",
    author="IllumiDesk Team",
    description="hello@illumidesk.com",
    packages=setuptools.find_packages(),
	keywords=['Jupyter','IllumiDesk','RStudio','Shiny Server','JupyterHub'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'illumidesk-rsession-proxy = illumidesk-rsession-proxy:setup_illumidesk-rsession-proxy',
        ]
    },
    package_data={
        'illumidesk-rsession-proxy': ['icons/*'],
    },
)

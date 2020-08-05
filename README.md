# IllumiDesk RStudio and Shiny Server Proxy for Jupyter

[RStudio and Shiny Server](https://www.rstudio.org/) are the leading development and visualization solutions for the `R` language. The `illumidesk-rsession-proxy` package allows users to launch RStudio and/or Shiny Servers from their Jupyter Notebook / Jupyter Lab environments.

This package was built using the [`jupyter-server-proxy` cookiecutter template](https://github.com/jupyterhub/jupyter-server-proxy/tree/master/contrib/template).

## Installation

```bash
pip install illumidesk-rsession-proxy
```

## Requirements

### R and IRkernel

Refer to [R's official documentation](https://www.r-project.org/) to install `R`. You will also need the [IRkernel installed](https://irkernel.github.io/installation/).

### RStudio Server and Shiny Server

`RStudio` is a desktop application and `RStudio Server` surfaces `RStudio` and the `Shiny` web applications to a web broswer. This package requires the installation of `rstudio-server`. Refer to [RStudio's official documentation](https://support.rstudio.com/hc/en-us/articles/360009981893-Getting-Started-Installation) to install `rstudio-server` in your environment. Another option is to use `conda` with the `conda-forge` channel to install the required dependencies. The
`illumidesk/r-conda` repo has an example [`environment.yml`](https://github.com/IllumiDesk/r-conda/blob/main/environment.yml) that you can use as a reference.

### Install Jupyter Notebook

This extension relies on the Jupyter Notebook to run. [Refer to Jupyter's official documentaion](https://jupyter.org/install) for installation instructions.

### Install illumidesk-rsession-proxy

Install the package with pip:

```
pip install illumidesk-rsession-proxy
```

## Why?

So we can open RStudio in a new browser tab from the Jupyter Lab launcher. Refer to [`jupyter-server-proxy`'s](https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html#specifying-config-from-python-packages) documentation for additional configuration settings.

## Attributions

- [`jupyter-rsession-proxy`](https://github.com/jupyterhub/jupyter-rsession-proxy)
- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)

## License

BSD 3-Clause

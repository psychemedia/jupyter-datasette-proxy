# jupyter-datasette-proxy

Using [datasette](https://datasette.io/) in JupyterHub or Binder with
[jupyter-server-proxy](https://github.com/jupyterhub/jupyter-server-proxy)

Launch into notebook interface (run `datasette` from the notebook `New` menu): [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-datasette-demo/master)

Launch directly into datasette: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-datasette-demo/master?urlpath=datasette)

The `datasette` port is assigned dynamically, although a known port could be specified if datasette is used to provide an API.

## Installation

You can install from PyPI:

```bash
pip install jupyter-datasette-proxy
```

This will also bring in datasette.
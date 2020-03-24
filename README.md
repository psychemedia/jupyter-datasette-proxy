# jupyterserverproxy-datasette-demo

Using datasette with Jupyter Server Proxy.

This fork is an experiment to see if https://github.com/simonw/datasette/issues/394 solves the various asset problems.

Launch into notebook interface (run `datasette` from the notebook `New` menu): [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/simonw/jupyterserverproxy-datasette-demo/master)

Launch directly into datasette: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/simonw/jupyterserverproxy-datasette-demo/master?urlpath=datasette)

The `datasette` port is assigned dynamically, although a known port could be specified if datasette is used to provide an API. (But in a notebook context that probably doesn't make sense? You could just as easilu call directly on the SQLite3 db.)



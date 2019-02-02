# jupyterserverproxy-datasette-demo
Using datasette with Jupyter Server Proxy.

I'm not sure *why* you'd want to do this, but you can... or should be able to once I figure out how to resolve the static files properly...

Launch into notebook interface (run `datasette` from the notebook `New` menu): [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-datasette-demo/master)


Launch directly into datasette: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/jupyterserverproxy-datasette-demo/master?urlpath=datasette)

The `datasette` port is assigned dynamically, although a known port could be specified if datasette is used to provide an API. (But in a notebook context that probably doesn't make sense? You could just as easilu call directly on the SQLite3 db.)



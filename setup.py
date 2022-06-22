import setuptools

with open("README.md", encoding="utf8") as f:
    readme = f.read()

setuptools.setup(
  name="jupyter-datasette-proxy",
  version="1.0",
  # py_modules rather than packages, since we only have 1 file
  py_modules=['nbdatasette'],
  install_requires=[
    'datasette',
    'jupyter-server-proxy'
  ],
  description="Run datasette on JupyterHub with jupyter-server-proxy",
  long_description=readme,
  long_description_content_type="text/markdown",
  entry_points={
      'jupyter_serverproxy_servers': [
          #path = module:entry_function
          'datasette = jupyter_datasette_proxy:setup_datasette',
      ]
  },
)

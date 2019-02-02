import os

def setup_datasette():
  dbpath = os.path.join(os.environ['HOME'], 'dakar_sql.sqlite')
  return {
    #datasette does look like it supports static references, but I'm missing something somewhere?
    # https://github.com/simonw/datasette/issues/160
    #If we set static refererncing, do we also need ;absolute_url': False ?
    #I may (also) be misunderstanding {base_url}
    #'command': ['datasette', 'serve', '-p', '{port}', '--static', 'static:{base_url}', dbpath],
    'command': ['datasette', 'serve', '-p', '{port}', dbpath],
    'absolute_url': True,
    #The following needs a the labextension installing.
    #eg in postBuild: jupyter labextension install jupyterlab-server-proxy
    'launcher_entry': {
        'enabled': True,
        #'icon_path': '/home/jovyan/.jupyter/datasette.svg',
        'title': 'Datasette',
    },
  }

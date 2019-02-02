import os

def setup_datasette():
  dbpath = os.path.join(os.environ['HOME'], 'dakar_sql.sqlite')
  return {
    #datasette does look like it supports static references, but I'm missing something somewhere?
    # https://github.com/simonw/datasette/issues/160
    #If we set static refererncing, do we also need ;absolute_url': False ?
    #I may (also) be misunderstanding {base_url}. Is that the domain, the domain+path, or the path?
    #If it's the path, then can it be used to set the static element (once I figure out what args --static takes)
    #I am so in the land of so-tired I have no idea what anything does.
    #'command': ['datasette', 'serve', '-p', '{port}', '--static', 'static:{base_url}', dbpath],
    'command': ['datasette', 'serve', '-p', '{port}', dbpath],
    #With absolute_url True we get infinite redirects?
    'absolute_url': False,
    #The following needs a the labextension installing.
    #eg in postBuild: jupyter labextension install jupyterlab-server-proxy
    'launcher_entry': {
        'enabled': True,
        #'icon_path': '/home/jovyan/.jupyter/datasette.svg',
        'title': 'Datasette',
    },
  }

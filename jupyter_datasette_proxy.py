import os


def setup_datasette():
    return {
        "command": [
            "datasette",
            "serve",
            "-p",
            "{port}",
            "--setting",
            "base_url:{base_url}datasette/",
        ],
        "absolute_url": True,
        # The following needs a the labextension installing.
        # eg in postBuild: jupyter labextension install jupyterlab-server-proxy
        "launcher_entry": {
            "enabled": True,
            #'icon_path': '/home/jovyan/.jupyter/datasette.svg',
            "title": "Datasette",
        },
    }

# {{cookiecutter.project_name}}

[! https://img.shields.io/github/license/{{cookiecutter.author_github_username}}/{{cookiecutter.repo_name}}] [! https://img.shields.io/badge/Made%20at-Starschema-red]
{{cookiecutter.description}}


## Running locally

To run a development instance locally, simply use the following command in the terminal under the project directory:

```ssh
make start-env ENV=dev
```

There are three options for the ENV variable: `prd`, `dev` and `lab`.  The `prd` instance will expose the app to port 80 while `dev` instance will expose it to port 8050. 
The `lab` instance only spins up a jupyter lab for development purposes.


BRiders
=======


Rest API
--------

A API possui os seguintes recursos:

  * Criar classificação (aka categoria);
  * Submissão de avaliação de corrida;
  * Login com JWT


Arquitetura do projeto
----------------------

O projeto usa principalmente FastAPI e seu ecossistema, por este motivo usei a arquitetura proposta para
projetos de produção encontrado no Cookiecutter_FastAPI_PostgreSQL_ .

.. _Cookiecutter_FastAPI_PostgreSQL: https://github.com/tiangolo/full-stack-fastapi-postgresql


Desenvolvimento
---------------

Projeto foi desenvolvido principalmente com:

  * poetry: Gerenciamento de dependências e empacotamento.
  * fastapi: Rest API.
  * typer: Kit para CLI.
  * pytest: Testes.


Quickstart
----------

  $ poetry install

  $ poetry run alembic upgrade head

  $ poetry run b_riders users create --is-superuser teste@teste.com 123qweasd

  $ poetry run uvicorn b_riders.api:app --reload

Antes de fazer criação de classificação e submisão de corridas, é preciso fazer o login.

.. image:: https://gist.githubusercontent.com/danielmartins/51252360eaec89fa366940129f635195/raw/58656d080ee3dcda219b6daa24f3893094640faa/b_riders_quickstart.gif


Documentação
------------

A API disponibiliza uma documentação por OpenApi Specification no endereço:

http://localhost:8000/docs

Nela você encontra informações de como criar e acompanhar a execução dos jobs.



Testes
------

  $ poetry run pytest


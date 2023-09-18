# Pet Kare
Projeto backend de uma plataforma de musica.

O desafio é:

*"Você é consultor em uma empresa especializada em sistemas para petshops. Uma franquia chamada PetKare trabalha com processos manuais, possui papéis espalhados por toda a recepção, além de ter informações desorganizadas sobre os bichinhos de seus clientes. Dessa forma, o petshop solicitou sua ajuda para implantar uma API que permitisse ao PetKare ter um maior controle e organização dos dados dos animais de sua gama de clientes."*

## Stack utilizada

Para o estudo foram escolhidas as tecnologias:

**Back-end:** Python, Django, PostgreSQLite3.

**Testes:** Pytest.

**Ambiente:** Venv.
## Rodando localmente

Clone o projeto

```bash
  git clone git@github.com:agnes-lica/Bandkamp-Python.git
```

Entre no diretório do projeto

```bash
  cd PetKare
```

Inicie o servidor

```bash
# linux:
  source venv/bin/activate

# windows:
  .\venv\Scripts\activate 
```

Instale as dependências

```bash
  pip install -r requirements. txt
```

## Rodando os testes

#### Rodar todos os testes
```bash
 pytest --testdox -vvs
```

#### Rodar testes por tarefas
##### Tarefa 1
```bash
 pytest --testdox -vvs tests/tarefas/tarefa_1/
```

##### Tarefa 3
```bash 
 pytest --testdox -vvs tests/tarefas/tarefa_3/
```

##### Tarefa 4
```bash 
 pytest --testdox -vvs tests/tarefas/tarefa_4/
```

#### Rodar testes isolados
```bash 
 pytest --testdox -vvs caminho/para/o/arquivo/de/teste::NomeDaClasse::nome_do_metodo_de_teste
```

Exemplo:

```bash 
 pytest --testdox -vvs tests/tarefas/tarefa_3/test_views.py::PetViewsTest::test_can_list_pets_with_pagination
```
## Documentação da API

#### Endpoints

| Método   | Endpoint       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `POST`      | `api/pets/` | Cadastrar pet |
| `GET`      | `api/pets/` | Listar pet |
| `GET`      | `api/pets/?trait=nome_da_trait` | Filtragem de pets que possuem a trait passada por query param |
| `GET`      | `api/pets/<pet_id>/` | Busca de pet |
| `PATCH`      | `api/pets/<pet_id>/` | Atualização de pet |
| `DELETE`      | `api/pets/<pet_id>/` | Deleção de pet |


## Contato

Para entrar em contato comigo me mande um e-mail ou uma mensagem nas redes sociais:

- [github](https://www.github.com/agnes-lica)
- [LinkedIn](https://www.linkedin.com/in/agnesmr/)
- E-mail: agnes.lica@gmail.com

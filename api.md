# MetMuseum

Methods:

- <code title="get /search">client.<a href="./src/met_museum/_client.py">search</a>(\*\*<a href="src/met_museum/types/client_search_params.py">params</a>) -> <a href="./src/met_museum/types/works.py">Works</a></code>

# Collections

Types:

```python
from met_museum.types import Work, Works
```

Methods:

- <code title="get /objects/{objectId}">client.collections.<a href="./src/met_museum/resources/collections.py">retrieve</a>(object_id) -> <a href="./src/met_museum/types/work.py">Work</a></code>
- <code title="get /objects">client.collections.<a href="./src/met_museum/resources/collections.py">list</a>(\*\*<a href="src/met_museum/types/collection_list_params.py">params</a>) -> <a href="./src/met_museum/types/works.py">Works</a></code>
- <code title="get /search">client.collections.<a href="./src/met_museum/resources/collections.py">search</a>(\*\*<a href="src/met_museum/types/collection_search_params.py">params</a>) -> <a href="./src/met_museum/types/works.py">Works</a></code>

# Departments

Types:

```python
from met_museum.types import Departments
```

Methods:

- <code title="get /departments">client.departments.<a href="./src/met_museum/resources/departments.py">list</a>() -> <a href="./src/met_museum/types/departments.py">Departments</a></code>

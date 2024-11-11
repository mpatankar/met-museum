# MetMuseum

Methods:

- <code title="get /search">client.<a href="./src/met_museum/_client.py">search</a>(\*\*<a href="src/met_museum/types/client_search_params.py">params</a>) -> <a href="./src/met_museum/types/objects.py">Objects</a></code>

# Objects

Types:

```python
from met_museum.types import Object, Objects
```

Methods:

- <code title="get /objects/{objectId}">client.objects.<a href="./src/met_museum/resources/objects.py">retrieve</a>(object_id) -> <a href="./src/met_museum/types/object.py">Object</a></code>
- <code title="get /objects">client.objects.<a href="./src/met_museum/resources/objects.py">list</a>(\*\*<a href="src/met_museum/types/object_list_params.py">params</a>) -> <a href="./src/met_museum/types/objects.py">Objects</a></code>

# Departments

Types:

```python
from met_museum.types import Departments
```

Methods:

- <code title="get /departments">client.departments.<a href="./src/met_museum/resources/departments.py">list</a>() -> <a href="./src/met_museum/types/departments.py">Departments</a></code>

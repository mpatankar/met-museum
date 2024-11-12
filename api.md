# MetMuseum

Methods:

- <code title="get /search">client.<a href="./src/met_museum/_client.py">search</a>(\*\*<a href="src/met_museum/types/client_search_params.py">params</a>) -> <a href="./src/met_museum/types/art_objects.py">ArtObjects</a></code>

# MetObjects

Types:

```python
from met_museum.types import ArtObject, ArtObjects
```

Methods:

- <code title="get /objects/{objectId}">client.met_objects.<a href="./src/met_museum/resources/met_objects.py">retrieve</a>(object_id) -> <a href="./src/met_museum/types/art_object.py">ArtObject</a></code>
- <code title="get /objects">client.met_objects.<a href="./src/met_museum/resources/met_objects.py">list</a>(\*\*<a href="src/met_museum/types/met_object_list_params.py">params</a>) -> <a href="./src/met_museum/types/art_objects.py">ArtObjects</a></code>

# MetDepartments

Types:

```python
from met_museum.types import Departments
```

Methods:

- <code title="get /departments">client.met_departments.<a href="./src/met_museum/resources/met_departments.py">list</a>() -> <a href="./src/met_museum/types/departments.py">Departments</a></code>

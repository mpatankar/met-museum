# Collections

Types:

```python
from met_museum.types import Work, Works
```

Methods:

- <code title="get /objects/{objectId}">client.collections.<a href="./src/met_museum/resources/collections.py">retrieve</a>(object_id) -> <a href="./src/met_museum/types/work.py">Work</a></code>
- <code title="get /objects">client.collections.<a href="./src/met_museum/resources/collections.py">list</a>(\*\*<a href="src/met_museum/types/collection_list_params.py">params</a>) -> <a href="./src/met_museum/types/works.py">Works</a></code>
- <code title="get /search">client.collections.<a href="./src/met_museum/resources/collections.py">search_and_retrieve</a>(\*\*<a href="src/met_museum/types/collection_search_and_retrieve_params.py">params</a>) -> <a href="./src/met_museum/types/works.py">Works</a></code>

# ArtDepartments

Types:

```python
from met_museum.types import Departments
```

Methods:

- <code title="get /departments">client.art_departments.<a href="./src/met_museum/resources/art_departments.py">list</a>() -> <a href="./src/met_museum/types/departments.py">Departments</a></code>

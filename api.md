# Collections

Types:

```python
from met_museum.types import Work, Works, CollectionFastAPIResponse
```

Methods:

- <code title="get /objects">client.collections.<a href="./src/met_museum/resources/collections.py">list</a>(\*\*<a href="src/met_museum/types/collection_list_params.py">params</a>) -> <a href="./src/met_museum/types/works.py">Works</a></code>
- <code title="post /fastapi">client.collections.<a href="./src/met_museum/resources/collections.py">fast_api</a>(\*\*<a href="src/met_museum/types/collection_fast_api_params.py">params</a>) -> <a href="./src/met_museum/types/collection_fast_api_response.py">CollectionFastAPIResponse</a></code>
- <code title="get /search">client.collections.<a href="./src/met_museum/resources/collections.py">search</a>(\*\*<a href="src/met_museum/types/collection_search_params.py">params</a>) -> <a href="./src/met_museum/types/works.py">Works</a></code>

# ArtDepartments

Types:

```python
from met_museum.types import Departments
```

Methods:

- <code title="get /departments">client.art_departments.<a href="./src/met_museum/resources/art_departments.py">list</a>() -> <a href="./src/met_museum/types/departments.py">Departments</a></code>

from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `met_museum.resources` module.

    This is used so that we can lazily import `met_museum.resources` only when
    needed *and* so that users can just import `met_museum` and reference `met_museum.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("met_museum.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()

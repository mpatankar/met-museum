# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CollectionSearchParams"]


class CollectionSearchParams(TypedDict, total=False):
    q: Required[str]
    """
    Returns a listing of all Object IDs for objects that contain the search query
    within the object’s data
    """

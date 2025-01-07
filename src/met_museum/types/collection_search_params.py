# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CollectionSearchParams"]


class CollectionSearchParams(TypedDict, total=False):
    is_highlight: Required[Annotated[bool, PropertyInfo(alias="isHighlight")]]
    """Returns objects that match the query and are designated as highlights.

    Highlights are selected works of art from The Met Museum’s permanent collection
    representing different cultures and time periods.
    """

    q: Required[str]
    """
    Returns a listing of all Object IDs for objects that contain the search query
    within the object’s data
    """

    artist_or_culture: Annotated[bool, PropertyInfo(alias="artistOrCulture")]
    """
    Returns objects that match the query, specifically searching against the artist
    name or culture field for objects.
    """

    date_begin: Annotated[int, PropertyInfo(alias="dateBegin")]
    """
    Returns objects that match the query and fall between the dateBegin and dateEnd
    parameters. Examples include dateBegin=1700&dateEnd=1800
    """

    date_end: Annotated[int, PropertyInfo(alias="dateEnd")]
    """
    Returns objects that match the query and fall between the dateBegin and dateEnd
    parameters. Examples include dateBegin=1700&dateEnd=1800
    """

    department_id: Annotated[int, PropertyInfo(alias="departmentId")]
    """Returns objects that are a part of a specific department."""

    geo_location: Annotated[str, PropertyInfo(alias="geoLocation")]
    """Returns objects that match the query and the specified geographic location.

    Examples include "Europe", "France", "Paris", "China", "New York", etc.
    """

    has_images: Annotated[bool, PropertyInfo(alias="hasImages")]
    """Returns objects that match the query and have images."""

    is_on_view: Annotated[bool, PropertyInfo(alias="isOnView")]
    """Returns objects that match the query and are on view in the museum."""

    medium: str
    """
    Returns objects that match the query and are of the specified medium or object
    type. Examples include "Ceramics", "Furniture", "Paintings", "Sculpture",
    "Textiles", etc.
    """

    tags: bool
    """
    Returns objects that match the query, specifically searching against the subject
    keyword tags field for objects.
    """

    title: bool
    """
    Returns objects that match the query, specifically searching against the title
    field for objects.
    """

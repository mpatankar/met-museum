# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from typing import Iterable, Union

from .._utils import PropertyInfo

from datetime import date

from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["CollectionListParams"]

class CollectionListParams(TypedDict, total=False):
    department_ids: Annotated[Iterable[int], PropertyInfo(alias="departmentIds")]
    """integers that correspond to department IDs e.g.

    1 or 3|9|12, delimited with the | character
    """

    metadata_date: Annotated[Union[str, date], PropertyInfo(alias="metadataDate", format = "iso8601")]
    """Returns any objects with updated data after this date"""
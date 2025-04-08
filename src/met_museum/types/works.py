# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Works"]


class Works(BaseModel):
    object_ids: Optional[List[float]] = FieldInfo(alias="objectIDs", default=None)

    total: Optional[float] = None

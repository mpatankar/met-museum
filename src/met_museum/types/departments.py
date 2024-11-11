# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Departments", "Department"]


class Department(BaseModel):
    department_id: Optional[float] = FieldInfo(alias="departmentId", default=None)

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)


class Departments(BaseModel):
    departments: Optional[List[Department]] = None

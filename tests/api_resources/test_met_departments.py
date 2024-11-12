# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from met_museum import MetMuseum, AsyncMetMuseum
from tests.utils import assert_matches_type
from met_museum.types import Departments

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetDepartments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: MetMuseum) -> None:
        met_department = client.met_departments.list()
        assert_matches_type(Departments, met_department, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MetMuseum) -> None:
        response = client.met_departments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        met_department = response.parse()
        assert_matches_type(Departments, met_department, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MetMuseum) -> None:
        with client.met_departments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            met_department = response.parse()
            assert_matches_type(Departments, met_department, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetDepartments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMetMuseum) -> None:
        met_department = await async_client.met_departments.list()
        assert_matches_type(Departments, met_department, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetMuseum) -> None:
        response = await async_client.met_departments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        met_department = await response.parse()
        assert_matches_type(Departments, met_department, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetMuseum) -> None:
        async with async_client.met_departments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            met_department = await response.parse()
            assert_matches_type(Departments, met_department, path=["response"])

        assert cast(Any, response.is_closed) is True

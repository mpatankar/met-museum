# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from met_museum import MetMuseum, AsyncMetMuseum
from tests.utils import assert_matches_type
from met_museum.types import Object, Objects
from met_museum._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: MetMuseum) -> None:
        object_ = client.objects.retrieve(
            0,
        )
        assert_matches_type(Object, object_, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MetMuseum) -> None:
        response = client.objects.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(Object, object_, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MetMuseum) -> None:
        with client.objects.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(Object, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: MetMuseum) -> None:
        object_ = client.objects.list()
        assert_matches_type(Objects, object_, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: MetMuseum) -> None:
        object_ = client.objects.list(
            department_ids=[0, 0, 0],
            metadata_date=parse_date("2019-12-27"),
        )
        assert_matches_type(Objects, object_, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MetMuseum) -> None:
        response = client.objects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(Objects, object_, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MetMuseum) -> None:
        with client.objects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(Objects, object_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncObjects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMetMuseum) -> None:
        object_ = await async_client.objects.retrieve(
            0,
        )
        assert_matches_type(Object, object_, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMetMuseum) -> None:
        response = await async_client.objects.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(Object, object_, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMetMuseum) -> None:
        async with async_client.objects.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(Object, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMetMuseum) -> None:
        object_ = await async_client.objects.list()
        assert_matches_type(Objects, object_, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetMuseum) -> None:
        object_ = await async_client.objects.list(
            department_ids=[0, 0, 0],
            metadata_date=parse_date("2019-12-27"),
        )
        assert_matches_type(Objects, object_, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetMuseum) -> None:
        response = await async_client.objects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(Objects, object_, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetMuseum) -> None:
        async with async_client.objects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(Objects, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

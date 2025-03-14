# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from met_museum import MetMuseum, AsyncMetMuseum
from tests.utils import assert_matches_type
from met_museum.types import (
    Works,
    CollectionFastAPIResponse,
)
from met_museum._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: MetMuseum) -> None:
        collection = client.collections.list()
        assert_matches_type(Works, collection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: MetMuseum) -> None:
        collection = client.collections.list(
            department_ids=[0],
            metadata_date=parse_date("2019-12-27"),
        )
        assert_matches_type(Works, collection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MetMuseum) -> None:
        response = client.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Works, collection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MetMuseum) -> None:
        with client.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Works, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_fast_api(self, client: MetMuseum) -> None:
        collection = client.collections.fast_api(
            entry={},
        )
        assert_matches_type(CollectionFastAPIResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_fast_api(self, client: MetMuseum) -> None:
        response = client.collections.with_raw_response.fast_api(
            entry={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionFastAPIResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_fast_api(self, client: MetMuseum) -> None:
        with client.collections.with_streaming_response.fast_api(
            entry={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionFastAPIResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: MetMuseum) -> None:
        collection = client.collections.search(
            is_highlight=True,
            q="q",
        )
        assert_matches_type(Works, collection, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: MetMuseum) -> None:
        collection = client.collections.search(
            is_highlight=True,
            q="q",
            artist_or_culture=True,
            date_begin=0,
            date_end=0,
            department_id=0,
            geo_location="geoLocation",
            has_images=True,
            is_on_view=True,
            medium="medium",
            tags=True,
            title=True,
        )
        assert_matches_type(Works, collection, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: MetMuseum) -> None:
        response = client.collections.with_raw_response.search(
            is_highlight=True,
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Works, collection, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: MetMuseum) -> None:
        with client.collections.with_streaming_response.search(
            is_highlight=True,
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Works, collection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMetMuseum) -> None:
        collection = await async_client.collections.list()
        assert_matches_type(Works, collection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetMuseum) -> None:
        collection = await async_client.collections.list(
            department_ids=[0],
            metadata_date=parse_date("2019-12-27"),
        )
        assert_matches_type(Works, collection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetMuseum) -> None:
        response = await async_client.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Works, collection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetMuseum) -> None:
        async with async_client.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Works, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_fast_api(self, async_client: AsyncMetMuseum) -> None:
        collection = await async_client.collections.fast_api(
            entry={},
        )
        assert_matches_type(CollectionFastAPIResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_fast_api(self, async_client: AsyncMetMuseum) -> None:
        response = await async_client.collections.with_raw_response.fast_api(
            entry={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionFastAPIResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_fast_api(self, async_client: AsyncMetMuseum) -> None:
        async with async_client.collections.with_streaming_response.fast_api(
            entry={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionFastAPIResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncMetMuseum) -> None:
        collection = await async_client.collections.search(
            is_highlight=True,
            q="q",
        )
        assert_matches_type(Works, collection, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncMetMuseum) -> None:
        collection = await async_client.collections.search(
            is_highlight=True,
            q="q",
            artist_or_culture=True,
            date_begin=0,
            date_end=0,
            department_id=0,
            geo_location="geoLocation",
            has_images=True,
            is_on_view=True,
            medium="medium",
            tags=True,
            title=True,
        )
        assert_matches_type(Works, collection, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncMetMuseum) -> None:
        response = await async_client.collections.with_raw_response.search(
            is_highlight=True,
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Works, collection, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncMetMuseum) -> None:
        async with async_client.collections.with_streaming_response.search(
            is_highlight=True,
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Works, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from met_museum import MetMuseum, AsyncMetMuseum
from tests.utils import assert_matches_type
from met_museum.types import ArtObjects

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_search(self, client: MetMuseum) -> None:
        client_ = client.search(
            q="q",
        )
        assert_matches_type(ArtObjects, client_, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: MetMuseum) -> None:
        client_ = client.search(
            q="q",
            artist_or_culture=True,
            date_begin=0,
            date_end=0,
            department_id=0,
            geo_location="geoLocation",
            has_images=True,
            is_highlight=True,
            is_on_view=True,
            medium="medium",
            tags=True,
            title=True,
        )
        assert_matches_type(ArtObjects, client_, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: MetMuseum) -> None:
        response = client.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ArtObjects, client_, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: MetMuseum) -> None:
        with client.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ArtObjects, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_search(self, async_client: AsyncMetMuseum) -> None:
        client = await async_client.search(
            q="q",
        )
        assert_matches_type(ArtObjects, client, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncMetMuseum) -> None:
        client = await async_client.search(
            q="q",
            artist_or_culture=True,
            date_begin=0,
            date_end=0,
            department_id=0,
            geo_location="geoLocation",
            has_images=True,
            is_highlight=True,
            is_on_view=True,
            medium="medium",
            tags=True,
            title=True,
        )
        assert_matches_type(ArtObjects, client, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncMetMuseum) -> None:
        response = await async_client.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ArtObjects, client, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncMetMuseum) -> None:
        async with async_client.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ArtObjects, client, path=["response"])

        assert cast(Any, response.is_closed) is True

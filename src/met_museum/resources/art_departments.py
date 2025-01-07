# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.departments import Departments

__all__ = ["ArtDepartmentsResource", "AsyncArtDepartmentsResource"]


class ArtDepartmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArtDepartmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/met-museum-python#accessing-raw-response-data-eg-headers
        """
        return ArtDepartmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArtDepartmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/met-museum-python#with_streaming_response
        """
        return ArtDepartmentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Departments:
        """returns a listing of all departments"""
        return self._get(
            "/departments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Departments,
        )


class AsyncArtDepartmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArtDepartmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/met-museum-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArtDepartmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArtDepartmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/met-museum-python#with_streaming_response
        """
        return AsyncArtDepartmentsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Departments:
        """returns a listing of all departments"""
        return await self._get(
            "/departments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Departments,
        )


class ArtDepartmentsResourceWithRawResponse:
    def __init__(self, art_departments: ArtDepartmentsResource) -> None:
        self._art_departments = art_departments

        self.list = to_raw_response_wrapper(
            art_departments.list,
        )


class AsyncArtDepartmentsResourceWithRawResponse:
    def __init__(self, art_departments: AsyncArtDepartmentsResource) -> None:
        self._art_departments = art_departments

        self.list = async_to_raw_response_wrapper(
            art_departments.list,
        )


class ArtDepartmentsResourceWithStreamingResponse:
    def __init__(self, art_departments: ArtDepartmentsResource) -> None:
        self._art_departments = art_departments

        self.list = to_streamed_response_wrapper(
            art_departments.list,
        )


class AsyncArtDepartmentsResourceWithStreamingResponse:
    def __init__(self, art_departments: AsyncArtDepartmentsResource) -> None:
        self._art_departments = art_departments

        self.list = async_to_streamed_response_wrapper(
            art_departments.list,
        )

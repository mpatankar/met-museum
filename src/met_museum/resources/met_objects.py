# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date

import httpx

from ..types import met_object_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.art_object import ArtObject
from ..types.art_objects import ArtObjects

__all__ = ["MetObjectsResource", "AsyncMetObjectsResource"]


class MetObjectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/met-museum-python#accessing-raw-response-data-eg-headers
        """
        return MetObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/met-museum-python#with_streaming_response
        """
        return MetObjectsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        object_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArtObject:
        """
        returns a record for an object, containing all open access data about that
        object, including its image (if the image is available under Open Access)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/objects/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtObject,
        )

    def list(
        self,
        *,
        department_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        metadata_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArtObjects:
        """
        returns a listing of all valid Object IDs available to use

        Args:
          department_ids: integers that correspond to department IDs e.g. 1 or 3|9|12, delimited with the
              | character

          metadata_date: Returns any objects with updated data after this date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/objects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "department_ids": department_ids,
                        "metadata_date": metadata_date,
                    },
                    met_object_list_params.MetObjectListParams,
                ),
            ),
            cast_to=ArtObjects,
        )


class AsyncMetObjectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/met-museum-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/met-museum-python#with_streaming_response
        """
        return AsyncMetObjectsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        object_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArtObject:
        """
        returns a record for an object, containing all open access data about that
        object, including its image (if the image is available under Open Access)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/objects/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtObject,
        )

    async def list(
        self,
        *,
        department_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        metadata_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArtObjects:
        """
        returns a listing of all valid Object IDs available to use

        Args:
          department_ids: integers that correspond to department IDs e.g. 1 or 3|9|12, delimited with the
              | character

          metadata_date: Returns any objects with updated data after this date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/objects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "department_ids": department_ids,
                        "metadata_date": metadata_date,
                    },
                    met_object_list_params.MetObjectListParams,
                ),
            ),
            cast_to=ArtObjects,
        )


class MetObjectsResourceWithRawResponse:
    def __init__(self, met_objects: MetObjectsResource) -> None:
        self._met_objects = met_objects

        self.retrieve = to_raw_response_wrapper(
            met_objects.retrieve,
        )
        self.list = to_raw_response_wrapper(
            met_objects.list,
        )


class AsyncMetObjectsResourceWithRawResponse:
    def __init__(self, met_objects: AsyncMetObjectsResource) -> None:
        self._met_objects = met_objects

        self.retrieve = async_to_raw_response_wrapper(
            met_objects.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            met_objects.list,
        )


class MetObjectsResourceWithStreamingResponse:
    def __init__(self, met_objects: MetObjectsResource) -> None:
        self._met_objects = met_objects

        self.retrieve = to_streamed_response_wrapper(
            met_objects.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            met_objects.list,
        )


class AsyncMetObjectsResourceWithStreamingResponse:
    def __init__(self, met_objects: AsyncMetObjectsResource) -> None:
        self._met_objects = met_objects

        self.retrieve = async_to_streamed_response_wrapper(
            met_objects.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            met_objects.list,
        )

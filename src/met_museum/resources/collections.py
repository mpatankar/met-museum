# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date

import httpx

from ..types import collection_list_params, collection_search_params, collection_fast_api_params
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
from ..types.work import Work
from ..types.works import Works
from .._base_client import make_request_options
from ..types.collection_fast_api_response import CollectionFastAPIResponse

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/met-museum-python#accessing-raw-response-data-eg-headers
        """
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/met-museum-python#with_streaming_response
        """
        return CollectionsResourceWithStreamingResponse(self)

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
    ) -> Work:
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
            cast_to=Work,
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
    ) -> Works:
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
                    collection_list_params.CollectionListParams,
                ),
            ),
            cast_to=Works,
        )

    def fast_api(
        self,
        *,
        entry: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionFastAPIResponse:
        """
        Do Thing

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fastapi",
            body=maybe_transform({"entry": entry}, collection_fast_api_params.CollectionFastAPIParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionFastAPIResponse,
        )

    def search(
        self,
        *,
        is_highlight: bool,
        q: str,
        artist_or_culture: bool | NotGiven = NOT_GIVEN,
        date_begin: int | NotGiven = NOT_GIVEN,
        date_end: int | NotGiven = NOT_GIVEN,
        department_id: int | NotGiven = NOT_GIVEN,
        geo_location: str | NotGiven = NOT_GIVEN,
        has_images: bool | NotGiven = NOT_GIVEN,
        is_on_view: bool | NotGiven = NOT_GIVEN,
        medium: str | NotGiven = NOT_GIVEN,
        tags: bool | NotGiven = NOT_GIVEN,
        title: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Works:
        """
        returns a listing of all Object IDs for objects that contain the search query
        within the object’s data

        Args:
          is_highlight: Returns objects that match the query and are designated as highlights.
              Highlights are selected works of art from The Met Museum’s permanent collection
              representing different cultures and time periods.

          q: Returns a listing of all Object IDs for objects that contain the search query
              within the object’s data

          artist_or_culture: Returns objects that match the query, specifically searching against the artist
              name or culture field for objects.

          date_begin: Returns objects that match the query and fall between the dateBegin and dateEnd
              parameters. Examples include dateBegin=1700&dateEnd=1800

          date_end: Returns objects that match the query and fall between the dateBegin and dateEnd
              parameters. Examples include dateBegin=1700&dateEnd=1800

          department_id: Returns objects that are a part of a specific department.

          geo_location: Returns objects that match the query and the specified geographic location.
              Examples include "Europe", "France", "Paris", "China", "New York", etc.

          has_images: Returns objects that match the query and have images.

          is_on_view: Returns objects that match the query and are on view in the museum.

          medium: Returns objects that match the query and are of the specified medium or object
              type. Examples include "Ceramics", "Furniture", "Paintings", "Sculpture",
              "Textiles", etc.

          tags: Returns objects that match the query, specifically searching against the subject
              keyword tags field for objects.

          title: Returns objects that match the query, specifically searching against the title
              field for objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "is_highlight": is_highlight,
                        "q": q,
                        "artist_or_culture": artist_or_culture,
                        "date_begin": date_begin,
                        "date_end": date_end,
                        "department_id": department_id,
                        "geo_location": geo_location,
                        "has_images": has_images,
                        "is_on_view": is_on_view,
                        "medium": medium,
                        "tags": tags,
                        "title": title,
                    },
                    collection_search_params.CollectionSearchParams,
                ),
            ),
            cast_to=Works,
        )


class AsyncCollectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/met-museum-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/met-museum-python#with_streaming_response
        """
        return AsyncCollectionsResourceWithStreamingResponse(self)

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
    ) -> Work:
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
            cast_to=Work,
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
    ) -> Works:
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
                    collection_list_params.CollectionListParams,
                ),
            ),
            cast_to=Works,
        )

    async def fast_api(
        self,
        *,
        entry: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionFastAPIResponse:
        """
        Do Thing

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fastapi",
            body=await async_maybe_transform({"entry": entry}, collection_fast_api_params.CollectionFastAPIParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionFastAPIResponse,
        )

    async def search(
        self,
        *,
        is_highlight: bool,
        q: str,
        artist_or_culture: bool | NotGiven = NOT_GIVEN,
        date_begin: int | NotGiven = NOT_GIVEN,
        date_end: int | NotGiven = NOT_GIVEN,
        department_id: int | NotGiven = NOT_GIVEN,
        geo_location: str | NotGiven = NOT_GIVEN,
        has_images: bool | NotGiven = NOT_GIVEN,
        is_on_view: bool | NotGiven = NOT_GIVEN,
        medium: str | NotGiven = NOT_GIVEN,
        tags: bool | NotGiven = NOT_GIVEN,
        title: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Works:
        """
        returns a listing of all Object IDs for objects that contain the search query
        within the object’s data

        Args:
          is_highlight: Returns objects that match the query and are designated as highlights.
              Highlights are selected works of art from The Met Museum’s permanent collection
              representing different cultures and time periods.

          q: Returns a listing of all Object IDs for objects that contain the search query
              within the object’s data

          artist_or_culture: Returns objects that match the query, specifically searching against the artist
              name or culture field for objects.

          date_begin: Returns objects that match the query and fall between the dateBegin and dateEnd
              parameters. Examples include dateBegin=1700&dateEnd=1800

          date_end: Returns objects that match the query and fall between the dateBegin and dateEnd
              parameters. Examples include dateBegin=1700&dateEnd=1800

          department_id: Returns objects that are a part of a specific department.

          geo_location: Returns objects that match the query and the specified geographic location.
              Examples include "Europe", "France", "Paris", "China", "New York", etc.

          has_images: Returns objects that match the query and have images.

          is_on_view: Returns objects that match the query and are on view in the museum.

          medium: Returns objects that match the query and are of the specified medium or object
              type. Examples include "Ceramics", "Furniture", "Paintings", "Sculpture",
              "Textiles", etc.

          tags: Returns objects that match the query, specifically searching against the subject
              keyword tags field for objects.

          title: Returns objects that match the query, specifically searching against the title
              field for objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "is_highlight": is_highlight,
                        "q": q,
                        "artist_or_culture": artist_or_culture,
                        "date_begin": date_begin,
                        "date_end": date_end,
                        "department_id": department_id,
                        "geo_location": geo_location,
                        "has_images": has_images,
                        "is_on_view": is_on_view,
                        "medium": medium,
                        "tags": tags,
                        "title": title,
                    },
                    collection_search_params.CollectionSearchParams,
                ),
            ),
            cast_to=Works,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.retrieve = to_raw_response_wrapper(
            collections.retrieve,
        )
        self.list = to_raw_response_wrapper(
            collections.list,
        )
        self.fast_api = to_raw_response_wrapper(
            collections.fast_api,
        )
        self.search = to_raw_response_wrapper(
            collections.search,
        )


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.retrieve = async_to_raw_response_wrapper(
            collections.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            collections.list,
        )
        self.fast_api = async_to_raw_response_wrapper(
            collections.fast_api,
        )
        self.search = async_to_raw_response_wrapper(
            collections.search,
        )


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.retrieve = to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            collections.list,
        )
        self.fast_api = to_streamed_response_wrapper(
            collections.fast_api,
        )
        self.search = to_streamed_response_wrapper(
            collections.search,
        )


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.retrieve = async_to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            collections.list,
        )
        self.fast_api = async_to_streamed_response_wrapper(
            collections.fast_api,
        )
        self.search = async_to_streamed_response_wrapper(
            collections.search,
        )

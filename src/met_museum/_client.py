# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_search_params
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .resources import collections, departments
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from .types.works import Works
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "MetMuseum",
    "AsyncMetMuseum",
    "Client",
    "AsyncClient",
]


class MetMuseum(SyncAPIClient):
    collections: collections.CollectionsResource
    departments: departments.DepartmentsResource
    with_raw_response: MetMuseumWithRawResponse
    with_streaming_response: MetMuseumWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous met-museum client instance."""
        if base_url is None:
            base_url = os.environ.get("MET_MUSEUM_BASE_URL")
        if base_url is None:
            base_url = f"https://collectionapi.metmuseum.org/public/collection/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.collections = collections.CollectionsResource(self)
        self.departments = departments.DepartmentsResource(self)
        self.with_raw_response = MetMuseumWithRawResponse(self)
        self.with_streaming_response = MetMuseumWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def search(
        self,
        *,
        q: str,
        artist_or_culture: bool | NotGiven = NOT_GIVEN,
        date_begin: int | NotGiven = NOT_GIVEN,
        date_end: int | NotGiven = NOT_GIVEN,
        department_id: int | NotGiven = NOT_GIVEN,
        geo_location: str | NotGiven = NOT_GIVEN,
        has_images: bool | NotGiven = NOT_GIVEN,
        is_highlight: bool | NotGiven = NOT_GIVEN,
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

          is_highlight: Returns objects that match the query and are designated as highlights.
              Highlights are selected works of art from The Met Museum’s permanent collection
              representing different cultures and time periods.

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
        return self.get(
            "/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "artist_or_culture": artist_or_culture,
                        "date_begin": date_begin,
                        "date_end": date_end,
                        "department_id": department_id,
                        "geo_location": geo_location,
                        "has_images": has_images,
                        "is_highlight": is_highlight,
                        "is_on_view": is_on_view,
                        "medium": medium,
                        "tags": tags,
                        "title": title,
                    },
                    client_search_params.ClientSearchParams,
                ),
            ),
            cast_to=Works,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncMetMuseum(AsyncAPIClient):
    collections: collections.AsyncCollectionsResource
    departments: departments.AsyncDepartmentsResource
    with_raw_response: AsyncMetMuseumWithRawResponse
    with_streaming_response: AsyncMetMuseumWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async met-museum client instance."""
        if base_url is None:
            base_url = os.environ.get("MET_MUSEUM_BASE_URL")
        if base_url is None:
            base_url = f"https://collectionapi.metmuseum.org/public/collection/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.collections = collections.AsyncCollectionsResource(self)
        self.departments = departments.AsyncDepartmentsResource(self)
        self.with_raw_response = AsyncMetMuseumWithRawResponse(self)
        self.with_streaming_response = AsyncMetMuseumWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def search(
        self,
        *,
        q: str,
        artist_or_culture: bool | NotGiven = NOT_GIVEN,
        date_begin: int | NotGiven = NOT_GIVEN,
        date_end: int | NotGiven = NOT_GIVEN,
        department_id: int | NotGiven = NOT_GIVEN,
        geo_location: str | NotGiven = NOT_GIVEN,
        has_images: bool | NotGiven = NOT_GIVEN,
        is_highlight: bool | NotGiven = NOT_GIVEN,
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

          is_highlight: Returns objects that match the query and are designated as highlights.
              Highlights are selected works of art from The Met Museum’s permanent collection
              representing different cultures and time periods.

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
        return await self.get(
            "/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "artist_or_culture": artist_or_culture,
                        "date_begin": date_begin,
                        "date_end": date_end,
                        "department_id": department_id,
                        "geo_location": geo_location,
                        "has_images": has_images,
                        "is_highlight": is_highlight,
                        "is_on_view": is_on_view,
                        "medium": medium,
                        "tags": tags,
                        "title": title,
                    },
                    client_search_params.ClientSearchParams,
                ),
            ),
            cast_to=Works,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class MetMuseumWithRawResponse:
    def __init__(self, client: MetMuseum) -> None:
        self.collections = collections.CollectionsResourceWithRawResponse(client.collections)
        self.departments = departments.DepartmentsResourceWithRawResponse(client.departments)

        self.search = to_raw_response_wrapper(
            client.search,
        )


class AsyncMetMuseumWithRawResponse:
    def __init__(self, client: AsyncMetMuseum) -> None:
        self.collections = collections.AsyncCollectionsResourceWithRawResponse(client.collections)
        self.departments = departments.AsyncDepartmentsResourceWithRawResponse(client.departments)

        self.search = async_to_raw_response_wrapper(
            client.search,
        )


class MetMuseumWithStreamedResponse:
    def __init__(self, client: MetMuseum) -> None:
        self.collections = collections.CollectionsResourceWithStreamingResponse(client.collections)
        self.departments = departments.DepartmentsResourceWithStreamingResponse(client.departments)

        self.search = to_streamed_response_wrapper(
            client.search,
        )


class AsyncMetMuseumWithStreamedResponse:
    def __init__(self, client: AsyncMetMuseum) -> None:
        self.collections = collections.AsyncCollectionsResourceWithStreamingResponse(client.collections)
        self.departments = departments.AsyncDepartmentsResourceWithStreamingResponse(client.departments)

        self.search = async_to_streamed_response_wrapper(
            client.search,
        )


Client = MetMuseum

AsyncClient = AsyncMetMuseum

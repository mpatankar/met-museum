# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Work", "Constituent", "Measurement", "MeasurementElementMeasurements", "Tag"]


class Constituent(BaseModel):
    constituent_id: Optional[float] = FieldInfo(alias="constituentID", default=None)

    constituent_ulan_url: Optional[str] = FieldInfo(alias="constituentULAN_URL", default=None)

    constituent_wikidata_url: Optional[str] = FieldInfo(alias="constituentWikidata_URL", default=None)

    gender: Optional[str] = None

    name: Optional[str] = None

    role: Optional[str] = None


class MeasurementElementMeasurements(BaseModel):
    height: Optional[float] = FieldInfo(alias="Height", default=None)

    width: Optional[float] = FieldInfo(alias="Width", default=None)


class Measurement(BaseModel):
    element_description: Optional[str] = FieldInfo(alias="elementDescription", default=None)

    element_measurements: Optional[MeasurementElementMeasurements] = FieldInfo(
        alias="elementMeasurements", default=None
    )

    element_name: Optional[str] = FieldInfo(alias="elementName", default=None)


class Tag(BaseModel):
    aat_url: Optional[str] = FieldInfo(alias="AAT_URL", default=None)

    term: Optional[str] = None

    wikidata_url: Optional[str] = FieldInfo(alias="Wikidata_URL", default=None)


class Work(BaseModel):
    accession_number: Optional[str] = FieldInfo(alias="accessionNumber", default=None)

    accession_year: Optional[str] = FieldInfo(alias="accessionYear", default=None)

    additional_images: Optional[List[str]] = FieldInfo(alias="additionalImages", default=None)

    artist_alpha_sort: Optional[str] = FieldInfo(alias="artistAlphaSort", default=None)

    artist_begin_date: Optional[str] = FieldInfo(alias="artistBeginDate", default=None)

    artist_display_bio: Optional[str] = FieldInfo(alias="artistDisplayBio", default=None)

    artist_display_name: Optional[str] = FieldInfo(alias="artistDisplayName", default=None)

    artist_end_date: Optional[str] = FieldInfo(alias="artistEndDate", default=None)

    artist_gender: Optional[str] = FieldInfo(alias="artistGender", default=None)

    artist_nationality: Optional[str] = FieldInfo(alias="artistNationality", default=None)

    artist_prefix: Optional[str] = FieldInfo(alias="artistPrefix", default=None)

    artist_role: Optional[str] = FieldInfo(alias="artistRole", default=None)

    artist_suffix: Optional[str] = FieldInfo(alias="artistSuffix", default=None)

    artist_ulan_url: Optional[str] = FieldInfo(alias="artistULAN_URL", default=None)

    artist_wikidata_url: Optional[str] = FieldInfo(alias="artistWikidata_URL", default=None)

    city: Optional[str] = None

    classification: Optional[str] = None

    constituents: Optional[List[Constituent]] = None

    country: Optional[str] = None

    county: Optional[str] = None

    credit_line: Optional[str] = FieldInfo(alias="creditLine", default=None)

    culture: Optional[str] = None

    department: Optional[str] = None

    dimensions: Optional[str] = None

    dynasty: Optional[str] = None

    excavation: Optional[str] = None

    gallery_number: Optional[str] = FieldInfo(alias="GalleryNumber", default=None)

    geography_type: Optional[str] = FieldInfo(alias="geographyType", default=None)

    is_highlight: Optional[bool] = FieldInfo(alias="isHighlight", default=None)

    is_public_domain: Optional[bool] = FieldInfo(alias="isPublicDomain", default=None)

    is_timeline_work: Optional[bool] = FieldInfo(alias="isTimelineWork", default=None)

    link_resource: Optional[str] = FieldInfo(alias="linkResource", default=None)

    locale: Optional[str] = None

    locus: Optional[str] = None

    measurements: Optional[List[Measurement]] = None

    medium: Optional[str] = None

    metadata_date: Optional[str] = FieldInfo(alias="metadataDate", default=None)

    object_begin_date: Optional[float] = FieldInfo(alias="objectBeginDate", default=None)

    object_date: Optional[str] = FieldInfo(alias="objectDate", default=None)

    object_end_date: Optional[float] = FieldInfo(alias="objectEndDate", default=None)

    object_id: Optional[float] = FieldInfo(alias="objectID", default=None)

    object_name: Optional[str] = FieldInfo(alias="objectName", default=None)

    object_url: Optional[str] = FieldInfo(alias="objectURL", default=None)

    object_wikidata_url: Optional[str] = FieldInfo(alias="objectWikidata_URL", default=None)

    period: Optional[str] = None

    portfolio: Optional[str] = None

    primary_image: Optional[str] = FieldInfo(alias="primaryImage", default=None)

    primary_image_small: Optional[str] = FieldInfo(alias="primaryImageSmall", default=None)

    region: Optional[str] = None

    reign: Optional[str] = None

    repository: Optional[str] = None

    rights_and_reproduction: Optional[str] = FieldInfo(alias="rightsAndReproduction", default=None)

    river: Optional[str] = None

    state: Optional[str] = None

    subregion: Optional[str] = None

    tags: Optional[List[Tag]] = None

    title: Optional[str] = None

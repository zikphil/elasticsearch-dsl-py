#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

# flake8: noqa:F401
#
# The dynamic sorting of `__all__` at the bottom of the file breaks flake8
# because flake8 is a static analysis tool. The alternative to ignoring these
# "unused import" errors would be to duplicate  `__all__` statically after the
# async files are imported.

import sys

from . import connections
from .aggs import A
from .analysis import analyzer, char_filter, normalizer, token_filter, tokenizer
from .document import Document, InnerDoc, MetaField
from .exceptions import (
    ElasticsearchDslException,
    IllegalOperation,
    UnknownDslObject,
    ValidationException,
)
from .faceted_search import (
    DateHistogramFacet,
    Facet,
    FacetedResponse,
    FacetedSearch,
    HistogramFacet,
    NestedFacet,
    RangeFacet,
    TermsFacet,
)
from .field import (
    Binary,
    Boolean,
    Byte,
    Completion,
    CustomField,
    Date,
    DateRange,
    DenseVector,
    Double,
    DoubleRange,
    Field,
    Float,
    FloatRange,
    GeoPoint,
    GeoShape,
    HalfFloat,
    Integer,
    IntegerRange,
    Ip,
    IpRange,
    Join,
    Keyword,
    Long,
    LongRange,
    Murmur3,
    Nested,
    Object,
    Percolator,
    RangeField,
    RankFeature,
    ScaledFloat,
    SearchAsYouType,
    Short,
    SparseVector,
    Text,
    TokenCount,
    construct_field,
)
from .function import SF
from .index import Index, IndexTemplate
from .mapping import Mapping
from .query import Q
from .search import MultiSearch, Search
from .update_by_query import UpdateByQuery
from .utils import AttrDict, AttrList, DslBase
from .wrappers import Range

VERSION = (7, 2, 0)
__version__ = VERSION
__versionstr__ = ".".join(map(str, VERSION))
__all__ = [
    "A",
    "AttrDict",
    "AttrList",
    "Binary",
    "Boolean",
    "Byte",
    "Completion",
    "CustomField",
    "Date",
    "DateHistogramFacet",
    "DateRange",
    "DenseVector",
    "Document",
    "Double",
    "DoubleRange",
    "DslBase",
    "ElasticsearchDslException",
    "Facet",
    "FacetedResponse",
    "FacetedSearch",
    "Field",
    "Float",
    "FloatRange",
    "GeoPoint",
    "GeoShape",
    "HalfFloat",
    "HistogramFacet",
    "IllegalOperation",
    "Index",
    "IndexTemplate",
    "InnerDoc",
    "Integer",
    "IntegerRange",
    "Ip",
    "IpRange",
    "Join",
    "Keyword",
    "Long",
    "LongRange",
    "Mapping",
    "MetaField",
    "MultiSearch",
    "Murmur3",
    "Nested",
    "NestedFacet",
    "Object",
    "Percolator",
    "Q",
    "Range",
    "RangeFacet",
    "RangeField",
    "RankFeature",
    "SF",
    "ScaledFloat",
    "Search",
    "SearchAsYouType",
    "Short",
    "SparseVector",
    "TermsFacet",
    "Text",
    "TokenCount",
    "UnknownDslObject",
    "UpdateByQuery",
    "ValidationException",
    "analyzer",
    "char_filter",
    "connections",
    "construct_field",
    "normalizer",
    "token_filter",
    "tokenizer",
]


try:
    # Asyncio only supported in Python 3.6+
    if sys.version_info < (3, 6):
        raise ImportError

    from elasticsearch_dsl._async.document import AsyncDocument
    from elasticsearch_dsl._async.faceted_search import AsyncFacetedSearch
    from elasticsearch_dsl._async.index import AsyncIndex, AsyncIndexTemplate
    from elasticsearch_dsl._async.mapping import AsyncMapping
    from elasticsearch_dsl._async.search import AsyncMultiSearch, AsyncSearch
    from elasticsearch_dsl._async.update_by_query import AsyncUpdateByQuery

    __all__ = sorted(
        __all__
        + [
            "AsyncDocument",
            "AsyncFacetedSearch",
            "AsyncIndex",
            "AsyncIndexTemplate",
            "AsyncMapping",
            "AsyncMultiSearch",
            "AsyncSearch",
            "AsyncUpdateByQuery",
        ]
    )

except (ImportError, SyntaxError):
    pass

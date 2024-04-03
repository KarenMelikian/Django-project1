from django.db.models import Q
from django.contrib.postgres.search import (SearchVector,
                                            SearchRank,
                                            SearchQuery,
                                            SearchHeadline,
                                            )

from .models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        product_id = int(query)
        return Products.objects.filter(id=product_id)

    vector = SearchVector('name', 'description')
    query = SearchQuery(query)

    return Products.objects.annotate(
        rank=SearchRank(
            vector,
            query
        )
    ).filter(rank__gt=0).order_by('-rank')
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

    return Products.objects.filter(description__search=query)



    # keywords = [word for word in query.split() if len(word) > 2]
    #
    # q_objects = Q()
    #
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
    #
    # return Products.objects.filter(q_objects)
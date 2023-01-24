from typing import Protocol, OrderedDict

from django.db.models import QuerySet

from blogs import models, repositories

class BlogServicesInterface(Protocol):
    repos: repositories.BlogRepositoriesInterface

    def create_blog(self, data: OrderedDict) -> models.Blog: ...

    def get_blogs(self) -> QuerySet[models.Blog]: ...


class BlogServicesV1:
    repos = repositories.BlogRepositoriesV1()

    def create_blog(self, data: OrderedDict) -> models.Blog:
        return self.repos.create_blog(data=data)

    def get_blogs(self) -> QuerySet[models.Blog]:
        return self.repos.get_blogs()
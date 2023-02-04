from typing import Protocol, OrderedDict

from django.db.models import QuerySet

from accounts import models, repos

class AccountServicesInterface(Protocol):
    account_repos: repos.AccountReposInterface

    def get_account(self) -> QuerySet[models.Account]: ...

    def create_account(self, data: OrderedDict) -> None: ...


class AccountServicesV1:
    account_repos: repos.AccountReposInterface = repos.AccountReposV1()

    def get_account(self) -> QuerySet[models.Account]:
        return self.account_repos.get_account()

    def create_account(self, data: OrderedDict) -> None:
        self.account_repos.create_account(data=data)
import abc

import telegram as tg


class BaseMessages(abc.ABC):
    @abc.abstractmethod
    def start(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def help(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def echo(self, text: str) -> str:
        raise NotImplemented


class RegularUser(BaseMessages):
    def start(self) -> str:
        return "Hi!"

    def help(self) -> str:
        return "You need to subscribe."

    def echo(self, text: str) -> str:
        return f'{text}'


class PremiumUser(RegularUser):
    def start(self) -> str:
        return "Hello!"

    def help(self) -> str:
        return "Our manager will contact you soon."


def get_messages(user: tg.User) -> BaseMessages:
    if user.is_premium:
        return PremiumUser()
    return RegularUser()

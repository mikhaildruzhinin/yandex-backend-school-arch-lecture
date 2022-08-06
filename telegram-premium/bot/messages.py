import abc


class BaseMessages(abc.ABC):
    @property
    @abc.abstractmethod
    async def start(self) -> str:
        raise NotImplemented

    @property
    @abc.abstractmethod
    async def help(self) -> str:
        raise NotImplemented

    @property
    @abc.abstractmethod
    async def echo(self) -> str:
        raise NotImplemented


class RegularUser(BaseMessages):
    @property
    async def start(self) -> str:
        return "Hi!"

    @property
    async def help(self) -> str:
        return "You need to subscribe."

    @property
    async def echo(self, text: str) -> str:
        return f'{text}'


class PremiumUser(RegularUser):
    @property
    async def start(self) -> str:
        return "Hello!"

    @property
    async def help(self) -> str:
        raise "Our manager will contact you soon."

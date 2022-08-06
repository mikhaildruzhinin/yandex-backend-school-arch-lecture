import abc
import typing as tp

import telegram as tg
import telegram.ext as tg_ext


class BaseHandler(abc.ABC):
    def __init__(self) -> None:
        self.user: tp.Optional[tg.User] = None
    
    async def __call__(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        self.user = update.effective_user
        await self.handle(update, context)

    @abc.abstractmethod
    async def handle(update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        raise NotImplemented


class StartHandler(BaseHandler):
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(
            rf'Hi {self.user.mention_html()}!',
            reply_markup=tg.ForceReply(selective=True),
        )


class HelpHandler(BaseHandler):
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text('Help!')


class EchoHandler(BaseHandler):
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(update.message.text)


def setup_handlers(application: tg_ext.Application) -> None:
    application.add_handler(tg_ext.CommandHandler('start', StartHandler()))
    application.add_handler(tg_ext.CommandHandler('help', HelpHandler()))

    application.add_handler(
        tg_ext.MessageHandler(tg_ext.filters.TEXT & ~tg_ext.filters.COMMAND, EchoHandler())
    )

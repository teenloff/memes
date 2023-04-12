

from .. import loader


@loader.tds
class MemesVoiceMod(loader.Module):
    """🎤 Мемные звуки"""

    strings = {"name": "MemesVoice"}

    async def bandcmd(self, message):
        """Здарова Бандиты"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/cs16memes/2",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def chaicmd(self, message):
        """Саундтрек Чай-Чай"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/cs16memes/3",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def suetacmd(self, message):
        """Суету навести охота"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/cs16memes/4",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def zaebcmd(self, message):
        """Здарова заебал"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/cs16memes/5",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def pesnyacmd(self, message):
        """Следущая песня звучит специально для пацанов"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/cs16memes/6",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def dobrocmd(self, message):
        """Добро пожаловать на сервер шизофрения"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/cs16memes/7",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def gandoncmd(self, message):
        """Нюхни газку"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/cs16memes/8",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def bruhcmd(self, message):
        """Брах"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/cs16memes/9",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def nahuicmd(self, message):
        """Нахуй я сюда пришел"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/cs16memes/10",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def oprivetcmd(self, message):
        """О привет!"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/cs16memes/11",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def kudacmd(self, message):
        """Кто куда а я посьебам"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/cs16memes/12",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
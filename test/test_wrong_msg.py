from telethon import TelegramClient, events
import conf_tests as ct
import asyncio
import pytest

client = TelegramClient(ct.session_name, ct.api_id, ct.api_hash, system_version=ct.sys_ver)

#Тест ответа бота на некорректное сообщение пользователя
@pytest.mark.asyncio
async def test_wrong_msg():
    flag = False

    @client.on(events.NewMessage(chats=ct.bot_name, incoming = True))
    async def handler_wrong_msg(event):
        nonlocal flag
        if ct.wrong_msg_reply in event.raw_text:
            flag = True
            client.disconnect()
        else: 
            client.disconnect()

    async with client:
        await client.send_message(ct.bot_name, '1Q#%$^23&%#&hthf45')
        for i in range(5):
            if flag:
                break
            await asyncio.sleep(1)
        client.disconnect()
    
    assert flag
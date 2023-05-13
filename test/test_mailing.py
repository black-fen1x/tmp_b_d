from telethon import TelegramClient, events
import conf_tests as ct
import asyncio
import pytest

client = TelegramClient(ct.session_name, ct.api_id, ct.api_hash, system_version=ct.sys_ver)

#Тест функции рассылки по группе
@pytest.mark.asyncio
async def test_mailing():
    flag = False
    n = 0

    @client.on(events.NewMessage(chats=ct.bot_name, incoming = True))
    async def handler_mailing(event):
        nonlocal flag, n
        if 'Введите группу для рассылки' in event.raw_text:
            n += 1
            await client.send_message(ct.bot_name, ct.default_group)
        elif 'Введите сообщение' in event.raw_text:
            n += 1
            await client.send_message(ct.bot_name, ct.mailing_msg)
        elif ct.mailing_msg in event.raw_text:
            n += 1
            if n == 3:
                flag = True
                client.disconnect()
        else:
            client.disconnect()
            

    async with client:
        await client.send_message(ct.bot_name, ct.mailing_btn)
        for i in range(5):
            if flag:
                break
            await asyncio.sleep(1)
        client.disconnect()
    
    assert flag
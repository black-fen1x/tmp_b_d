from telethon import TelegramClient, events
import conf_tests as ct
import asyncio
import pytest

client = TelegramClient(ct.session_name, ct.api_id, ct.api_hash, system_version=ct.sys_ver)

#Тест функции смены группы пользователем
@pytest.mark.asyncio
async def test_change_group():
    flag = False
    f1 = False
    f2 = False

    @client.on(events.NewMessage(chats=ct.bot_name, incoming = True))
    async def handler_change_group(event):
        nonlocal flag, f1, f2
        if 'Введите новое значение' in event.raw_text:
            f1 = True
            await client.send_message(ct.bot_name, ct.default_group)
        elif 'Группа успешно изменена!' in event.raw_text:
            f2 = True
            if f1 and f2:
                flag = True
                client.disconnect()
        else: 
            client.disconnect()


    async with client:
        await client.send_message(ct.bot_name, ct.change_group_btn)
        for i in range(5):
            if flag:
                break
            await asyncio.sleep(1)
        client.disconnect()
    
    assert flag



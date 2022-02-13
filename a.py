import asyncio
from main import Mirai, MiraiSession, Bot, BotConfiguration


Mirai(
       MiraiSession(
              verify_key="verifyKey",
              host="localhost:8080",
       ),
       loop=asyncio.get_event_loop(),
       bots=[
              Bot(BotConfiguration(account=1375075223)),
              Bot(BotConfiguration(account=552282813))
       ]
).launch_blocking()

app = Mirai.getIntance()

# source = Source.parse_obj({'type': 'Source', 'id': 8728, 'time': 1643272815})
# print(source)
# MessageChain.deserializeMiraiCode("[mirai:atall]")

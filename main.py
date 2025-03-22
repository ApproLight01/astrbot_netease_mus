import re
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api.message_components import Node, Nodes, Plain
from astrbot.api import logger

# **网易云音乐链接正则表达式**
NETEASE_MUSIC_PATTERN = r"https://y\.music\.163\.com/m/song\?id=(\d+)&userid=(\d+)&dlt=(\d+)"

@register("netease_music_parser", "YourName", "解析网易云音乐链接参数", "1.0.0")
class NeteaseMusicParser(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.regex(NETEASE_MUSIC_PATTERN)
    async def handle_netease_music_link(self, event: AstrMessageEvent):
        """监听网易云音乐链接并解析参数"""
        msg = event.message_str

        # **解析链接**
        match = re.search(NETEASE_MUSIC_PATTERN, msg)
        if match:
            song_id = match.group(1)
            user_id = match.group(2)
            dlt = match.group(3)

            # **拼接文本**
            result_text = f"解析结果：id={song_id}, userid={user_id}, dlt={dlt}"

            # **创建消息节点**
            nodes = Nodes([Node(uin=event.get_self_id(), name="MusicParserBot", content=[Plain(result_text)])])

            # **发送消息**
            yield event.chain_result([nodes])
        else:
            logger.error("❌ 解析网易云音乐链接失败")
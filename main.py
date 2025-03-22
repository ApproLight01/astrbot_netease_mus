import logging
import random
import requests
from urllib.parse import urlparse, parse_qs
from astrbot.api.star import Context, Star, register
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.event.filter import event_message_type, EventMessageType

logger = logging.getLogger(__name__)

@register("music_link_extractor", "ましろSaber", "一个音乐链接参数提取插件", "1.1", "repo url")
class MusicLinkExtractorPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @event_message_type(EventMessageType.ALL)
    async def on_message(self, event: AstrMessageEvent) -> MessageEventResult:
        """
        当消息中包含网易云音乐链接时，提取id、userid和dlt参数并发送到群聊。
        """
        msg_obj = event.message_obj
        text = msg_obj.message_str or ""

        logger.debug("=== Debug: AstrBotMessage ===")
        logger.debug("Bot ID: %s", msg_obj.self_id)
        logger.debug("Session ID: %s", msg_obj.session_id)
        logger.debug("Message ID: %s", msg_obj.message_id)
        logger.debug("Sender: %s", msg_obj.sender)
        logger.debug("Group ID: %s", msg_obj.group_id)
        logger.debug("Message Chain: %s", msg_obj.message)
        logger.debug("Raw Message: %s", msg_obj.raw_message)
        logger.debug("Timestamp: %s", msg_obj.timestamp)
        logger.debug("============================")

        if "https://y.music.163.com/m/song?" in text:
            try:
                # 解析URL
                parsed_url = urlparse(text.split("https://y.music.163.com/m/song?")[1].split()[0])
                query_params = parse_qs(parsed_url.query)

                id_value = query_params.get('id', [''])[0]
                userid_value = query_params.get('userid', [''])[0]
                dlt_value = query_params.get('dlt', [''])[0]

                result_text = f"id: {id_value}, userid: {userid_value}, dlt: {dlt_value}"
                yield event.plain_result(result_text)
            except Exception as e:
                logger.error(f"提取参数时出错: {e}")

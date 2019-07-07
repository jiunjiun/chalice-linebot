#!/usr/bin/env python
import os

from chalice import Chalice
from chalice import Response

from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
from linebot.exceptions import (InvalidSignatureError, LineBotApiError)

app = Chalice(app_name='chalice-linebot')

line_bot_api = LineBotApi(os.environ['LINEBOT_CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['LINEBOT_CHANNEL_SECRET'])

@app.route('/callback', methods=['POST'])
def callback():
    signature = app.current_request.headers['X-Line-Signature']
    body = app.current_request.raw_body.decode('utf-8')
    try:
        handler.handle(body, signature)
    except InvalidSignatureError as e:
        return Response({'error': e.message}, status_code=400)
    except LineBotApiError as e:
        if e.message == 'Invalid reply token':
            return 'OK'
        return Response({'error': e.message}, status_code=400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    # app.log.error("message: " + event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Reply: {}'.format(event.message.text))
    )

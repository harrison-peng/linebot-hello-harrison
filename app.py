# -*- coding: UTF-8 -*-

import os
import teachMode as teach
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(os.environ['LINE_CHANNEL_ACCESS_TOKEN'])
# Channel Secret
handler = WebhookHandler(os.environ['LINE_CHANNEL_SECRET'])

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text

    try:
        if message == '教我說話':
            content = '嗨嗨～只要在照著 [@學習 指令 回覆] 這個格式輸入就可以讓我學習說話哦!還不趕快試試嗎？'
            res_message = TextSendMessage(text=content)
            line_bot_api.reply_message(event.reply_token, res_message)
        elif message == '猜數字遊戲':
            confirm_template_message = TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://example.com/image.jpg',
                    title='【猜數字】',
                    text='猜一個四位不重複的數字，A表示數字對位置對，B表示數字錯位置錯，透過已知的線索，來看看你能多快猜到數字吧！',
                    actions=[
                        PostbackAction(
                            label='我要玩',
                            text='#我要玩猜數字',
                            data='action=buy&itemid=1'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, confirm_template_message)
        elif message == '觀看作品':
            pass
        else:
            if message.startswith('@學習 '):
                res = teach.learn_new_word(message)
            else:
                result = teach.responding(message)
                if result is None:
                    res = '還沒學會哦！'
                else:
                    res = result
            res_message = TextSendMessage(text=res)
            line_bot_api.reply_message(event.reply_token, res_message)
    except Exception as e:
        res_message = TextSendMessage(text=str(e))
        line_bot_api.reply_message(event.reply_token, res_message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

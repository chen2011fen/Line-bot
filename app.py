from flask import Flask, request, abort             # python用來架設伺服器/網站的套件有 flash(小規模)、django(大型專案)
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('fC/kMcuHe4GukZDcqa8V2XhKVdj5uKBj38i2fR6qAB9TvMa2L0NwzeauJ6p52'
                          '+2lv9yPDutnsYDJ9aW7TosW6K47aEFgGnZQijFys1UVhHUbQbWxjzt6LVD'
                          '/bNjkpaLJ2UagYYhzaO72pHAyOtoGTgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1245cd255c16b7934cc1fec4a8757ade')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s = "什麼?"

    if "貼圖" in msg:
        sticker_message = StickerSendMessage(
            package_id='2',
            sticker_id='23'
        )
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return

    if msg in ["hi", "Hi"]:
        s = "嗨"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()


# test-new-1

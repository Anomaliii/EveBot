import requests
from Cutiepii_Robot import dispatcher
from Cutiepii_Robot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from kaga.modules.helper_funcs.alternate import typing_action


@typing_action
def ud(update, context):
    message = update.effective_message
    text = message.text[len('/ud '):]
    results = requests.get(
        f'https://api.urbandictionary.com/v0/define?term={text}').json()
    try:
        reply_text = f'*{text}*\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
    except:
        reply_text = "No results found."
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


UD_HANDLER = DisableAbleCommandHandler(["ud"], ud, run_async=True)

dispatcher.add_handler(UD_HANDLER)

__command_list__ = ["ud"]
__handlers__ = [UD_HANDLER]

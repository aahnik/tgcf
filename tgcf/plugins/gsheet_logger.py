import logging

from tgcf.plugins import TgcfMessage, TgcfPlugin
from tgcf.plugin_models import GsheetLogger
import gspread_asyncio
from google.oauth2.service_account import Credentials
import json
from datetime import datetime
from io import StringIO


class TgcfGsheetLogger(TgcfPlugin):
    id_ = "gsheet_logger"

    def __init__(self, data: GsheetLogger) -> None:
        self.gsl = data

    async def __ainit__(self) -> None:
        def get_creds():
            # To obtain a service account JSON file, follow these steps:
            # https://gspread.readthedocs.io/en/latest/oauth2.html#for-bots-using-service-account
            service_account_info = json.load(StringIO(self.gsl.service_account_json))
            creds = Credentials.from_service_account_info(service_account_info)
            scoped = creds.with_scopes(
                [
                    "https://spreadsheets.google.com/feeds",
                    "https://www.googleapis.com/auth/spreadsheets",
                    "https://www.googleapis.com/auth/drive",
                ]
            )
            return scoped

        self.agcm = gspread_asyncio.AsyncioGspreadClientManager(get_creds)
        self.next_row = 2
        agc = await self.agcm.authorize()
        ss = await agc.open_by_url(self.gsl.gsheet_link)
        wks = await ss.get_worksheet(0)
        existing_values = await wks.get_all_values()
        self.next_row = len(existing_values) + 1

    async def modify(self, tm: TgcfMessage) -> TgcfMessage:
        logging.info("Processing message under Gsheet Logger")

        if not tm.text.startswith(self.gsl.prefix):
            return tm

        agc = await self.agcm.authorize()
        ss = await agc.open_by_url(self.gsl.gsheet_link)
        wks = await ss.get_worksheet(0)
        await wks.update(f"A{self.next_row}", str(datetime.now()))
        await wks.update(f"B{self.next_row}", str(tm.sender_id))
        await wks.update(
            f"C{self.next_row}", str(tm.text.lstrip(self.gsl.prefix).strip())
        )
        self.next_row += 1

        return tm

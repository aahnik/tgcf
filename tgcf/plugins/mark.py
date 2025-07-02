import logging

from tgcf.plugins import TgcfMessage, TgcfPlugin


class TgcfMark(TgcfPlugin):
    id_ = "mark"

    def __init__(self, data) -> None:
        self.data = data # data will be the simplified MarkConfig

    async def modify(self, tm: TgcfMessage) -> TgcfMessage:
        if tm.file_type == "nofile" or not tm.message.media:
            # No file/media in the message, so nothing to do
            return tm

        # Download the media from the message
        # tm.get_file() handles the download and returns the path
        # It also sets tm.file_type correctly if not already set by Telethon
        try:
            downloaded_file_path = await tm.get_file()
            if downloaded_file_path:
                tm.new_file = downloaded_file_path
                tm.cleanup = True # Mark the downloaded file for cleanup after sending
                logging.info(f"Mark plugin: Prepared media {tm.new_file} for sending.")
            else:
                logging.warning("Mark plugin: tm.get_file() did not return a path.")
        except Exception as e:
            logging.error(f"Mark plugin: Error downloading file: {e}")
            # Optionally, decide if you want to suppress the message or send it without media
            # For now, returning tm as is, which might mean it's sent without media if download failed
            # or if an earlier stage populated tm.new_file incorrectly.
            pass # Let it proceed, sender might still handle text part

        return tm

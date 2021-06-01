from typing import Any, Dict

from pydantic import BaseModel  # pylint: disable=no-name-in-module
from watermark import File, Position, Watermark, apply_watermark

from tgcf.plugins import TgcfMessage, TgcfPlugin
from tgcf.utils import cleanup


class MarkConfig(BaseModel):
    image: str = "image.png"
    position: Position = Position.centre
    frame_rate: int = 15


class TgcfMark(TgcfPlugin):
    id_ = "mark"

    def __init__(self, data: Dict[str, Any]) -> None:
        self.data = MarkConfig(**data)

    async def modify(self, tm: TgcfMessage) -> TgcfMessage:
        if not tm.file_type in ["gif", "video", "photo"]:
            return tm
        downloaded_file = await tm.get_file()
        base = File(downloaded_file)
        overlay = File(self.data.image)
        wtm = Watermark(overlay, self.data.position)
        tm.new_file = apply_watermark(base, wtm, frame_rate=self.data.frame_rate)
        cleanup(downloaded_file)
        tm.cleanup = True
        return tm

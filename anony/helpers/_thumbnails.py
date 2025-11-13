# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


import os
import aiohttp
from PIL import (Image, ImageDraw, ImageEnhance,
                 ImageFilter, ImageFont, ImageOps)

from anony import config
from anony.helpers import Track


class Thumbnail:
    def __init__(self):
        self.rect = (914, 514)
        self.fill = (255, 255, 255)
        self.mask = Image.new("L", self.rect, 0)
        self.font1 = ImageFont.truetype("anony/helpers/Raleway-Bold.ttf", 30)
        self.font2 = ImageFont.truetype("anony/helpers/Inter-Light.ttf", 30)

    async def save_thumb(self, output_path: str, url: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                open(output_path, "wb").write(await resp.read())
            return output_path

    async def generate(self, song: Track, size=(1280, 720)) -> str:
        try:
            temp = f"cache/temp_{song.id}.jpg"
            output = f"cache/{song.id}.png"
            if os.path.exists(output):
                return output

            await self.save_thumb(temp, song.thumbnail)
            thumb = Image.open(temp).convert("RGBA").resize(size, Image.Resampling.LANCZOS)
            blur = thumb.filter(ImageFilter.GaussianBlur(25))
            image = ImageEnhance.Brightness(blur).enhance(.40)

            _rect = ImageOps.fit(thumb, self.rect, method=Image.LANCZOS, centering=(0.5, 0.5))
            ImageDraw.Draw(self.mask).rounded_rectangle((0, 0, self.rect[0], self.rect[1]), radius=15, fill=255)
            _rect.putalpha(self.mask)
            image.paste(_rect, (183, 30), _rect)

            draw = ImageDraw.Draw(image)
            draw.text((50, 560), f"{song.channel_name[:25]} | {song.view_count}", font=self.font2, fill=self.fill)
            draw.text((50, 600), song.title[:50], font=self.font1, fill=self.fill)
            draw.text((40, 650), "0:01", font=self.font1)
            draw.line([(140, 670), (1160, 670)], fill=self.fill, width=5, joint="curve")
            draw.text((1185, 650), song.duration, font=self.font1, fill=self.fill)

            image.save(output)
            os.remove(temp)
            return output
        except:
            config.DEFAULT_THUMB

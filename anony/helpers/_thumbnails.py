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
        # Square cover art size for the right panel
        self.cover_size = (455, 450)
        self.fill = (255, 255, 255)
        
        # Typography scaling
        self.font_header = ImageFont.truetype("anony/helpers/Raleway-Bold.ttf", 32)
        self.font_title = ImageFont.truetype("anony/helpers/Raleway-Bold.ttf", 60)
        self.font_track = ImageFont.truetype("anony/helpers/Raleway-Bold.ttf", 36)
        self.font_info = ImageFont.truetype("anony/helpers/Inter-Light.ttf", 26)
        self.font_time = ImageFont.truetype("anony/helpers/Raleway-Bold.ttf", 22)
        
        self.session: aiohttp.ClientSession | None = None

    async def start(self) -> None:
        self.session = aiohttp.ClientSession()

    async def close(self) -> None:
        if self.session:
            await self.session.close()

    async def save_thumb(self, output_path: str, url: str) -> str:
        async with self.session.get(url) as resp:
            with open(output_path, "wb") as f:
                f.write(await resp.read())
        return output_path

    async def generate(self, song: Track, size=(1280, 720)) -> str:
        try:
            temp = f"cache/temp_{song.id}.jpg"
            output = f"cache/{song.id}.png"
            if os.path.exists(output):
                return output

            await self.save_thumb(temp, song.thumbnail)
            raw_thumb = Image.open(temp).convert("RGBA")

            # Background: blurred & darkened original artwork
            bg_image = raw_thumb.resize(size, Image.Resampling.LANCZOS)
            blur = bg_image.filter(ImageFilter.GaussianBlur(35))
            image = ImageEnhance.Brightness(blur).enhance(0.35)

            # Foreground: cropped square cover placed on the right
            cover = ImageOps.fit(raw_thumb, self.cover_size, method=Image.Resampling.LANCZOS)
            image.paste(cover, (730, 90))

            draw = ImageDraw.Draw(image)

            # Header / Branding
            draw.text((70, 40), "GenZ Official", font=self.font_header, fill=self.fill)

            # Track Information Section
            draw.text((70, 170), "NOW PLAYING", font=self.font_title, fill=self.fill)
            
            # Truncate title cleanly if too long
            title_text = song.title[:30] + "..." if len(song.title) > 30 else song.title
            draw.text((70, 290), title_text, font=self.font_track, fill=self.fill)

            # Metadata details
            draw.text((70, 395), f"Views : {song.view_count}", font=self.font_info, fill=self.fill)
            draw.text((70, 460), f"Duration : {song.duration}", font=self.font_info, fill=self.fill)
            draw.text((70, 520), f"Channel : {song.channel_name[:25]}", font=self.font_info, fill=self.fill)

            # Progress Bar & Timestamps
            draw.text((70, 600), "00:55", font=self.font_time, fill=self.fill)
            draw.text((1160, 600), song.duration, font=self.font_time, fill=self.fill)

            # Track slider lines and pointer knob
            bar_start_x, bar_end_x, bar_y = 170, 1140, 624
            knob_x = bar_start_x + int((bar_end_x - bar_start_x) * 0.30)  # ~30% progress

            draw.line([(bar_start_x, bar_y), (bar_end_x, bar_y)], fill=self.fill, width=4)
            draw.ellipse([(knob_x - 8, bar_y - 8), (knob_x + 8, bar_y + 8)], fill=self.fill)

            # Volume Indicator at bottom
            draw.text((70, 675), "Volume:  ■ ■ ■ ■ ■ □ □ □ □ □", font=self.font_info, fill=self.fill)

            image.save(output)
            
            try:
                os.remove(temp)
            except Exception:
                pass
                
            return output
        except Exception:
            return config.DEFAULT_THUMB

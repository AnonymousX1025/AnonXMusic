# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


from dataclasses import dataclass


@dataclass
class Media:
    id: str
    duration: str = "00:00"
    duration_sec: int = 0
    file_path: str = None
    message_id: int = 0
    title: str = None
    url: str = None
    time: int = 0
    user: str = None
    video: bool = False


@dataclass
class Track:
    id: str
    channel_name: str = None
    duration: str = "00:00"
    duration_sec: int = 0
    title: str = None
    url: str = None
    file_path: str = None
    message_id: int = 0
    time: int = 0
    thumbnail: str = None
    user: str = None
    view_count: str = None
    video: bool = False

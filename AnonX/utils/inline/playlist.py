from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴩᴇʀsᴏɴᴀʟ",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="ᴛᴏᴘ 10", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ɢʟᴏʙᴀʟ ᴛᴏᴘ 10", callback_data="SERVERTOP global"
            )
        ],
        [
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ's ᴛᴏᴘ 10", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴘᴇʀsᴏɴᴀʟ ᴛᴏᴘ 10", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"], callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"], callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text=_["P_B_2"], callback_data="play_playlist b"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"], callback_data="home_play"
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ɢʟᴏʙᴀʟ ᴛᴏᴘ 10", callback_data="SERVERTOP Global"
            )
        ],
        [
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ's ᴛᴏᴘ 10", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴘᴇʀsᴏɴᴀʟ ᴛᴏᴘ 10", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"], callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["PL_B_7"],
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl

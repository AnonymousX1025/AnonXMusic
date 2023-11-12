from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


def botplaylist_markup(_):
    return [
        [
            InlineKeyboardButton(text=_["S_B_9"], url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]


def close_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )


def supp_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_9"],
                    url=SUPPORT_CHAT,
                ),
            ]
        ]
    )

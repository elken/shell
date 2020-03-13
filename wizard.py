from gi.repository import Gio
from os import path
import json
from getopt import getopt, GetoptError
from sys import argv, exit

VI_LEFT = "h"
VI_DOWN = "j"
VI_UP = "k"
VI_RIGHT = "l"

KEYS_GNOME_WM = "org.gnome.desktop.wm.keybindings"
KEYS_GNOME_SHELL = "org.gnome.shell.keybindings"
KEYS_MUTTER = "org.gnome.mutter.keybindings"
KEYS_MEDIA = "org.gnome.settings-daemon.plugins.media-keys"
KEYS_MUTTER_WAYLAND = "org.gnome.mutter.wayland.keybindings"

SETTINGS_GNOME_WM = Gio.Settings.new(KEYS_GNOME_WM)
SETTINGS_GNOME_SHELL = Gio.Settings.new(KEYS_GNOME_SHELL)
SETTINGS_MUTTER = Gio.Settings.new(KEYS_MUTTER)
SETTINGS_MEDIA = Gio.Settings.new(KEYS_MEDIA)
SETTINGS_MUTTER_WAYLAND = Gio.Settings.new(KEYS_MUTTER_WAYLAND)


def red(inputString): return "\033[91m {}\033[00m".format(inputString)


def green(inputString): return "\033[92m {}\033[00m".format(inputString)


def yellow(inputString): return "\033[93m {}\033[00m".format(inputString)


def lightPurple(inputString): return "\033[94m {}\033[00m".format(inputString)


def purple(inputString): return "\033[95m {}\033[00m".format(inputString)


def cyan(inputString): return "\033[96m {}\033[00m".format(inputString)


def lightGray(inputString): return "\033[97m {}\033[00m".format(inputString)


def black(inputString): return "\033[98m {}\033[00m".format(inputString)


settings = {
    "restore-shortcuts": {
        "current_setting": SETTINGS_MUTTER_WAYLAND.get_strv("restore-shortcuts"),
        "new_setting": []
    },
    "minimize": {
        "current_setting": SETTINGS_GNOME_WM.get_strv("minimize"),
        "new_setting": []
    },
    "open-application-menu": {
        "current_setting": SETTINGS_GNOME_SHELL.get_strv("open-application-menu"),
        "new_setting": []
    },
    "switch-to-workspace-left": {
        "current_setting": SETTINGS_GNOME_WM.get_strv("switch-to-workspace-left"),
        "new_setting": []
    },
    "switch-to-workspace-right": {
        "current_setting": SETTINGS_GNOME_WM.get_strv("switch-to-workspace-right"),
        "new_setting": []
    },
    "switch-to-workspace-up": {
        "current_setting": SETTINGS_GNOME_WM.get_strv("switch-to-workspace-up"),
        "new_setting": ["<Primary><Super>Up", "<Primary><Super>{0}".format(VI_UP)]
    },
    "switch-to-workspace-down": {
        "current_setting": SETTINGS_GNOME_WM.get_strv("switch-to-workspace-down"),
        "new_setting": ["<Primary><Super>Down", "<Primary><Super>{0}".format(VI_DOWN)]
    },
    "move-to-monitor-left": {
        "current_setting": SETTINGS_GNOME_WM.get_strv("move-to-monitor-left"),
        "new_setting": ["<Shift><Super>Left", "<Shift><Super>{0}".format(VI_LEFT)]
    },
    "move-to-monitor-down": {
        "current_setting": SETTINGS_GNOME_WM.get_strv("move-to-monitor-down"),
        "new_setting": ["<Shift><Super>Down", "<Shift><Super>{0}".format(VI_DOWN)]
    },
    "move-to-monitor-up": {
        "current_setting": SETTINGS_GNOME_WM.get_strv("move-to-monitor-up"),
        "new_setting": ["<Shift><Super>Up", "<Shift><Super>{0}".format(VI_UP)]
    },
    "move-to-monitor-right": {
        "current_setting": SETTINGS_GNOME_WM.get_strv("move-to-monitor-left"),
        "new_setting": ["<Shift><Super>Right", "<Shift><Super>{0}".format(VI_RIGHT)]
    },
    "toggle-tiled-left": {
        "current_setting": SETTINGS_MUTTER.get_strv("toggle-tiled-left"),
        "new_setting": []
    },
    "toggle-tiled-right": {
        "current_setting": SETTINGS_MUTTER.get_strv("toggle-tiled-right"),
        "new_setting": []
    },
    "toggle-maximized": {
        "current_setting": SETTINGS_GNOME_WM.get_strv("toggle-maximized"),
        "new_setting": ["<Super>m"]
    },
    "screensaver": {
        "current_setting": SETTINGS_MEDIA.get_strv("screensaver"),
        "new_setting": ['<Super>Escape']
    },
    "home": {
        "current_setting": SETTINGS_MEDIA.get_strv("home"),
        "new_setting": ['<Super>f']
    },
    "email": {
        "current_setting": SETTINGS_MEDIA.get_strv("email"),
        "new_setting": ['<Super>e']
    },
    "www": {
        "current_setting": SETTINGS_MEDIA.get_strv("www"),
        "new_setting": ['<Super>b']
    },
    "rotate-video-lock-static": {
        "current_setting": SETTINGS_MEDIA.get_strv("rotate-video-lock-static"),
        "new_setting": []
    },
    "close": {
        "current_setting": SETTINGS_GNOME_WM.get_strv("close"),
        "new_setting": ['<Super>q']
    }
}

# print(lightPurple("The following settings are going to be changed:\n"))
MAX_SETTING_NAME_LENGTH = len(max(settings.keys(), key=len))
MAX_SETTING_LENGTH = len(
    max(settings, key=lambda x: settings[x]["current_setting"]))

# if not path.exists('.wizard_defaults'):
#     print(cyan('No defaults defined, saving the following settings as defaults'))
#     defaults = {}
#     for key, val in settings.items():
#         key_gap = ''.ljust(MAX_SETTING_NAME_LENGTH - len(key) + 1)
#         print("{0}: {1}{2}".format(yellow(key),
#                                    key_gap, green(val["current_setting"])))
#         defaults[key] = val["current_setting"]
#     with open('.wizard_defaults', 'w') as json_file:
#         json.dump(defaults, json_file)

#     # for key, val in settings.items():
#     #     if (val["current_setting"] != val["new_setting"]):

#     #         key_gap = ''.ljust(MAX_SETTING_NAME_LENGTH - len(key) + 1)
#     #         current_gap = ''.rjust(MAX_SETTING_LENGTH -
#     #                                len(str(val["current_setting"])) + 1)

#     #         print("{0}: {1}{2}{3}-> {4}".format(yellow(key),
#     #                                             key_gap,
#     #                                             red(val["current_setting"]),
#     #                                             current_gap,
#     #                                             green(val["new_setting"])))


def rebuild():
    print("rebuild")


def defaults():
    if not path.exists('.wizard_defaults'):
        print(red("No defaults configured"))
        exit(1)
    else:
        with open('.wizard_defaults', 'r') as json_file:
            defaults = json.load(json_file)
            print(lightGray("Current Defaults\n"))
            for key, val in defaults.items():
                key_gap = ''.ljust(MAX_SETTING_NAME_LENGTH - len(key) + 1)
                print("{0}: {1}{2}".format(yellow(key),
                                           key_gap, green(val)))


def reset():
    if not path.exists('.wizard_defaults'):
        print(red("No defaults configured"))
        exit(1)
    else:
        with open('.wizard_defaults', 'r') as json_file:
            defaults = json.load(json_file)


def overwrite():
    print(cyan("Saving the following settings as defaults"))
    defaults = {}
    for key, val in settings.items():
        key_gap = ''.ljust(MAX_SETTING_NAME_LENGTH - len(key) + 1)
        print("{0}: {1}{2}".format(yellow(key),
                                   key_gap, green(val["current_setting"])))
        defaults[key] = val["current_setting"]
    with open('.wizard_defaults', 'w') as json_file:
        json.dump(defaults, json_file)


help_text = """
{0}
Simple script to help manage the shortcuts necessary for the extension.

Usage:
    {0} <option>

Options:
    -h --help       Show this screen.
    -b --rebuild    Rebuild the extension
    -d --defaults   Print the current defaults (if configured)
    -r --reset      Reset the current settings back to defaults (if configured)
    -o --overwrite  Overwrite the old defaults with current settings
""".format(path.basename(argv[0]))

if __name__ == "__main__":
    raw_args = argv[1:]
    if len(argv) == 1:
        print(help_text)
    try:
        opts, args = getopt(
            raw_args, "hbrdo", ["help", "rebuild", "defaults", "reset", "overwrite"])
    except GetoptError:
        print(help_text)
        exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help_text)
            exit()
        elif opt in ("-b", "--rebuild"):
            rebuild()
        elif opt in ("-d", "--defaults"):
            defaults()
        elif opt in ("-r", "--reset"):
            reset()
        elif opt in ("-o", "--overwrite"):
            overwrite()

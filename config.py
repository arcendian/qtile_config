#!/usr/bin/env python

from libqtile.bar import Bar
from libqtile.config import Click, Drag, DropDown, Group
from libqtile.config import Key, Match, ScratchPad, Screen
from libqtile.layout.columns import Columns
from libqtile.layout.floating import Floating
from libqtile.layout.max import Max
from libqtile.layout.stack import Stack
from libqtile.layout.xmonad import MonadTall

from libqtile.lazy import lazy

from libqtile.widget.battery import Battery
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayoutIcon
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.spacer import Spacer
from libqtile.widget.volume import Volume
from libqtile.widget.wlan import Wlan

from qcolors import nordlike

mod = "mod4"
terminal = "alacritty"

keys = [
    Key(
        [mod],
        "h",
        lazy.layout.left(),
        desc="Move focus to left",
    ),
    Key(
        [mod],
        "l",
        lazy.layout.right(),
        desc="Move focus to right",
    ),
    Key(
        [mod],
        "j",
        lazy.layout.down(),
        desc="Move focus down",
    ),
    Key(
        [mod],
        "k",
        lazy.layout.up(),
        desc="Move focus up",
    ),
    Key(
        [mod],
        "space",
        lazy.layout.next(),
        desc="Move window focus to other window",
    ),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down",
    ),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        desc="Move window up",
    ),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, "control"],
        "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    Key(
        [mod, "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.grow_down(),
        desc="Grow window down",
    ),
    Key(
        [mod, "control"],
        "k",
        lazy.layout.grow_up(),
        desc="Grow window up",
    ),
    Key(
        [mod],
        "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes",
    ),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key(
        [mod],
        "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts",
    ),
    Key(
        [mod],
        "w",
        lazy.window.kill(),
        desc="Kill focused window",
    ),
    Key(
        [mod, "control"],
        "r",
        lazy.reload_config(),
        desc="Reload the config",
    ),
    Key(
        [mod, "control"],
        "q",
        lazy.shutdown(),
        desc="Shutdown Qtile",
    ),
    Key(
        [mod],
        "Return",
        lazy.spawn(terminal),
        desc="Launch terminal",
    ),
    Key(
        [mod, "shift"],
        "e",
        lazy.spawn("start-emacs"),
        desc="Launch rofi menu for emacs stuff",
    ),
    Key(
        [mod],
        "e",
        lazy.spawn("emacsclient -c -a 'emacs'"),
        desc="Launch emacsclient",
    ),
    Key(
        [mod, "shift"],
        "b",
        lazy.spawn("brave"),
        desc="Launch web browser",
    ),
    Key(
        [mod],
        "b",
        lazy.hide_show_bar(),
        desc="Toggle visibility of the bar",
    ),
    # IO control stuff
    Key(
        [],
        "Print",
        lazy.spawn("flameshot gui"),
        desc="Launch screenshot program",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer -q sset PCM,0 1+ unmute"),
        desc="Increase audio volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer -q sset PCM,0 1- unmute"),
        desc="Decrease audio volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("amixer -q sset PCM,0 toggle"),
        desc="Mute out audio volume",
    ),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +5%"),
        desc="Increase display brightness",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 5%-"),
        desc="Decrease display brightness",
    ),
    Key(
        [mod, "shift"],
        "c",
        lazy.spawn("changewallpaper"),
        desc="Decrease display brightness",
    ),
    Key(
        [mod, "shift"],
        "q",
        lazy.spawn("dm-powermenu"),
        desc="Launch power menu",
    ),
    Key(
        [mod, "shift"],
        "o",
        lazy.spawn("dmopen"),
        desc="Launch dmenu file opener",
    ),
    Key(
        [mod, "shift"],
        "p",
        lazy.spawn("passmenu"),
        desc="Get password from password manager",
    ),
    Key(
        [mod],
        "p",
        lazy.spawn("rofi -show run"),
        desc="Launch run menu",
    ),
]

groups = [
    Group(
        "1",
        label="",
        layout="columns",
    ),
    Group(
        "2",
        label="",
        layout="columns",
    ),
    Group(
        "3",
        label="",
        layout="columns",
    ),
    Group(
        "4",
        label="",
        layout="stack",
    ),
    Group(
        "5",
        label="",
        layout="columns",
    ),
    Group(
        "6",
        label="",
        layout="columns",
    ),
    Group(
        "7",
        label="",
        layout="columns",
    ),
    Group(
        "8",
        label="",
        layout="columns",
        matches=[
            Match(wm_class="pcmanfm-qt"),
        ],
    ),
    Group(
        "9",
        label="",
        layout="max",
        matches=[
            Match(wm_class="Emacs"),
        ],
    ),
    Group(
        "0",
        label="",
        layout="monadtall",
        matches=[
            Match(wm_class="Brave-browser"),
        ],
    ),
]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            Key(
                [mod, "control"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    Columns(
        border_normal=nordlike["dark-gray"],
        border_focus=nordlike["blue"],
        border_width=2,
        border_normal_stack=nordlike["dark-gray"],
        border_focus_stack=nordlike["cyan"],
        border_on_single=2,
        margin=10,
        margin_on_single=10,
    ),
    Max(
        border_normal=nordlike["dark-gray"],
        border_focus=nordlike["blue"],
        border_width=2,
        margin=0,
    ),
    MonadTall(
        border_normal=nordlike["dark-gray"],
        border_focus=nordlike["blue"],
        margin=10,
        border_width=2,
        single_border_width=2,
        single_margin=10,
    ),
    Stack(
        border_normal=nordlike["dark-gray"],
        border_focus=nordlike["blue"],
        border_width=2,
        num_stacks=1,
        margin=10,
    ),
]

widget_defaults = dict(
    font="JetBrains Mono Nerd Font",
    fontsize=15,
    padding=10,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=Bar(
            [
                CurrentLayoutIcon(
                    background=nordlike["blue"],
                    padding=3,
                ),
                Spacer(
                    length=10,
                ),
                Battery(
                    background=nordlike["magenta"],
                    full_char="",
                    charge_char="",
                    discharge_char="",
                    empty_char="",
                    show_short_text=False,
                    low_percentage=0.15,
                    notify_below=0.15,
                ),
                Spacer(
                    length=10,
                ),
                Clock(
                    background=nordlike["cyan"],
                    format=" %Y-%m-%d %a %I:%M %p",
                ),
                Spacer(
                    length=315,
                ),
                GroupBox(
                    disable_drag=True,
                    active=nordlike["orange"],
                    inactive=nordlike["fg_gutter"],
                    highlight_method="line",
                    block_highlight_text_color=nordlike["magenta"],
                    borderwidth=0,
                    highlight_color=nordlike["bg"],
                    background=nordlike["bg"],
                ),
                Spacer(
                    length=140,
                ),
                Volume(
                    background=nordlike["dark-orange"],
                    channel="PCM",
                    fmt="墳 {:3}",
                ),
                Spacer(
                    length=10,
                ),
                CPU(
                    format=" {freq_current}GHz {load_percent}%",
                    background=nordlike["dark-cyan"],
                ),
                Spacer(
                    length=10,
                ),
                Memory(
                    format=" {MemUsed:4.0f}{mm}/{MemTotal:4.0f}{mm}",
                    background=nordlike["dark-magenta"],
                ),
                Spacer(
                    length=10,
                ),
                Net(
                    background=nordlike["dark-blue"],
                    interface="enp1s0",
                    format=" {down} ↓↑ {up}",
                ),
                Wlan(
                    background=nordlike["dark-blue"],
                    disconnected_message="睊",
                    interface="wlp0s20f3",
                    format="直 {percent:2.0%}",
                ),
            ],
            margin=[10, 10, 5, 10],
            background="#0000000F",
            opacity=1,
            size=25,
        )
    ),
]

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                "alacritty",
                width=0.4,
                height=0.5,
                x=0.3,
                y=0.1,
                opacity=0.8,
            ),
            DropDown(
                "ncmpcpp",
                "kitty -e ncmpcpp",
                width=0.4,
                height=0.6,
                x=0.3,
                y=0.1,
                opacity=0.8,
            ),
        ],
    )
)

# extend keys list with keybinding for scratchpad
keys.extend(
    [
        Key(
            [mod, "mod1"],
            "1",
            lazy.group["scratchpad"].dropdown_toggle("term"),
        ),
        Key(
            [mod, "mod1"],
            "2",
            lazy.group["scratchpad"].dropdown_toggle("ncmpcpp"),
        ),
    ]
)

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = Floating(
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
        Match(wm_class="Pinentry-gtk-2"),
    ],
    border_focus=nordlike["blue"],
    border_normal=nordlike["gray"],
    border_width=2,
)
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"

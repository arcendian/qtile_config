# -----------------------------------------------------------------------------------------
# IMPORTS
from libqtile import bar, widget
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy

# layouts
from libqtile.layout.columns import Columns
from libqtile.layout.xmonad import MonadTall
from libqtile.layout.stack import Stack
from libqtile.layout.floating import Floating

# custom colors
from qcolors import nordfox

# -----------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------
# Set modifier key and default terminal emulator
mod = "mod4"
terminal = "alacritty"
# -----------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------
# KEYBINDINGS
keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
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
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Launch programs
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "e", lazy.spawn("start-emacs"), desc="Launch emacsclient"),
    Key([mod, "shift"], "b", lazy.spawn("brave"), desc="Launch web browser"),
    Key([mod], "b", lazy.hide_show_bar(), desc="Toggle visibility of the bar"),
    # IO control stuff
    Key([mod], "Print", lazy.spawn("flameshot gui"), desc="Launch screenshot program"),
    Key(
        [mod],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer -q sset PCM,0 1+ unmute"),
        desc="Increase audio volume",
    ),
    Key(
        [mod],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer -q sset PCM,0 1- unmute"),
        desc="Decrease audi volume",
    ),
    Key(
        [mod],
        "XF86AudioMute",
        lazy.spawn("amixer -q sset PCM,0 1- unmute"),
        desc="Mute out audio volume",
    ),
    Key(
        [mod],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +5%"),
        desc="Increase display brightness",
    ),
    Key(
        [mod],
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
    Key([mod, "shift"], "q", lazy.spawn("dm-powermenu"), desc="Launch power menu"),
    Key([mod], "p", lazy.spawn("rofi -show run"), desc="Launch run menu"),
]

groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
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
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# LAYOUTS
layouts = [
    Columns(
        border_normal=nordfox["dark-gray"],
        border_focus=nordfox["blue"],
        border_width=2,
        border_normal_stack=nordfox["dark-gray"],
        border_focus_stack=nordfox["cyan"],
        border_on_single=2,
        margin=10,
        margin_on_single=10,
    ),
    MonadTall(
        border_normal=nordfox["dark-gray"],
        border_focus=nordfox["blue"],
        margin=10,
        border_width=2,
        single_border_width=2,
        single_margin=10,
    ),
    Stack(
        border_normal=nordfox["dark-gray"],
        border_focus=nordfox["blue"],
        border_width=2,
        num_stacks=1,
        margin=10,
    ),
]
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# WIDGETS
widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#b988b0", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
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

# Append scratchpad with dropdowns to groups
groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term", "alacritty", width=0.4, height=0.5, x=0.3, y=0.1, opacity=1
            ),
            DropDown(
                "ncmpcpp",
                "kitty -e ncmpcpp",
                width=0.4,
                height=0.6,
                x=0.3,
                y=0.1,
                opacity=1,
            ),
            # DropDown('pomo', 'pomotroid', x=0.4, y=0.2, opacity=1),
            # DropDown('bitwarden', 'bitwarden-desktop',
            #          width=0.4, height=0.6, x=0.3, y=0.1, opacity=1),
        ],
    )
)
# extend keys list with keybinding for scratchpad
keys.extend(
    [
        Key([mod, "mod1"], "1", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key([mod, "mod1"], "2", lazy.group["scratchpad"].dropdown_toggle("ncmpcpp")),
        # Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('pomo')),
        # Key(["control"], "4", lazy.group['scratchpad'].dropdown_toggle('bitwarden')),
    ]
)
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# OTHERS
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"

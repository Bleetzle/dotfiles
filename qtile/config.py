import os
import subprocess
from libqtile import hook
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration

mod = "mod4"
terminal = "kitty"
wmname = "qtile"
browser = "librewolf"
alt = "mod1"
home = os.path.expanduser('~')
nightmode = False

# [Colours]
dark_red = '#800F0F'
bg_colour = '#111318'
gold = '#FFB238'
bright_red = '#E73131'
white = '#E6E6E6'

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "k", lazy.layout.grow(), desc="Grow window"),
    Key([mod, "control"], "j", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod, "control"], "h", lazy.window.resize_floating(20,20), desc="Grow floating window"),
    Key([mod, "control"], "l", lazy.window.resize_floating(-20,-20), desc="Shrink floating window"),
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
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawn("rofi -combi-modi window#drun -show combi -theme ~/.config/rofi/style-3.rasi"), desc="Spawn a command using a prompt widget"),
    Key([mod], "c", lazy.spawn(browser), desc="Spawn a browser"),
    Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer -d set Master 5%+")),
    #Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer -c 0 -q set Master 2dB+")),
    #Key([], "XF86AudioLowerVolume",lazy.spawn("amixer -c 0 -q set Master 2dB-")),
    Key([], "XF86AudioLowerVolume",lazy.spawn("amixer -d set Master 5%-")),
    Key([], "XF86AudioMute",lazy.spawn("amixer -d set Master toggle")),
    Key([], "XF86MonBrightnessUp",lazy.spawn("xbacklight -inc 7")),
    Key([], "XF86MonBrightnessDown",lazy.spawn("xbacklight -dec 7")),
    Key([], "Print",lazy.spawn("flameshot full"),desc="Normal Screenshot"),
    Key([mod], "Print",lazy.spawn("flameshot launcher"),desc="Special Screenshot"),
    Key([], "XF86TouchpadToggle",lazy.spawn("redshift -O 2000K"),desc="Touchpad Toggle"),
    Key([mod], "p",lazy.spawn("betterlockscreen --lock"),desc="screen key next to home"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"), 
    Key([mod], "i", lazy.window.toggle_floating(), desc="Toggle floating mode for a window"),
]


groups = [Group(f"{i+1}", label=" ") for i in range(4)]

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
                ]
            )





layouts = [
    #layout.Columns(border_focus_stack=["#E73131", "#E73131"], border_width=1,margin=7),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    #layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(border_focus_stack=["#E73131", "#E73131"], border_width=1,margin=10),
    # layout.MonadWide(),
    layout.Max(),
    #layout.RatioTile(),
    # layout.Tile(),
   # layout.TreeTab(),
    # layout.VerticalTile(),
   # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=14,
    padding=10,
    )
extension_defaults = widget_defaults.copy()

decoration_group = {
    "decorations": [
        RectDecoration(colour=bg_colour,radius=15, filled=True, group=True,clip=True), 
        ],
}

screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayoutIcon(),
                widget.GroupBox(
                    borderwidth=3,
                    highlight_method='block',
                    active=dark_red,
                    block_highlight_text_color=gold,
                    highlight_color=dark_red,
                    inactive=white,
                    this_current_screen_border=dark_red,
                    rounded=True,
                    disable_drag=True,
                    **decoration_group
                ),
                #widget.WindowName(),
                widget.Spacer(length=5),
                widget.TextBox(
                    text="",
                    foreground=gold,
                    **decoration_group,
                    ),
                widget.CPU(format='{load_percent}%',**decoration_group),
                widget.TextBox(text="",foreground=gold,**decoration_group),
                widget.ThermalSensor(format='{temp:.0f}{unit}',update_interval=10,**decoration_group),
                widget.TextBox(text="﬙",foreground=gold,**decoration_group),
                widget.Memory(format='{MemUsed: .0f}{mm}',measure_mem='G',**decoration_group),
                widget.Spacer(),
                widget.Systray(),
                widget.OpenWeather(location='London',
                                   format='{icon} {main_temp} °{units_temperature} {weather_details}',
                                   **decoration_group,
                                   ),
                widget.Spacer(),
                #widget.Visualiser(bar_colour=gold,bar_height=40,hide=True,**decoration_group),
                widget.WiFiIcon(active_colour=gold,disconnected_colour=bright_red,**decoration_group),
                #widget.Wlan(
                #    format='{essid}',
                #    disconnected_message='睊',
                #    foreground=gold,
                #    **decoration_group,
                #    ),
                widget.Net(format=' {down}    {up}',prefix='M',**decoration_group),
                widget.Spacer(length=5),
                widget.TextBox(text="",foreground=gold,**decoration_group),
                widget.Volume(**decoration_group),
                widget.Spacer(length=5),
                #widget.TextBox(text="",foreground=gold,**decoration_group),
                widget.UPowerWidget(border_colour=gold,
                                    border_critical_colour=bright_red,
                                    fill_critical=bright_red,
                                    fill_low=dark_red,
                                    fill_normal=gold,
                                    margin=10,
                                    **decoration_group),
                widget.Battery(
                    low_percentage=0.10,
                    format='{char}  {percent:2.0%}',
                    discharge_char='',
                    charge_char='',
                    **decoration_group,
                    ),
                widget.Spacer(length=5),
                widget.Clock(format="  %X",foreground=gold,**decoration_group),
                widget.Clock(format="  %d/%m/%Y",**decoration_group),
            ],
            30,margin=[10,10,0,10],background="#00000000",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
          #  border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
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
auto_minimize = True

wl_input_rules = None


@hook.subscribe.startup_once
def autostart():
    homeStart = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([homeStart])


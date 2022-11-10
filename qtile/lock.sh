#!/bin/sh

BLANK='#00000000'
CLEAR='#ffffff22'
DEFAULT='#e73131ff'
TEXT='#e1e1e1ee'
WRONG='#111318ff'
VERIFYING='#111318bb'

i3lock \
--color=$WRONG      \
--insidever-color=$CLEAR     \
--ringver-color=$VERIFYING   \
\
--insidewrong-color=$CLEAR   \
--ringwrong-color=$WRONG     \
\
--inside-color=$BLANK        \
--ring-color=$DEFAULT        \
--line-color=$BLANK          \
--separator-color=$DEFAULT   \
\
--verif-color=$TEXT          \
--wrong-color=$TEXT          \
--time-color=$TEXT           \
--date-color=$TEXT           \
--layout-color=$TEXT         \
--keyhl-color=$WRONG         \
\
--greeter-text="Welcome Back"      \
--verif-text="CHECKING"      \
--wrong-text="ERROR!!!"      \
--date-size=27.0      \
--time-size=27.0      \
--wrong-size=27.0      \
--verif-size=27.0      \
\
--screen 1                   \
--ring-width 20.0            \
--radius 180                 \
--clock                      \
--indicator                  \
--pass-volume-keys                  \
--pass-power-keys                  \
--pass-screen-keys                  \
--time-str="%H:%M:%S"        \
--date-str="%A, %Y-%m-%d"       \

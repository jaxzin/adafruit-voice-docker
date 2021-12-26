# SPDX-FileCopyrightText: 2021 scivision for soothingsounds
# SPDX-License-Identifier: Apache-2.0
# Changes: Added exit handler and support for looping sounds

from time import sleep
import soothingsounds as ss
from argparse import ArgumentParser
import signal

soundmod = "sounddevice"  # 'pygame'#'pyglet'#'pyaudio' #'pygame' #'scikits.audiolab'

nbitfile = 16
nbitfloat = 32  # from generator.py

# Setup exit handler
kill_now = False
def exit_handler(signum, frame):
    kill_now = True

signal.signal(signal.SIGINT, exit_handler)
signal.signal(signal.SIGTERM, exit_handler)

def main():
    P = ArgumentParser(
        description="noise generation program for Raspberry Pi or any Python-capable computer"
    )
    P.add_argument(
        "nmode",
        help="what type of white noise [white, pink, brown...]",
        nargs="?",
        default="white",
    )
    P.add_argument(
        "hours",
        help="how many hours do you want sound generated for [default=1 hour]",
        type=float,
        nargs="?",
        default=1,
    )
    P.add_argument(
        "-fs", help="sampling freq e.g. 16000 or 44100", type=int, default=16000
    )
    P.add_argument(
        "-nsec",
        help="length of unique noise sequence [seconds]",
        type=float,
        default=60,
    )
    p = P.parse_args()

    samps = ss.computenoise(p.nmode, p.fs, p.nsec, nbitfloat, nbitfile)

    while not kill_now:
        ss.liveplay(samps, p.hours, p.fs, p.nsec, soundmod)
        sleep(p.hours * 3600)  # for async playback, else sound doesn't play

if __name__ == "__main__":
    main()



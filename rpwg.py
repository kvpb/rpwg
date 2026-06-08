#!/usr/bin/env python3

import sys
import getopt
import re
import random
import secrets

class ANSIES: # ANSI escape sequences
  # SGR parameters
  reset = "\x1B[0m" # reset or normal
  bold = "\x1B[1m" # bold or increased intensity
  dim = "\x1B[2m" # faint, decreased density or dim
  italic = "\x1B[3m" # italic
  underline = "\x1B[4m" # underline
  slowblink = "\x1B[5m" # slow blink
  rapidblink = "\x1B[6m" # rapid blink
  invert = "\x1B[7m" # reverse video or invert
  hide = "\x1B[8m" # conceal or hide
  strike = "\x1B[9m" # crossed-out or strike
  defaultfont = "\x1B[10m" # primary (default) font
  alternativefont1 = "\x1B[11m" # alternative font
  alternativefont2 = "\x1B[12m" # alternative font
  alternativefont3 = "\x1B[13m" # alternative font
  alternativefont4 = "\x1B[14m" # alternative font
  alternativefont5 = "\x1B[15m" # alternative font
  alternativefont6 = "\x1B[16m" # alternative font
  alternativefont7 = "\x1B[17m" # alternative font
  alternativefont8 = "\x1B[18m" # alternative font
  alternativefont9 = "\x1B[19m" # alternative font
  Fraktur = "\x1B[20m" # Fraktur (Gothic)
  doublyunderlined = "\x1B[21m" # doubly underlined or not bold
  normalintensity = "\x1B[22m" # normal intensity
  neitheritalicnorblackletter = "\x1B[23m" # neither italic nor blackletter
  notunderlined = "\x1B[24m" # not underlined
  notblinking = "\x1B[25m" # not blinking
  proportionalspacing = "\x1B[26m" # proportional spacing
  notreversed = "\x1B[27m" # not reversed
  reveal = "\x1B[28m" # 
  notcrossedout = "\x1B[29m" # not crossed out
  foregroundcolor1 = "\x1B[30m" # set foreground color
  foregroundcolor2 = "\x1B[31m" # set foreground color
  foregroundcolor3 = "\x1B[32m" # set foreground color
  foregroundcolor4 = "\x1B[33m" # set foreground color
  foregroundcolor5 = "\x1B[34m" # set foreground color
  foregroundcolor6 = "\x1B[35m" # set foreground color
  foregroundcolor7 = "\x1B[36m" # set foreground color
  foregroundcolor8 = "\x1B[37m" # set foreground color
  foregroundcolor9 = "\x1B[38m" # set foreground color, next arguments are 5;n or 2;r;g;b
  foregroundcolor0 = "\x1B[39m" # default foreground color
  backgroundcolor1 = "\x1B[40m" # set background color
  backgroundcolor2 = "\x1B[41m" # set background color
  backgroundcolor3 = "\x1B[42m" # set background color
  backgroundcolor4 = "\x1B[43m" # set background color
  backgroundcolor5 = "\x1B[44m" # set background color
  backgroundcolor6 = "\x1B[45m" # set background color
  backgroundcolor7 = "\x1B[46m" # set background color
  backgroundcolor8 = "\x1B[47m" # set background color
  backgroundcolor9 = "\x1B[48m" # set background color, next arguments are 5;n or 2;r;g;b
  backgroundcolor0 = "\x1B[49m" # default background color
  disableproportionalspacing = "\x1B[50m" # disable proportional spacing
  framed = "\x1B[51m" # framed
  encircled = "\x1B[52m" # encircled
  overlined = "\x1B[53m" # overlined
  neitherframednorencircled = "\x1B[54m" # neither framed nor encircled
  notoverlined = "\x1B[55m" # not overlined
  underlinecolor9 = "\x1B[58m" # set underline color, next arguments are 5;n or 2;r;g;b
  underlinecolor0 = "\x1B[59m" # default underline color
  rightsideline = "\x1B[60m" # ideogram underline or right side line
  doublerightsideline = "\x1B[61m" # ideogram double underline or double line on the right side
  leftsideline = "\x1B[62m" # ideogram overline or left side line
  doubleleftsideline = "\x1B[63m" # ideogram double overline or double line on the left side
  ideogramstressmarking = "\x1B[64m" # ideogram stress marking
  noideogramattributes = "\x1B[65m" # no ideogram attributes
  superscript = "\x1B[73m" # superscript
  subscript = "\x1B[74m" # subscript
  neithersuperscriptnorsubscript = "\x1B[75m" # neither superscript nor subscript
  brightforegroundcolor0 = "\x1B[90m" # set bright foreground color
  brightforegroundcolor1 = "\x1B[91m" # set bright foreground color
  brightforegroundcolor2 = "\x1B[92m" # set bright foreground color
  brightforegroundcolor3 = "\x1B[93m" # set bright foreground color
  brightforegroundcolor4 = "\x1B[94m" # set bright foreground color
  brightforegroundcolor5 = "\x1B[95m" # set bright foreground color
  brightforegroundcolor6 = "\x1B[96m" # set bright foreground color
  brightforegroundcolor7 = "\x1B[97m" # set bright foreground color
  brightbackgroundcolor0 = "\x1B[100m" # set bright background color
  brightbackgroundcolor1 = "\x1B[101m" # set bright background color
  brightbackgroundcolor2 = "\x1B[102m" # set bright background color
  brightbackgroundcolor3 = "\x1B[103m" # set bright background color
  brightbackgroundcolor4 = "\x1B[104m" # set bright background color
  brightbackgroundcolor5 = "\x1B[105m" # set bright background color
  brightbackgroundcolor6 = "\x1B[106m" # set bright background color
  brightbackgroundcolor7 = "\x1B[107m" # set bright background color
  # 3- and 4-bit colors
  # = "\x1B[m" # 
  # 8-bit colors
  # = "\x1B[m" # 
  # 24-bit colors
  # = "\x1B[m" # 
  
  def disable( self ):
    self.reset = ""
    self.bold = ""
    self.dim = ""
    self.italic = ""
    self.underline = ""
    self.slowblink = ""
    self.rapidblink = ""
    self.invert = ""
    self.hide = ""
    self.strike = ""
    self.defaultfont = ""
    self.alternativefont1 = ""
    self.alternativefont2 = ""
    self.alternativefont3 = ""
    self.alternativefont4 = ""
    self.alternativefont5 = ""
    self.alternativefont6 = ""
    self.alternativefont7 = ""
    self.alternativefont8 = ""
    self.alternativefont9 = ""
    self.Fraktur = ""
    self.doublyunderlined = ""
    self.normalintensity = ""
    self.neitheritalicnorblackletter = ""
    self.notunderlined = ""
    self.notblinking = ""
    self.proportionalspacing = ""
    self.notreversed = ""
    self.reveal = ""
    self.notcrossedout = ""
    self.foregroundcolor1 = ""
    self.foregroundcolor2 = ""
    self.foregroundcolor3 = ""
    self.foregroundcolor4 = ""
    self.foregroundcolor5 = ""
    self.foregroundcolor6 = ""
    self.foregroundcolor7 = ""
    self.foregroundcolor8 = ""
    self.foregroundcolor9 = ""
    self.foregroundcolor0 = ""
    self.backgroundcolor1 = ""
    self.backgroundcolor2 = ""
    self.backgroundcolor3 = ""
    self.backgroundcolor4 = ""
    self.backgroundcolor5 = ""
    self.backgroundcolor6 = ""
    self.backgroundcolor7 = ""
    self.backgroundcolor8 = ""
    self.backgroundcolor9 = ""
    self.backgroundcolor0 = ""
    self.disableproportionalspacing = ""
    self.framed = ""
    self.encircled = ""
    self.overlined = ""
    self.neitherframednorencircled = ""
    self.notoverlined = ""
    self.underlinecolor9 = ""
    self.underlinecolor0 = ""
    self.rightsideline = ""
    self.doublerightsideline = ""
    self.leftsideline = ""
    self.doubleleftsideline = ""
    self.ideogramstressmarking = ""
    self.noideogramattributes = ""
    self.superscript = ""
    self.subscript = ""
    self.neithersuperscriptnorsubscript = ""
    self.brightforegroundcolor0 = ""
    self.brightforegroundcolor1 = ""
    self.brightforegroundcolor2 = ""
    self.brightforegroundcolor3 = ""
    self.brightforegroundcolor4 = ""
    self.brightforegroundcolor5 = ""
    self.brightforegroundcolor6 = ""
    self.brightforegroundcolor7 = ""
    self.brightbackgroundcolor0 = ""
    self.brightbackgroundcolor1 = ""
    self.brightbackgroundcolor2 = ""
    self.brightbackgroundcolor3 = ""
    self.brightbackgroundcolor4 = ""
    self.brightbackgroundcolor5 = ""
    self.brightbackgroundcolor6 = ""
    self.brightbackgroundcolor7 = ""

set_character = [
   '!',
   '$',
   '%',
   '&',
  '\'',
   '(',
   ')',
   '*',
   '+',
   ',',
   '-',
   '.',
   '/',
   '0',
   '1',
   '2',
   '3',
   '4',
   '5',
   '6',
   '7',
   '8',
   '9',
   ':',
   ';',
   '<',
   '=',
   '>',
   '?',
   '@',
   'A',
   'B',
   'C',
   'D',
   'E',
   'F',
   'G',
   'H',
   'I',
   'J',
   'K',
   'L',
   'M',
   'N',
   'O',
   'P',
   'Q',
   'R',
   'S',
   'T',
   'U',
   'V',
   'W',
   'X',
   'Y',
   'Z',
   '[',
   ']',
   '^',
   '_',
   '`',
   'a',
   'b',
   'c',
   'd',
   'e',
   'f',
   'g',
   'h',
   'i',
   'j',
   'k',
   'l',
   'm',
   'n',
   'o',
   'p',
   'q',
   'r',
   's',
   't',
   'u',
   'v',
   'w',
   'x',
   'y',
   'z',
   '{',
   '|',
   '}',
   '~',
] # in ASCII order, no 032, '"', '\' or '#'.
matrix_key = {
  "ANSI QWERTY": {
    "!": "AE01",
    "$": "AE04",
    "%": "AE05",
    "&": "AE07",
    "'": "AC11",
    "(": "AE09",
    ")": "AE10",
    "*": "AE08",
    "+": "AE12",
    ",": "AB08",
    "-": "AE11",
    ".": "AB09",
    "/": "AB10",
    "0": "AE10",
    "1": "AE01",
    "2": "AE02",
    "3": "AE03",
    "4": "AE04",
    "5": "AE05",
    "6": "AE06",
    "7": "AE07",
    "8": "AE08",
    "9": "AE09",
    ":": "AC10",
    ";": "AC10",
    "<": "AB08",
    "=": "AE12",
    ">": "AB09",
    "?": "AB10",
    "@": "AE02",
    "A": "AC01",
    "B": "AB05",
    "C": "AB03",
    "D": "AC03",
    "E": "AD03",
    "F": "AC04",
    "G": "AC05",
    "H": "AC06",
    "I": "AD08",
    "J": "AC07",
    "K": "AC08",
    "L": "AC09",
    "M": "AB07",
    "N": "AB06",
    "O": "AD09",
    "P": "AD10",
    "Q": "AD01",
    "R": "AD04",
    "S": "AC02",
    "T": "AD05",
    "U": "AD07",
    "V": "AB04",
    "W": "AD02",
    "X": "AB02",
    "Y": "AD06",
    "Z": "AB01",
    "[": "AD11",
    "]": "AD12",
    "^": "AE06",
    "_": "AE11",
    "`": "TLDE",
    "a": "AC01",
    "b": "AB05",
    "c": "AB03",
    "d": "AC03",
    "e": "AD03",
    "f": "AC04",
    "g": "AC05",
    "h": "AC06",
    "i": "AD08",
    "j": "AC07",
    "k": "AC08",
    "l": "AC09",
    "m": "AB07",
    "n": "AB06",
    "o": "AD09",
    "p": "AD10",
    "q": "AD01",
    "r": "AD04",
    "s": "AC02",
    "t": "AD05",
    "u": "AD07",
    "v": "AB04",
    "w": "AD02",
    "x": "AB02",
    "y": "AD06",
    "z": "AB01",
    "{": "AD11",
    "|": "BKSL",
    "}": "AD12",
    "~": "TLDE",
  },
  "Apple British": { # Apple GB QWERTY
    "!": "AE01",
    "$": "AE04",
    "%": "AE05",
    "&": "AE07",
    "'": "AC11",
    "(": "AE09",
    ")": "AE10",
    "*": "AE08",
    "+": "AE12",
    ",": "AB08",
    "-": "AE11",
    ".": "AB09",
    "/": "AB10",
    "0": "AE10",
    "1": "AE01",
    "2": "AE02",
    "3": "AE03",
    "4": "AE04",
    "5": "AE05",
    "6": "AE06",
    "7": "AE07",
    "8": "AE08",
    "9": "AE09",
    ":": "AC10",
    ";": "AC10",
    "<": "AB08",
    "=": "AE12",
    ">": "AB09",
    "?": "AB10",
    "@": "AE02",
    "A": "AC01",
    "B": "AB05",
    "C": "AB03",
    "D": "AC03",
    "E": "AD03",
    "F": "AC04",
    "G": "AC05",
    "H": "AC06",
    "I": "AD08",
    "J": "AC07",
    "K": "AC08",
    "L": "AC09",
    "M": "AB07",
    "N": "AB06",
    "O": "AD09",
    "P": "AD10",
    "Q": "AD01",
    "R": "AD04",
    "S": "AC02",
    "T": "AD05",
    "U": "AD07",
    "V": "AB04",
    "W": "AD02",
    "X": "AB02",
    "Y": "AD06",
    "Z": "AB01",
    "[": "AD11",
    "]": "AD12",
    "^": "AE06",
    "_": "AE11",
    "`": "TLDE",
    "a": "AC01",
    "b": "AB05",
    "c": "AB03",
    "d": "AC03",
    "e": "AD03",
    "f": "AC04",
    "g": "AC05",
    "h": "AC06",
    "i": "AD08",
    "j": "AC07",
    "k": "AC08",
    "l": "AC09",
    "m": "AB07",
    "n": "AB06",
    "o": "AD09",
    "p": "AD10",
    "q": "AD01",
    "r": "AD04",
    "s": "AC02",
    "t": "AD05",
    "u": "AD07",
    "v": "AB04",
    "w": "AD02",
    "x": "AB02",
    "y": "AD06",
    "z": "AB01",
    "{": "AD11",
    "|": "BKSL",
    "}": "AD12",
    "~": "TLDE",
  },
  "ISO QWERTY": {
    "!": "AE01",
    "$": "AE04",
    "%": "AE05",
    "&": "AE07",
    "'": "AC11",
    "(": "AE09",
    ")": "AE10",
    "*": "AE08",
    "+": "AE12",
    ",": "AB08",
    "-": "AE11",
    ".": "AB09",
    "/": "AB10",
    "0": "AE10",
    "1": "AE01",
    "2": "AE02",
    "3": "AE03",
    "4": "AE04",
    "5": "AE05",
    "6": "AE06",
    "7": "AE07",
    "8": "AE08",
    "9": "AE09",
    ":": "AC10",
    ";": "AC10",
    "<": "LSGT",
    "=": "AE12",
    ">": "LSGT",
    "?": "AB10",
    "@": "AE02",
    "A": "AC01",
    "B": "AB05",
    "C": "AB03",
    "D": "AC03",
    "E": "AD03",
    "F": "AC04",
    "G": "AC05",
    "H": "AC06",
    "I": "AD08",
    "J": "AC07",
    "K": "AC08",
    "L": "AC09",
    "M": "AB07",
    "N": "AB06",
    "O": "AD09",
    "P": "AD10",
    "Q": "AD01",
    "R": "AD04",
    "S": "AC02",
    "T": "AD05",
    "U": "AD07",
    "V": "AB04",
    "W": "AD02",
    "X": "AB02",
    "Y": "AD06",
    "Z": "AB01",
    "[": "AD11",
    "]": "AD12",
    "^": "AE06",
    "_": "AE11",
    "`": "TLDE",
    "a": "AC01",
    "b": "AB05",
    "c": "AB03",
    "d": "AC03",
    "e": "AD03",
    "f": "AC04",
    "g": "AC05",
    "h": "AC06",
    "i": "AD08",
    "j": "AC07",
    "k": "AC08",
    "l": "AC09",
    "m": "AB07",
    "n": "AB06",
    "o": "AD09",
    "p": "AD10",
    "q": "AD01",
    "r": "AD04",
    "s": "AC02",
    "t": "AD05",
    "u": "AD07",
    "v": "AB04",
    "w": "AD02",
    "x": "AB02",
    "y": "AD06",
    "z": "AB01",
    "{": "AD11",
    "|": "BKSL",
    "}": "AD12",
    "~": "TLDE",
  },
  "Apple French": { # Apple AZERTY
    "!": "AE08",
    "$": "AD12",
    "%": "AC11",
    "&": "AE01",
    "'": "AE04",
    "(": "AE05",
    ")": "AE11",
    "*": "AD12",
    "+": "AE13",
    ",": "AB08",
    "-": "AE12",
    ".": "AB09",
    "/": "AB10",
    "0": "AE10",
    "1": "AE01",
    "2": "AE02",
    "3": "AE03",
    "4": "AE04",
    "5": "AE05",
    "6": "AE06",
    "7": "AE07",
    "8": "AE08",
    "9": "AE09",
    ":": "AB10",
    ";": "AB09",
    "<": "LSGT",
    "=": "AE13",
    ">": "LSGT",
    "?": "AB08",
    "@": "TLDE",
    "A": "AD01",
    "B": "AB05",
    "C": "AB03",
    "D": "AC03",
    "E": "AD03",
    "F": "AC04",
    "G": "AC05",
    "H": "AC06",
    "I": "AD08",
    "J": "AC07",
    "K": "AC08",
    "L": "AC09",
    "M": "AC10",
    "N": "AB06",
    "O": "AD09",
    "P": "AD10",
    "Q": "AC01",
    "R": "AD04",
    "S": "AC02",
    "T": "AD05",
    "U": "AD07",
    "V": "AB04",
    "W": "AB01",
    "X": "AB02",
    "Y": "AD06",
    "Z": "AD02",
    "[": "AE05",
    "]": "AE11",
    "^": "AD11",
    "_": "AE12",
    "`": "BKSL",
    "a": "AD01",
    "b": "AB05",
    "c": "AB03",
    "d": "AC03",
    "e": "AD03",
    "f": "AC04",
    "g": "AC05",
    "h": "AC06",
    "i": "AD08",
    "j": "AC07",
    "k": "AC08",
    "l": "AC09",
    "m": "AC10",
    "n": "AB06",
    "o": "AD09",
    "p": "AD10",
    "q": "AC01",
    "r": "AD04",
    "s": "AC02",
    "t": "AD05",
    "u": "AD07",
    "v": "AB04",
    "w": "AB01",
    "x": "AB02",
    "y": "AD06",
    "z": "AD02",
    "{": "AE05",
    "|": "AC09",
    "}": "AE11",
    "~": "AB06",
  },
  "ISO AZERTY": {
    "!": "AB10",
    "$": "AD12",
    "%": "AC11",
    "&": "AE01",
    "'": "AE04",
    "(": "AE05",
    ")": "AE11",
    "*": "BKSL",
    "+": "AE12",
    ",": "AB08",
    "-": "AE06",
    ".": "AB09",
    "/": "AB10",
    "0": "AE10",
    "1": "AE01",
    "2": "AE02",
    "3": "AE03",
    "4": "AE04",
    "5": "AE05",
    "6": "AE06",
    "7": "AE07",
    "8": "AE08",
    "9": "AE09",
    ":": "AB09",
    ";": "AB08",
    "<": "LSGT",
    "=": "AE12",
    ">": "LSGT",
    "?": "AB07",
    "@": "AE02",
    "A": "AD01",
    "B": "AB05",
    "C": "AB03",
    "D": "AC03",
    "E": "AD03",
    "F": "AC04",
    "G": "AC05",
    "H": "AC06",
    "I": "AD08",
    "J": "AC07",
    "K": "AC08",
    "L": "AC09",
    "M": "AC10",
    "N": "AB06",
    "O": "AD09",
    "P": "AD10",
    "Q": "AC01",
    "R": "AD04",
    "S": "AC02",
    "T": "AD05",
    "U": "AD07",
    "V": "AB04",
    "W": "AB01",
    "X": "AB02",
    "Y": "AD06",
    "Z": "AD02",
    "[": "AE05",
    "]": "AE11",
    "^": "AD11",
    "_": "AE08",
    "`": "AE07",
    "a": "AD01",
    "b": "AB05",
    "c": "AB03",
    "d": "AC03",
    "e": "AD03",
    "f": "AC04",
    "g": "AC05",
    "h": "AC06",
    "i": "AD08",
    "j": "AC07",
    "k": "AC08",
    "l": "AC09",
    "m": "AC10",
    "n": "AB06",
    "o": "AD09",
    "p": "AD10",
    "q": "AC01",
    "r": "AD04",
    "s": "AC02",
    "t": "AD05",
    "u": "AD07",
    "v": "AB04",
    "w": "AB01",
    "x": "AB02",
    "y": "AD06",
    "z": "AD02",
    "{": "AE04",
    "|": "AE06",
    "}": "AE12",
    "~": "AE02",
  },
  "Apple German": { # Apple QWERTZ
    "!": "AE01",
    "$": "AE04",
    "%": "AE05",
    "&": "AE06",
    "'": "AE12",
    "(": "AE08",
    ")": "AE09",
    "*": "AD12",
    "+": "AD12",
    ",": "AB08",
    "-": "AB10",
    ".": "AB09",
    "/": "AE07",
    "0": "AE10",
    "1": "AE01",
    "2": "AE02",
    "3": "AE03",
    "4": "AE04",
    "5": "AE05",
    "6": "AE06",
    "7": "AE07",
    "8": "AE08",
    "9": "AE09",
    ":": "AB09",
    ";": "AB08",
    "<": "TLDE",
    "=": "AE10",
    ">": "TLDE",
    "?": "AE11",
    "@": "AC09",
    "A": "AC01",
    "B": "AB05",
    "C": "AB03",
    "D": "AC03",
    "E": "AD03",
    "F": "AC04",
    "G": "AC05",
    "H": "AC06",
    "I": "AD08",
    "J": "AC07",
    "K": "AC08",
    "L": "AC09",
    "M": "AB07",
    "N": "AB06",
    "O": "AD09",
    "P": "AD10",
    "Q": "AD01",
    "R": "AD04",
    "S": "AC02",
    "T": "AD05",
    "U": "AD07",
    "V": "AB04",
    "W": "AD02",
    "X": "AB02",
    "Y": "AB01",
    "Z": "AD06",
    "[": "AE05",
    "]": "AE06",
    "_": "AB10",
    "a": "AC01",
    "b": "AB05",
    "c": "AB03",
    "d": "AC03",
    "e": "AD03",
    "f": "AC04",
    "g": "AC05",
    "h": "AC06",
    "i": "AD08",
    "j": "AC07",
    "k": "AC08",
    "l": "AC09",
    "m": "AB07",
    "n": "AB06",
    "o": "AD09",
    "p": "AD10",
    "q": "AD01",
    "r": "AD04",
    "s": "AC02",
    "t": "AD05",
    "u": "AD07",
    "v": "AB04",
    "w": "AD02",
    "x": "AB02",
    "y": "AB01",
    "z": "AD06",
    "{": "AE08",
    "|": "AE07",
    "}": "AE09",
  },
  "ISO QWERTZ": {
    "!": "AE01",
    "$": "AE04",
    "%": "AE05",
    "&": "AE06",
    "'": "AE12",
    "(": "AE08",
    ")": "AE09",
    "*": "BKSL",
    "+": "AD12",
    ",": "AB08",
    "-": "AB10",
    ".": "AB09",
    "/": "AE07",
    "0": "AE10",
    "1": "AE01",
    "2": "AE02",
    "3": "AE03",
    "4": "AE04",
    "5": "AE05",
    "6": "AE06",
    "7": "AE07",
    "8": "AE08",
    "9": "AE09",
    ":": "AB09",
    ";": "AB08",
    "<": "LSGT",
    "=": "AE10",
    ">": "LSGT",
    "?": "AB10",
    "@": "AD01",
    "A": "AC01",
    "B": "AB05",
    "C": "AB03",
    "D": "AC03",
    "E": "AD03",
    "F": "AC04",
    "G": "AC05",
    "H": "AC06",
    "I": "AD08",
    "J": "AC07",
    "K": "AC08",
    "L": "AC09",
    "M": "AB07",
    "N": "AB06",
    "O": "AD09",
    "P": "AD10",
    "Q": "AD01",
    "R": "AD04",
    "S": "AC02",
    "T": "AD05",
    "U": "AD07",
    "V": "AB04",
    "W": "AD02",
    "X": "AB02",
    "Y": "AB01",
    "Z": "AD06",
    "[": "AE08",
    "]": "AE09",
    "^": "TLDE",
    "_": "AB10",
    "`": "AE12",
    "a": "AC01",
    "b": "AB05",
    "c": "AB03",
    "d": "AC03",
    "e": "AD03",
    "f": "AC04",
    "g": "AC05",
    "h": "AC06",
    "i": "AD08",
    "j": "AC07",
    "k": "AC08",
    "l": "AC09",
    "m": "AB07",
    "n": "AB06",
    "o": "AD09",
    "p": "AD10",
    "q": "AD01",
    "r": "AD04",
    "s": "AC02",
    "t": "AD05",
    "u": "AD07",
    "v": "AB04",
    "w": "AD02",
    "x": "AB02",
    "y": "AB01",
    "z": "AD06",
    "{": "AE07",
    "|": "LSGT",
    "}": "AE10",
    "~": "AD12",
  },
}
#matrix_key = {
#  "ANSI QWERTY": [
#      1,    4,    5,    7,   39,    9,   10,    8,   12,   49,   11,   50,   51,   10,
#      1,    2,    3,    4,    5,    6,    7,    8,    9,   38,   38,   49,   12,   50,
#     51,    2,   29,   46,   44,   31,   17,   32,   33,   34,   22,   35,   36,   37,
#     48,   47,   23,   24,   15,   18,   30,   19,   21,   45,   16,   43,   20,   42,
#     25,   26,    6,   11,    0,   29,   46,   44,   31,   17,   32,   33,   34,   22,
#     35,   36,   37,   48,   47,   23,   24,   15,   18,   30,   19,   21,   45,   16,
#     43,   20,   42,   25,   27,   26,    0
#  ],
#  "Apple GB QWERTY": [
#    
#  ],
#  "ISO QWERTY": [
#    
#  ],
#  "Apple AZERTY": [
#      8,   26,   39,    1,    4,    5,   11,   26,   52,   49,   12,   50,   51,   10,
#      1,    2,    3,    4,    5,    6,    7,    8,    9,   51,   50,   42,   52,   42,
#     49,    0,   15,   47,   45,   31,   17,   32,   33,   34,   22,   35,   36,   37,
#     38,   48,   23,   24,   29,   18,   30,   19,   21,   46,   43,   44,   20,   16,
#      5,   11,   25,   12,   40,   15,   47,   45,   31,   17,   32,   33,   34,   22,
#     35,   36,   37,   38,   48,   23,   24,   29,   18,   30,   19,   21,   46,   43,
#     44,   20,   16,    5,   37,   11,   48
#  ],
#  "ISO AZERTY": [
#    
#  ],
#  "Apple QWERTZ": [
#    
#  ],
#  "ISO QWERTZ": [
#    
#  ],
#}
#set_trimmed = [
#  '!',  '$',  '%',  '&', '\'',  '(',  ')',  '*',  ',',  '-',  '.', '/',  ':',  ';',
#  '?',  '@',  'A',  'M',  'Q',  'W',  'Z',  '[', ']',  '^',  '`',  'a',  'm',  'q',
#  'w',  'z',  '{',  '|',  '}', '~'
#] # in ASCII order.

alias_layout = {
  "apus": "ANSI QWERTY",
  "us":   "ANSI QWERTY",
  # ANSI US QWERTY
  "apuk": "Apple British", # Apple GB QWERTY
  "apgb": "Apple British", # Apple GB QWERTY
  # Apple GB QWERTY
  "uk":   "ISO QWERTY",
  "gb":   "ISO QWERTY",
  # ISO GB QWERTY
  "apfr": "Apple French", # Apple FR AZERTY
  "fr":   "ISO AZERTY", # ISO FR AZERTY
  "apde": "Apple German", # Apple DE QWERTZ
  "de":   "ISO QWERTZ", # ISO DE QWERTZ
}

def set_characters( ids_layout: list[str] | None = None ) -> list[str]:
  if ids_layout is None:
    ids_layout = []
  if not ids_layout:
    return set_character

  intersection_set: list[str] = []
  symmetricdifference_set: list[str] = []
  length_set: int = len( set_character )
  ids_matrix_key: list[str] = [] #layouts
  id_layout: str
  id_matrix_key: str
  ids_key: list[str]

  id_layout = ""
  for id_layout in ids_layout:
    id_layout = str( id_layout ).strip().lower()
    if id_layout in alias_layout:
      ids_matrix_key.append( alias_layout[id_layout] )
    else:
      raise ValueError("RPwG doesn't know the layout "+id_layout+'.')
    if ids_matrix_key[ -1 ] not in matrix_key:
      raise ValueError("RPwG doesn't have the layout "+ids_matrix_key[ -1 ]+'.')
  for character in set_character:
    ids_key = []
    id_matrix_key = ""
    for id_matrix_key in ids_matrix_key:
      if character not in matrix_key[ id_matrix_key ]:
        break
      ids_key.append( matrix_key[ id_matrix_key ][ character ] )
    if len( ids_key ) == len( ids_matrix_key ) and len( set( ids_key ) ) == 1:
      intersection_set.append( character )
  #intersection_set = list(set( set_character )^set( symmetricdifference_set )) #set_character = list(set( set_character )^set( set_trimmed ))
  return intersection_set

def stringtogether_password( length_password: int, set_character_password: list[str] ) -> str:
  if length_password <= 0:
    raise ValueError("RPwG can't generate a password with a null or negative length.")
  if not set_character_password:
    raise ValueError("RPwG can't generate a password from an empty character set.")
  string_password = ""
  
  while 0 < length_password:
    string_password += str( secrets.choice( set_character_password ) )
    length_password -= 1
  
  return string_password

def interactwith_program():
  string_splash: str = """RANDOM      PASSWORD     GENERATOR
   ,-----, ,-----,         ,-----,
  / /'/ / / /'/ / ,-,-,-, / /''-'
 / / | | / ,---' / / / / / /_/'/
'-'  '-''-'     '-----' '-----'
V  E  R  S  I  O  N     1  .  6  b"""
  length_password: int
  set_password: list[str]
  string_mode: str
  flag_mode: int
  vector_layout: list[str] = []
  id_layout: str
  
  print(ANSIES.dim+string_splash+ANSIES.reset)
  try:
    length_password = int( input(ANSIES.bold+"password length:\t"+ANSIES.reset) )
  except:
    length_password = random.randint( 8, 127 )
  try:
    string_mode = input(ANSIES.bold+"cross-layout mode, 'y' for yes or by default 'n' for no:\t"+ANSIES.reset)
  except:
    string_mode = "NO"
  if bool(re.fullmatch(r'\b[Yy]([Ee][Ss])?\b', str(string_mode).strip())):
    flag_mode = 1
  else:
    flag_mode = 0
  if flag_mode == 1:
    while True:
      try:
        id_layout = input(ANSIES.bold+"layout, for example \"us\" for ANSI QWERTY:\t"+ANSIES.reset)
      except EOFError:
        break
      id_layout = str(id_layout).strip()
      if not id_layout:
        break
      vector_layout.append(id_layout)
    if not vector_layout:
      vector_layout = ["us", "apfr"]
    set_password = set_characters( vector_layout )
  else:
    set_password = set_character
  return stringtogether_password( length_password, set_password )

def help_use() -> None:
  print("""rpwg.py --length=12 --mode=cross-layout --layout=us --layout=apfr
        --random
        --interactive
        --help
rpwg.py -l 8 -m q -k us -k apus -k gb -k apfr -k de
        -r
        -i
        -h""")
#  return """rpwg.py --length=12 --mode=cross-layout --layout=us --layout=apfr
#        --random
#        --interactive
#        --help
#rpwg.py length=16 mode=qwazerty layout=us layout=apde
#rpwg.py -l 6 -m c -k uk -k fr
#rpwg.py l 8 m q k us k apus k gb k de"""

def main():
  #vector_argument = []
  length_password: int = 0
  flag_mode: int = 0
  vector_layout: list[str] = []
  set_password: list[str] = []
  string_password: str
  vector_option: list[tuple[str, str]]
  option: str
  vector_parameter: list[str]
  parameter: str
  
  try:
    vector_option,\
    vector_parameter = getopt.getopt(
      sys.argv[1:],
      "l:m:k:rihu",
      [
        "length=",
        "mode=",
        "layout=",
        "random",
        "interactive",
        "help",
        "use",
      ]
    )
  except getopt.GetoptError as string_error:
    print(string_error)
    help_use()
    return 2
  
  if vector_parameter:
    print("RPwG doesn't handle "+" ".join( vector_parameter )+'.')
    help_use()
    return 2
  
  if not vector_option:
    help_use()
    return 2
  
  for option, parameter in vector_option:
    if option in ("--length", "-l"):
      try:
        length_password = int( parameter )
      except ValueError:
        print("RPwG couldn't understand the password length "+str( parameter )+'.')
        return 2
    
    elif option in ("--mode", "-m"):
      parameter = str(parameter).strip().lower()
      if bool(re.fullmatch(r'q(wazerty)?|cross-layout|cross|c', parameter)): #if bool( re.match(r'\b(q(wazerty)?|c(ross(-layout)?)?)\b', parameter)):
        flag_mode = 1
      else:
        flag_mode = 0
    
    elif option in ("--layout", "-k"):
      vector_layout.append(str(parameter))

    elif option in ("--random", "-r"):
      length_password = random.randint( 8, 127 )
      flag_mode = random.randint( 0, 1 )
    
    elif option in ("--interactive", "-i"):
      string_password = interactwith_program()
      print(string_password)
      return 0
    
    elif option in ("--help", "-h", "--use", "-u"):
      help_use()
      return 0
  
  if length_password <= 0:
    length_password = random.randint( 8, 127 )
  
  if flag_mode == 1:
    if not vector_layout:
      vector_layout = ["us", "apfr"]
    set_password = set_characters( vector_layout )
  else:
    set_password = set_character
  
  string_password = stringtogether_password( length_password, set_password )
  print(ANSIES.reset+string_password)
  return 0

if __name__ == "__main__":
  sys.exit( main() )

#	rpwg.py
#	KVPB's random password generator
#	1.64 alpha
#
#	Karl V. P. B. `kvpb`    Karl Thomas George West `ktgw`
#	+33 A BB BB BB BB       +1 (DDD) DDD-DDDD
#	local-part@domain	      local-part@domain
#	kvpb.fr                 
#	https://x.com/ktgwkvpb  
#	https://github.com/kvpb 
#
#	'I can help you!
#	 I can understand!
#	 I can help you!
#	 ... To the promised land!
#	 I'm _your_ helping hand,
#	 your midnight man!
#	 Your midnight man!'

#	Copyright 2026 Karl Vincent Pierre Bertin
#
#	Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
#	1.  Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
#	2.  Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
#	3.  Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
#
#	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

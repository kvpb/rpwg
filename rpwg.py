#!/usr/bin/env python3

import sys
import getopt
import re
import random

class ANSIES:
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
  
  def disable(self):
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
    '!',  '$',  '%',  '&', '\'',  '(',  ')',  '*',  '+',  ',',  '-',  '.',  '/',  '0',
    '1',  '2',  '3',  '4',  '5',  '6',  '7',  '8',  '9',  ':',  ';',  '<',  '=',  '>',
    '?',  '@',  'A',  'B',  'C',  'D',  'E',  'F',  'G',  'H',  'I',  'J',  'K',  'L',
    'M',  'N',  'O',  'P',  'Q',  'R',  'S',  'T',  'U',  'V',  'W',  'X',  'Y',  'Z',
    '[',  ']',  '^',  '_',  '`',  'a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',
    'j',  'k',  'l',  'm',  'n',  'o',  'p',  'q',  'r',  's',  't',  'u',  'v',  'w',
    'x',  'y',  'z',  '{',  '|',  '}',  '~'
] # in ASCII order, no 032, '"', '\' or '#'.
matrix_key = {
  "ANSI QWERTY": [
      1,    4,    5,    7,   39,    9,   10,    8,   12,   49,   11,   50,   51,   10,
      1,    2,    3,    4,    5,    6,    7,    8,    9,   38,   38,   49,   12,   50,
     51,    2,   29,   46,   44,   31,   17,   32,   33,   34,   22,   35,   36,   37,
     48,   47,   23,   24,   15,   18,   30,   19,   21,   45,   16,   43,   20,   42,
     25,   26,    6,   11,    0,   29,   46,   44,   31,   17,   32,   33,   34,   22,
     35,   36,   37,   48,   47,   23,   24,   15,   18,   30,   19,   21,   45,   16,
     43,   20,   42,   25,   27,   26,    0
  ],
  "Apple AZERTY": [
      8,   26,   39,    1,    4,    5,   11,   26,   52,   49,   12,   50,   51,   10,
      1,    2,    3,    4,    5,    6,    7,    8,    9,   51,   50,   42,   52,   42,
     49,    0,   15,   47,   45,   31,   17,   32,   33,   34,   22,   35,   36,   37,
     38,   48,   23,   24,   29,   18,   30,   19,   21,   46,   43,   44,   20,   16,
      5,   11,   25,   12,   40,   15,   47,   45,   31,   17,   32,   33,   34,   22,
     35,   36,   37,   38,   48,   23,   24,   29,   18,   30,   19,   21,   46,   43,
     44,   20,   16,    5,   37,   11,   48
  ]
}
#set_trimmed = [
#  '!',  '$',  '%',  '&', '\'',  '(',  ')',  '*',  ',',  '-',  '.', '/',  ':',  ';',
#  '?',  '@',  'A',  'M',  'Q',  'W',  'Z',  '[', ']',  '^',  '`',  'a',  'm',  'q',
#  'w',  'z',  '{',  '|',  '}', '~'
#] # in ASCII order.

def characters_set(id_layout_1st="", id_layout_2nd=""):
#  if id_layout_1st == "" or id_layout_2nd == "":
#    return set_character

  intersection_set = []
  symmetricdifference_set = []
  length_set = len( set_character )

  match id_layout_1st:
    case "us": #bool(re.match(r'\b[Uu]([Ss])?\b', str(id_layout_1st))):
      layout_1st = "ANSI QWERTY"
    case "fr": #bool(re.match(r'\b[Ff]([Rr])?\b', str(id_layout_1st))):
      layout_1st = "Apple AZERTY"
    case "" | _:
      layout_1st = "ANSI QWERTY"
  match id_layout_2nd:
    case "us": #bool(re.match(r'\b[Uu]([Ss])?\b', str(id_layout_2nd))):
      layout_2nd = "ANSI QWERTY"
    case "fr": #bool(re.match(r'\b[Ff]([Rr])?\b', str(id_layout_2nd))):
      layout_2nd = "Apple AZERTY"
    case "" | _:
      layout_2nd = "ANSI QWERTY"
  print(layout_1st, '\t', layout_2nd)
  index = 0
  while index < length_set:
    print( index, '\t', set_character[ index ], '\t', matrix_key[layout_1st][ index ], '\t', matrix_key[layout_2nd][ index ] )
    if matrix_key[layout_1st][ index ] != matrix_key[layout_2nd][ index ]:
      print("\t\t", matrix_key[layout_1st][ index ], '\t', matrix_key[layout_2nd][ index ] )
      symmetricdifference_set.append( set_character[ index ] )
    index += 1
  print( symmetricdifference_set, '\t', len( symmetricdifference_set ) )
  intersection_set = list(set( set_character )^set( symmetricdifference_set )) #set_character = list(set( set_character )^set( set_trimmed ))
  print( intersection_set, '\t', len( intersection_set ) )
  
  return intersection_set

def password_stringtogether( length_password, set_character_password ):
  string_password = ""
  length_set_character = len( set_character_password )
  
  while 0 < length_password:
    string_password += str( set_character_password[ random.randint( 0, length_set_character - 1 ) ] )
    length_password -= 1
  
  return string_password

def program_interactwith():
  string_splash = """RANDOM      PASSWORD     GENERATOR
   ,-----, ,-----,         ,-----,
  / /'/ / / /'/ / ,-,-,-, / /''-'
 / / | | / ,---' / / / / / /_/'/
'-'  '-''-'     '-----' '-----'
V  E  R  S  I  O  N     1  .  6  b"""
  length_password = 0
  set_password = set_character
  string_mode = ""
  id_layout_1st = ""
  id_layout_2nd = ""
  truth_mode = 0
  
  print(ANSIES.dim + string_splash + ANSIES.reset)
  
  try:
    length_password = int( input(ANSIES.bold + "password length:\t" + ANSIES.reset) )
  except:
    length_password = random.randint( 8, 127 )
  
  try:
    string_mode = input(ANSIES.bold + "QWAZERTY^TM mode, 'y' for \"yes\" or by default 'n' for \"no\":\t" + ANSIES.reset)
  except:
    string_mode = "NO"
  
  if bool(re.match(r'\b[Yy]([Ee][Ss])?\b', str(string_mode))):
    truth_mode = 1
  else:
    truth_mode = 0
  
  if truth_mode == 1:
    try:
      id_layout_1st = input(ANSIES.bold + "1st layout, for example \"us\" for ANSI QWERTY:\t" + ANSIES.reset)
    except:
      id_layout_1st = ""
    try:
      id_layout_2nd = input(ANSIES.bold + "2nd layout, for example \"fr\" for Apple AZERTY:\t" + ANSIES.reset)
    except:
      id_layout_2nd = ""
    if id_layout_2nd == id_layout_1st:
      id_layout_1st = "us"
      id_layout_2nd = "fr"
    set_password = characters_set(id_layout_1st, id_layout_2nd)
  else:
    set_password = set_character
  
  return password_stringtogether( length_password, set_password )

def main():
  #vector_argument = []
  length_password = 0
  truth_mode = 0
  id_layout_1st = ""
  id_layout_2nd = ""

  string_help = """rpwg.py --length=12 --mode=q --1stlayout=us --2ndlayout=fr
        --random
        --interactive
        --help"""
  
  try:
    vector_option, vector_parameter = getopt.getopt(sys.argv[1:], "l:m:1:2:rih", ["length=", "mode=", "1stlayout=", "2ndlayout=", "random", "interactive", "help"])
  except getopt.GetoptError as string_error:
    print(string_error)
    sys.exit( 2 )
  if not vector_option:
    length_password = random.randint( 8, 127 )
    truth_mode = random.randint( 0, 1 )
    if truth_mode == 1:
      string_password = password_stringtogether( length_password, characters_set("us", "fr") )
    else:
      string_password = password_stringtogether( length_password, characters_set("", "") )
    print(string_help)
    return 0
  for option, parameter in vector_option:
    if option in ("-l", "--length"):
      if int( parameter ):
        length_password = int( parameter )
      else:
        length_password = random.randint( 8, 127 )
    elif option in ("-m", "--mode"):
      if bool(re.match(r'\b[Qq]([Ww][Aa][Zz][Ee][Rr][Tt][Yy])?\b', str(parameter))):
        truth_mode = 1
      else:
        truth_mode = 0
    elif option in ("-1", "--1stlayout"):
      id_layout_1st = str(parameter)
    elif option in ("-2", "--2ndlayout"):
      id_layout_2nd = str(parameter)
    elif option in ("-r", "--random"):
      length_password = random.randint( 8, 127 )
      truth_mode = random.randint( 0, 1 )
    elif option in ("-h", "--help"):
      print(string_help)
      sys.exit()
    elif option in ("-i", "--interactive"):
      string_password = program_interactwith()
      print(string_password)
      return 0
  string_password = password_stringtogether( length_password, characters_set(id_layout_1st, id_layout_2nd) )
  print(ANSIES.reset + string_password)

if __name__ == "__main__":
  main()

#	rpwg.py
#	Random Password Generator
#	1.6 beta
#
#	Karl V. P. B. `kvpb`	Karl Thomas George West `ktgw`
#	+33 A BB BB BB BB		+1 (DDD) DDD-DDDD
#	local-part@domain		local-part@domain
#	kvpb.fr
#	https://x.com/ktgwkvpb
#	https://github.com/kvpb
#
#	'I can help you!
#	I can understand!
#	I can help you!
#	... To the promised land!
#	I'm _your_ helping hand,
#	your midnight man!
#	Your midnight man!'

#	Copyright 2024 Karl Vincent Pierre Bertin
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

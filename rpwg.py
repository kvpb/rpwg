#!/usr/bin/env python3

import sys
import getopt
import re
import random

def sub( l, t ):
  #s = ''
  a_f = [
           '!',  '$',  '%',  '&', '\'',  '(',  ')',  '*',  '+',  ',',  '-',
           '.',  '/',  '0',  '1',  '2',  '3',  '4',  '5',  '6',  '7',  '8',
           '9',  ':',  ';',  '<',  '=',  '>',  '?',  '@',  'A',  'B',  'C',
           'D',  'E',  'F',  'G',  'H',  'I',  'J',  'K',  'L',  'M',  'N',
           'O',  'P',  'Q',  'R',  'S',  'T',  'U',  'V',  'W',  'X',  'Y',
           'Z',  '[',  ']',  '^',  '_',  '`',  'a',  'b',  'c',  'd',  'e',
           'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n',  'o',  'p',
           'q',  'r',  's',  't',  'u',  'v',  'w',  'x',  'y',  'z',  '{',
           '|',  '}',  '~'
        ] # in ASCII order, no 032, ", \ or #.
  a_t = [
           '!',  '$',  '%',  '&', '\'',  '(',  ')',  '*',  ',',  '-',  '.',
           '/',  ':',  ';',  '?',  '@',  'A',  'M',  'Q',  'W',  'Z',  '[',
           ']',  '^',  '`',  'a',  'm',  'q',  'w',  'z',  '{',  '|',  '}',
           '~'
        ] # in ASCII order.
  #a = list(set( a_f )^set( a_t ))
  #l_a = len( a )
  
  if    (  t ==  1 ):
    a_f = list(set( a_f )^set( a_t ))
  
  l_a = len( a_f )

  s = ''
  while (  0  <  l ):
    s += str( a_f[ random.randint( 0, l_a - 1 ) ] )
    l -= 1
  
  return s

#print(sub( random.randint( 0, 80 ), random.randint( 0, 1 ) )) #print(sub( 8, 1 )) #	debug

def alt():
  s = """RANDOM      PASSWORD     GENERATOR
   ,-----, ,-----,         ,-----,
  / /'/ / / /'/ / ,-,-,-, / /''-'
 / / | | / ,---' / / / / / /_/'/
'-'  '-''-'     '-----' '-----'
V  E  R  S  I  O  N     1  .  5  0"""
  #l = 0 #l = input("password length:\t")
  #m = "" #m = input("QWAZERTY mode:\t")
  #t = 0
  
  print(s)
  
  try:
    l = int( input("password length:\t") )
  except:
    l = random.randint( 8, 127 )
  #l = input("password length:\t")
  #print( l ) #	debug
  
  try:
    m = input("QWAZERTY mode [yN]:\t")
  except:
    m = 'NO'
  #m = input("QWAZERTY mode [yN]:\t")
  #print(m)#	debug
  
  #print( bool(re.match(r'\b[Yy]([Ee][Ss])?\b', str(m))) ) #	debug
  if bool(re.match(r'\b[Yy]([Ee][Ss])?\b', str(m))):
    t = 1
  else:
    t = 0
  #print( t ) #	debug
  
  return sub( l, t )

#print(alt()) #	debug

def main():
  #v_a = 
  l = 0
  t = 0
  s = """rpwg.py --length=12 --mode=q
        --random
        --interactive
        --help""" #s = "RTFM. Don't worry; I kept it simple for you."
  
  try:
    v_o, v_p = getopt.getopt(sys.argv[1:], "l:m:rih", ["length=", "mode=", "random", "interactive", "help"])
  except getopt.GetoptError as s:
    print(s)
    sys.exit(2)
  if not v_o:
    l = random.randint( 8, 127 )
    t = random.randint( 0, 1 )
    s = sub( l, t )
    print(s)
    return 0
  for o, p in v_o:
    if o in ("-l", "--length"):
      if int( p ):
        l = int( p )
      else:
        l = random.randint( 8, 127 )
    elif o in ("-m", "--mode"):
      if bool(re.match(r'\b[Qq]([Ww][Aa][Zz][Ee][Rr][Tt][Yy])?\b', str(p))):
        t = 1
      else:
        t = 0
    elif o in ("-r", "--random"):
      l = random.randint( 8, 127 )
      t = random.randint( 0, 1 )
    elif o in ("-h", "--help"):
      print(s)
      sys.exit()
    elif o in ("-i", "--interactive"):
      s = alt()
      print(s)
      return 0
    #else:
    #  l = random.randint( 8, 127 )
    #  t = random.randint( 0, 1 )
  s = sub( l, t )
  print(s)

if __name__ == "__main__":
  main()

#	rpwg.py
#	Random Password Generator
#	Version 1.50
#
#	Karl V. P. B. `kvpb`
#	+1 (DDD) DDD-DDDD
#	+33 A BB BB BB BB
#	local-part@domain
#	https://www.linkedin.com/in/karlbertin
#	https://twitter.com/kvpbx
#	https://github.com/kvpb
#	https://www.instagram.com/add/karlbertin
#	https://vm.tiktok.com/ZSwAmcFh/
#	
#	Women, they will come, and they will go.
#	When the rain washes you clean, you'll know.
#	Oh, thunder only happens when it's raining.
#	Players only love you when they're playing.
#	
#	... And the music stops.
#	This is funny, if you think about it. I was gonna do it this time for real. But the carbine was not under the bed. I did not find the rifle. Nor did I find the mag either. Fuck me, right? She said we never left it underneath the bed. Maybe. She never really lies to me, so I guess she told me the truth. Thought I had kept that bloody thing. Perhaps never had it to begin with. Can hardly tell. That whole COVID-19 fuckery messed my head up pretty bad. I usually am lucky, but I would really like to see the luck into this. Depressing sucks. Believe me, I have not missed that crap all those years. I doubt I will ever have the balls again, even if I was depressing once too many once more, had the rifle loaded, had gone through a lot, and Ritalin wore off at the same time. Screw this shit. Rifle rounds seem to be some of the best pills against that. Could barely work any worse, except if you survive, but I have never seen anyone manage to pull that off with 7.62. Oh well. Could be worse. We finally get to see the freaking Sun again. I feel better, sorta-kinda-ish. I gotta get the hell outta here before winter. Or else this will not go well at all. If I cannot make it to California in time, I need to at least reach Dublin or Vancouver. I have been rotting in this fourth-world-country-to-be shithole for far too long. I will be able to immigrate to the United States more easily from there. Then will have to wait 7 years for the US citizenship. It is what it is. Gotta play by the rules. I really do not want to live here anymore. People are rude. The culture is inflated horseshit. The weather is dogpiss. Careers are rubbish. Jobs pay shit. The ed sys is fucked. Its academics make everyone cringe. Fonctionnaires are the Antichrist. Nothing ever happens here. Le la lu french baguette with a glass of pinard and ho ho ho le beret de Madame, this is all turbogarbage. Graveyards are funnier, and those do not exactly make me wanna party hard already. Yeah. Not happy. 1 green dot on TripAdvisor. Would not recommend. I can milk better from my meat, a gym and an OnlyFans, and even that option interests me more. I just wanna drive through Utah, swim in Hawaii... But why the fuck am I here? Why am I stuck here in fucking France? Why do people in these parts have to be complete assholes? Why did I have to start my education over all by myself alone for nothing? Why did they waste 20 years of my fucking life? Why did we have to pay for everything, when the other motherfuckers got anything for free? Why will you never get any better than the scraps of inept top school graduates here? I am gonna go to bed.

#	Copyright 2022 Karl V. P. Bertin
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

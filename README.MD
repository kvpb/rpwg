<p align='center'><a href=''><img src='https://gistcdn.githack.com/kvpb/bfc847c17e106fb8f99c9bdf05d408c7/raw/73ea74e68c8543efb617120f2af2d6cbd2c42f22/aceofclubs.svg' alt="Karl Vincent Pierre Bertin AKA Karl Thomas George West's"></a></p>
<p align='center'><a href='https://github.com/kvpb/.files/blob/master/bin/rpwg.py'><img src='https://gistcdn.githack.com/kvpb/c9d1aa35c62862e73c50836dc49dbc66/raw/8023f43cc7eb3d7849511deada26a71b2bad29b3/rpwg.svg' alt="an illustration for Karl Vincent Pierre Bertin AKA Karl Thomas George West's cross-layout random password generator"></a></p>

![platform](https://gistcdn.githack.com/kvpb/ed57eb3a03f2b5338fbede97e7cf296b/raw/ea6556bb04f592433023533ddbd931cc7d23e92b/apple-F6F6F6D5E1ED1E72F21AD5FD-madeona-1AD5FD1E72F2-mac-F6F6F6D5E1ED.svg) ![platform](https://gistcdn.githack.com/kvpb/ed57eb3a03f2b5338fbede97e7cf296b/raw/ea6556bb04f592433023533ddbd931cc7d23e92b/ubuntu-F6F6F6D5E1ED1E72F21AD5FD-madeona-1AD5FD1E72F2-linuxbox-F6F6F6D5E1ED.svg) ![platform](https://gistcdn.githack.com/kvpb/ed57eb3a03f2b5338fbede97e7cf296b/raw/ea6556bb04f592433023533ddbd931cc7d23e92b/android-F6F6F6D5E1ED1E72F21AD5FD-madeonan-1AD5FD1E72F2-androidphone-F6F6F6D5E1ED.svg)

```
Karl V. P. B.
WWWWWWWW WW
WW WWW WW WWW
WWWWW WWWWW
WWWWWW
+33 A BB BB BB BB
local-part@domain

                                            `a Paris, le 2 juillet 2026

                         K a r l   V .   P .   B . ' s
                       ,-----, ,-----,         ,-----,
                      / /'/ / / /_/ / ,-,-,-, / /''-'
                     / / | | / ,---' / / / / / /_/'/
                    '-'  '-''-'     '-----' '-----'
                   random password generator  1.67

                           instructions manual

    RPwG is a cross-layout--originally French-American 'QWAZERTY'--
random password generator. This program is written in Python 3. It
randomly generates passwords of length and cross-layout portability
at the user's discretion. NB: though cross-layout passwords are cool
and thus will make you get laid with bimbos, cross-layout portability
reduces the set of available characters, and the more different layouts
are set, the more the character set is restricted, so the adverse
effect on security should be compensated for with a higher password
length.
    The files in this ZIP constitute the official release of RPwG.
They are not documented currently. RPwG is made self-explanatory. A few
points should be noted, particularly by a novice user.

          rpwg.py
                  --length=${n}   (-l ${n})
                  --mode="${s}"   (-m ${s})
                  --layout="${s}" (-k ${s})
                  --interactive   (-i)
                  --random        (-r)
                  --help          (-h)

          --length=${n}, -l ${n}
            Set the length of the password. l is an integer number. If
            the user does not set the mode along, the program randomly
            sets it.

          --mode="${s}", -m ${s}
            Set the portability of the password. s is a string of
            characters: 'q'--"QWAZERTY"--and 'c'--'cross',
            'cross-layout'--for cross-layout compatibility or anything
            else for none. If the user does not set the length along,
            the program randomly sets it.

          --layout="${s}", -k ${s}
            Set a layout. The user must set it at least twice with
            different layouts. s is a string of characters, e.g. "us"
            for ANSI QWERTY or "apfr" for Apple AZERTY. Refer to the
            table below for the aliases of all keyboard layouts. If the
            user does not set two different layouts, the program
            historically defaults to ANSI QWERTY (United States
            English) and Apple French.

                     | alias      |        layout |
                     |------------|---------------|
                     | us, apus   |   ANSI QWERTY |
                     | uk, gb     |    ISO QWERTY |
                     | apuk, apgb | Apple British |
                     | fr         |    ISO AZERTY |
                     | apfr       |  Apple French |
                     | de         |    ISO QWERTZ |
                     | apde       |  Apple German |

          --random, -r
            Randomize both the length and portability of the password.
            This option overrides --interactive.

          --interactive, -i
            Fire up the good ol' interactive prompt. This option
            overrides other options, is overridden by --help.

          --help, -h
            Tell the user how to use RPwG. This option overrides all
            others.

          An online version 2 for freedom from Ruby was planned to
sport a graphical user interface, was to be written in JavaScript,
HTML5 and CSS3, would mimic a command-line interface on a Twiggy Mac.
The user would have had to only enter the length of the password and
set none to any amount of layouts. Although that version was 100%
graphically designed, it has been canceled until further notice.
    Since RPwG first was designed to make passwords without characters
of variable positions between the ANSI QWERTY and the ISO AZERTY
layouts, running the script without any option defaults to
French-American random password generation, whereas specifying two or
more keyboard layouts will incrementally refine the resulting password.
As RPwG 2.0 will emphasize security, the user will be alerted of the
lower security, as the level of layout divergence increases, and the
program will display various stats.

    Should problems arise with this software, please communicate them
to the author, or open an issue at https://github.com/kvpb/rpwg/issues.

                                             ^J:                       
                            ^   .:^^.      ^?7.                        
                          ^?Y~!!~~7J. ~!:~YY.               ...........
                        ^55?57.  ~Y5~!5?~:J~~~~^.  .:^^^~~~~~~~~~~~~~!!
                       7G?:  !~    ..       .  ~J  ::.... ....::^^^.   
                       .   ...^^^^^^^~~~~~~~!7J??!~~~~~~~~~~^^::.      
                         !?!^^^^:::....:::^~~~^                        
                         ~7~^^^^^^~~~~^^^::.                           
```
<br>
<p align='center'><a href='http://kvpb.co'><img src='https://gistcdn.githack.com/kvpb/c80594e9079e857c55c36dec49a1a2d7/raw/eec54d5821dc092ad910635141c4e4feebf07565/kvpbssymbol.svg'></a><br><!--
<b>Karl V. P. B. `<code>kvpb</code>`<br>
カール・ビンセント・ピエール・ベルティン</b><br>
<b>AKA&nbsp;&nbsp;Karl Thomas George West `<code>ktgw</code>`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;カール・トーマス・ジョージ・ウェスト</b><br>-->
<img src='https://gistcdn.githack.com/kvpb/f5f75716dd024cc48f8dc28176c0b642/raw/e5344bebf926b378faeb208724ae97f4e06639ca/kvpbsesrbrating.svg'></p>

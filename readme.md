<p align='center'><a href='https://github.com/kvpb/.files/blob/master/bin/rpwg.py'><img src='https://gistcdn.githack.com/kvpb/c9d1aa35c62862e73c50836dc49dbc66/raw/5c32c06d72b0169b6ed688efdd99d1d3d6d2eb31/rpwg.svg'></a></p>

# Random Password Generator<br>`rpwg.py`

```
Karl V. P. B.
XXXXXXXX XX
XX XXX XX XXX
XXXXX XXXXX, XXXXXX
+33 A BB BB BB BB
local-part@domain

                                                  A XXXXX, l'1 mai 2024

                       ,-----, ,-----,         ,-----,
                      / /'/ / / /_/ / ,-,-,-, / /''-'
                     / / | | / ,---' / / / / / /_/'/
                    '-'  '-''-'     '-----' '-----'
                   Random Password Generator  1.60

                           Instructions Manual

          RPwG is a French-American-- 'QWAZERTY'-- pseudorandom
password generator. This program written in Python pseudorandomly
generates passwords whose length and US QWERTY-FR AZERTY portability
are at the user's discretion. NB: Python 3 must be installed.
          The files in this ZIP constitute the first official release
of RPwG. Currently, they are not documented. RPwG has been designed
so that it is self-explanatory. There are a few points which should
be noted, particularly by any novice user.

          rpwg.py 
                  -l, --length=${l}
                  -m, --mode="${s}"
                  -1, --1stlayout="${s}"
                  -2, --2ndlayout="${s}"
                  -i, --interactive
                  -r, --random
                  -h, --help

          -l, --length=${l}
                Set the length of the password. l is an integer number.
                If the user does not set the mode along, the program
                randomly sets it. This option overrides all others.

          -m, --mode="${s}"
                Set the portability mode of the password. s is a string
                of characters like 'q' or "QWAZERTY" for cross-layout
                compatibility and 'a', "AZERTY" or even '' for none. If
                the user does not set the length along, the program
                randomly sets it. This option overrides all others.

          -1, --1stlayout="${s}"
                Set the first layout. s is a string of characters like
                "us" for ANSI QWERTY or "fr" for Apple AZERTY. If the
                user does not set two different layouts, the program
                defaults to ANSI QWERTY.

          -2, --2ndlayout="${s}"
                Set the second layout. s is a string of characters like
                "us" for ANSI QWERTY or "fr" for Apple AZERTY. If the
                user does not set two different layouts, the program
                defaults to ANSI QWERTY.

          -r, --random
                Randomly set the length and portability. This option
                overrides -i and -h.

          -i, --interactive
                Use the old interactive prompt. All other options
                override this one.

          -h, --help
                Print the help. This option overrides -i.

          An online version 2 was planned to have a GUI written in
HTML5, CSS3 and JavaScript, mimicking a powered-on Twiggy Mac in which
only enter the length of the password and set its 'qwazertyness'--- to
unrestrict users from Ruby as a requirement. Albeit the graphic design
part is 100% done, development has been canceled until further notice.
          As of may 2019, an offline version 2 is planned to be a
complete rewrite in Python adding support for all keyboard layouts,
performance improvements and better security. Since RPwG was designed
to make passwords from characters whose position differs not from the
US layout to the french layout, running the script without optional
arguments defaults to the franco-US-american random password
generation, whereas specifying two or more keyboard layouts will
incrementally refine the resulting password. Because RPwG 2.0 will put
emphasis on security, the user will be alerted of the decreasing
security as the layout divergence level increases, and the warning will
mention stats, e.g. the number of removed characters or the percentage
of lost keys per layout.

          Should problems arise with this software, please communicate
them to the author, or open an issue at
https://github.com/kvpb/rpwg/issues.

                                                                   Karl
```
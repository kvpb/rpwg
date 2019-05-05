```
Karl V. P. Bertin
X XXX XX XXX X XXXXXX
75005 Paris, France
+336XXXXXXXX
local-part@domain

                                                         A Paris, le 1 mai 2019

                          ,-----, ,-----,         ,-----,
                         / /'/ / / / / / ,-,-,-, / /''-'
                        / / | | / ,---' / / / / / /_/'/
                       '-'  '-''-'     '-----' '-----'
                      Random Password Generator  1.10

                              Instructions Manual

          RPwG is a franco-US-american-- 'QWAZERTY'-- random password 
generator. This program written in Ruby pseudorandomly generates passwords 
whose length and US QWERTY-FR AZERTY portability are at the user's discretion.
NB: Ruby must be installed.
          The files in this zip archive constitute the first official release
of the RPwG program. Currently, they are not documented. RPwG has been designed
so that it is self-explanatory. There are a few points which should be noted,
particularly by any novice user.

          How-to:
          1.	Launch a terminal emulator, e.g. Terminal.
          2.	Drag-and-drop the RPwG.rb file into the window of the terminal
            	emulator.
          3.	Press Enter.
          4.	Follow the on-screen instructions.
          5.	Enjoy your copy-pastable password!

          The program is designed both at a first attempt to create a 'true'
program and to fill its conceptor's need to have passwords whose typing do not
require US-american QWERTY to french AZERTY 'layout translation'; would have
there been such a password generator, making another one would have been
pointless. As such, it has been made naively, more or less, at that time when a
computer programmer begins. Ever since, the author has gained experience, and
they guessed an important detail about passwords and so password generation:
password authentication is made to protect the access to something, and so if a
password is part of the security, then the password itself becomes either a
factor of security or a vulnerability. A pseudorandomly generated password is
made by a program, which is written in a given language, which is defined and
has rules. If the rules are flawed and known, then how the program does its job
can be known, exposing any of its products to be counterfeited. In the case of
RPwG, written in Ruby, it uses the array class' sample method, which's source
code can be found at https://ruby-doc.org/core/Array.html#method-i-sample. But
a program is just an implementation of an idea written in a language, not the
idea itself. EG a french man wants to point the Moon to two women, a french and
an US-american: he has the idea to make them get that he talks about the Moon,
and he says 'Regardez la Lune' to the french and 'Look at the Moon' to the US-
american--- he implemented the same idea in two languages. The programs' rules
are not the only things that matter; design itself must be considered. To make
passwords 'QWAZERTY', RPwG ignores all characters which's key's location
differs from US QWERTY to FR AZERTY layouts. This potentially makes a password
known to have been made with RPwG easier to guess as the attacker has a way to
determine a set of characters to try first. If these aspects of the passwords
made via RPwG become flaws, then these passwords are at risk to be guessed.
For these reasons, RPwG should not be considered suit for top security purposes
such as a master key, an administrator account or a bank account. Yet still,
RPwG should remain reliable for strong security passwords.

          An online version 2 was planned to have a GUI written in HTML5, CSS3
and JavaScript, mimicking a powered-on Twiggy Mac in which only enter the
password's length and set its 'qwazertyness'--- to unrestrict users from Ruby
as a requirement. Albeit the graphic design part is 100% done, the development
has been canceled until further notice.
          As of may 2019, an offline version 2 is planned to be a complete
rewrite in Python adding support for all keyboard layouts, performance
improvements and better security. Since RPwG was designed to make passwords
from characters whose position differs not from the US layout to the french
layout, running the script without optional arguments defaults to the franco-
US-american random password generation, whereas specifying two or more keyboard
layouts will incrementally refine the resulting password. Because RPwG 2.0 will
put emphasis on security, the user will be alerted of the decreasing security
as the layout divergence level increases, and the warning will mention stats,
eg the number of removed characters or the percentage of lost keys per layout.

          Should problems arise with this software, please communicate them to
the author, or open an issue at https://github.com/kvpb/RPwG/issues.

                                                                           Karl
```
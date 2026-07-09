#!/usr/bin/make -f

SHELL = /bin/sh
# If we inherit the SHELL variable from the environment. https://www.gnu.org/software/make/manual/make.html#Makefile-Basics

.SUFFIXES:
# Clear out the suffix list. https://www.gnu.org/software/make/manual/make.html#Makefile-Basics

#	V A R I A B L E S   F O R   S P E C I F Y I N G   C O M M A N D S
#	                                    variables for specifying commands
#	https://www.gnu.org/software/make/manual/make.html#Command-Variables

INSTALL = /usr/bin/install -c#/usr/local/bin/install -c
INSTALL_PROGRAM = $(INSTALL)
# installer
INSTALL_DATA = ${INSTALL} -m 644

RM = rm
# remover

#	V A R I A B L E S   F O R   I N S T A L L A T I O N   D I R E C T O R I E S
#	                                         variables for installation directories
#	https://www.gnu.org/prep/standards/html_node/Directory-Variables.html#Directory-Variables
#	https://www.gnu.org/software/make/manual/make.html#Prerequisite-Types

#DESTDIR = /tmp/stage
# 'The DESTDIR variable is specified by the user on the make command line as an absolute file name.  For example: ```make DESTDIR=/tmp/stage install```  DESTDIR should be supported only in the install* and uninstall* targets, as those are the only targets where it is useful.  [...]  You should not set the value of DESTDIR in your Makefile at all; then the files are installed into their expected locations by default.' https://www.gnu.org/software/make/manual/make.html#DESTDIR

srcdir = .
prefix = /usr/local#$${HOME} # installation pathname prefix
datarootdir = $(prefix)/share
datadir = $(datarootdir)
exec_prefix = $(prefix)
bindir = $(exec_prefix)/bin
docdir = $(datarootdir)/doc/rpwg

#	R U L E S   &   P H O N Y   T A R G E T S
#	                        rules & phony targets
#	https://www.gnu.org/software/make/manual/make.html#Standard-Targets
#	https://www.gnu.org/software/make/manual/make.html#Install-Command-Categories

PROGRAM = rpwg
PROGRAM_SOURCE = $(srcdir)/rpwg.py
DATA = $(srcdir)/README.MD $(srcdir)/LICENSE

.PHONY: all
all:
	@:

.PHONY: install
install:
	$(INSTALL) -d $(DESTDIR)$(bindir)
	$(INSTALL_PROGRAM) $(PROGRAM_SOURCE) $(DESTDIR)$(bindir)/$(PROGRAM)
	$(INSTALL) -d $(DESTDIR)$(docdir)
	$(INSTALL_DATA) $(DATA) $(DESTDIR)$(docdir)

.PHONY: uninstall
uninstall:
	$(RM) -v $(DESTDIR)$(bindir)/$(PROGRAM)
	$(RM) -rv $(DESTDIR)$(docdir)

.PHONY: clean
clean:
	@:

#	Makefile
#	Karl's random password generator
#
#	Karl V. P. B. `kvpb`  Karl Thomas George West `ktgw`
#	+33 A BB BB BB BB     +1 (DDD) DDD-DDDD
#	local-part@domain     local-part@domain
#	kvpb.fr
#	https://x.com/ktgwkvpb
#	https://github.com/kvpb
#
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

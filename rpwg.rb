#!/usr/bin/env ruby

set_character = [ #set_character_ascii
  "!", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0",
  "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">",
  "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
  "[", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i",
  "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
  "x", "y", "z", "{", "|", "}", "~"
] # ASCII order, no 032, '"', '\' or '#'.
#set_character_qwazerty = [
#  "!", "$", "%", "&", "'", "(", ")", "*", ",", "-", ".", "/", ":", ";",
#  "?", "@", "A", "M", "Q", "W", "Z", "[", "]", "^", "`", "a", "m", "q",
#  "w", "z", "{", "|", "}", "~"
#]
matrix_key = {
	"ANSI QWERTY" => [
    1,   4,   5,   7,  39,   9,  10,   8,  12,  49,  11,  50,  51,  10,
    1,   2,   3,   4,   5,   6,   7,   8,   9,  38,  38,  49,  12,  50,
   51,   2,  29,  46,  44,  31,  17,  32,  33,  34,  22,  35,  36,  37,
   48,  47,  23,  24,  15,  18,  30,  19,  21,  45,  16,  43,  20,  42,
   25,  26,   6,  11,   0,  29,  46,  44,  31,  17,  32,  33,  34,  22,
   35,  36,  37,  48,  47,  23,  24,  15,  18,  30,  19,  21,  45,  16,
   43,  20,  42,  25,  27,  26,   0
	],
	"Apple AZERTY" => [
    8,  26,  39,   1,   4,   5,  11,  26,  52,  49,  12,  50,  51,  10,
    1,   2,   3,   4,   5,   6,   7,   8,   9,  51,  50,  42,  52,  42,
   49,   0,  15,  47,  45,  31,  17,  32,  33,  34,  22,  35,  36,  37,
   38,  48,  23,  24,  29,  18,  30,  19,  21,  46,  43,  44,  20,  16,
    5,  11,  25,  12,  40,  15,  47,  45,  31,  17,  32,  33,  34,  22,
   35,  36,  37,  38,  48,  23,  24,  29,  18,  30,  19,  21,  46,  43,
   44,  20,  16,   5,  37,  11,  48
	]
#	"keyboard layout" => [
#     ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,
#     ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,
#     ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,
#     ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,
#     ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,
#     ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,
#     ,    ,    ,    ,    ,    ,    
#	],
} # Exploiting associative arrays enables me to more easily let users pick different layouts. Many QWERTY variants have sprung from the ANSI QWERTY, like the ACNOR QWERTY, even an AFNOR QWERTY. French AZERTY in turn got varied into Belgian AZERTY, AFNOR AZERTY... And these are only two layouts. Krauts [just kidding; love you guys --- cross that border more often, brothers] of course had to come up with QWERTZ. The best solution to me right now is an array of the set of characters with an associative array of key matrices of numbers from 0 to n in left-to-right, top-to-bottom script. Yes, it still reeks of the eighties, but hey...
#matrix_key_ansiqwerty = [
#    1,   4,   5,   7,  39,   9,  10,   8,  12,  49,  11,  50,  51,  10,
#    1,   2,   3,   4,   5,   6,   7,   8,   9,  38,  38,  49,  12,  50,
#   51,   2,  29,  46,  44,  31,  17,  32,  33,  34,  22,  35,  36,  37,
#   48,  47,  23,  24,  15,  18,  30,  19,  21,  45,  16,  43,  20,  42,
#   25,  26,   6,  11,   0,  29,  46,  44,  31,  17,  32,  33,  34,  22,
#   35,  36,  37,  48,  47,  23,  24,  15,  18,  30,  19,  21,  45,  16,
#   43,  20,  42,  25,  27,  26,   0
#]
#matrix_key_macfrazerty = [
#    8,  26,  39,   1,   4,   5,  11,  26,  52,  49,  12,  50,  51,  10,
#    1,   2,   3,   4,   5,   6,   7,   8,   9,  51,  50,  42,  52,  42,
#   49,   0,  15,  47,  45,  31,  17,  32,  33,  34,  22,  35,  36,  37,
#   38,  48,  23,  24,  29,  18,  30,  19,  21,  46,  43,  44,  20,  16,
#    5,  11,  25,  12,  40,  15,  47,  45,  31,  17,  32,  33,  34,  22,
#   35,  36,  37,  38,  48,  23,  24,  29,  18,  30,  19,  21,  46,  43,
#   44,  20,  16,   5,  37,  11,  48
#]
#matrix_key_layout = [
#     ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,
#     ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,
#     ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,
#     ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,
#     ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,
#     ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,    ,
#     ,    ,    ,    ,    ,    ,    
#]

puts `tput setaf 1` + """
RANDOM      PASSWORD     GENERATOR
   ,-----, ,-----,         ,-----,
  / /'/ / / /'/ / ,-,-,-, / /''-'
 / / | | / ,---' / / / / / /_/'/
'-'  '-''-'     '-----' '-----'
V  E  R  S  I  O  N     1  .  6  a""" + `tput sgr0` + "\n" * 2
print `tput setaf 1` + "Password length " + `tput smul` + "(digits only)" + `tput sgr0` + `tput setaf 1` + ":" + `tput sgr0` + " " + `tput setaf 3`
length_password = gets.to_i
print `tput sgr0`
print `tput setaf 1` + "QWAZERTY mode " + `tput smul` + "('y' for yes)" + `tput sgr0` + `tput setaf 1` + "?" + `tput sgr0` + " " + `tput setaf 3`
mode_qwazerty = gets
print `tput sgr0`

if mode_qwazerty =~ /(|^)y(|$)/i
	l = set_character.length
	intersection_set = Array.new( l )
	i = 0
	while i < l do
		print "#{i}\t#{set_character[ i ]}\t#{matrix_key['ANSI QWERTY'][ i ]}\t#{matrix_key['Apple AZERTY'][ i ]}\n" #print "#{i}\t#{set_character[ i ]}\t#{matrix_key_ansiqwerty[ i ]}\t#{matrix_key_macfrazerty[ i ]}\n"
		if matrix_key['ANSI QWERTY'][ i ] != matrix_key['Apple AZERTY'][ i ] #if matrix_key_macfrazerty[ i ] != matrix_key_ansiqwerty[ i ]
			print "\t\t#{matrix_key['ANSI QWERTY'][ i ]}\t#{matrix_key['Apple AZERTY'][ i ]}\n" #print "\t\t#{matrix_key_ansiqwerty[ i ]}\t#{matrix_key_macfrazerty[ i ]}\n" #print "#{i}\t#{set_character[ i ]}\t#{matrix_key_ansiqwerty[ i ]}\t#{matrix_key_macfrazerty[ i ]}\n"
			intersection_set << set_character[ i ]
		end
		i += 1
	end
	print "#{intersection_set}\n"
	intersection_set = set_character - intersection_set #set_character = set_character - set_character_qwazerty
	print "#{intersection_set}\n"
else
	intersection_set = set_character
	end
password = Array.new
while length_password > 0 do
	password << intersection_set.sample
	length_password -= 1
end

puts `tput setaf 1` + "Randomly generated password:" + `tput sgr0` + " " + password.map(&:inspect).join('').to_s.gsub('"', '') + "\n"
# ... And if you thought this code looks like shit, you're right, because it is! :D

#	rpwg.rb
#	Random Password Generator
#	1.6 alpha
#
#	Karl V. P. B. `kvpb`	Karl Thomas George West `ktgw`
#	+33 A BB BB BB BB		+1 (DDD) DDD-DDDD
#	local-part@domain		local-part@domain
#	kvpb.fr
#	https://x.com/ktgwkvpb
#	https://github.com/kvpb
#
#	'what a change come over me
#	you showed me what life could be
#	it's not grime like it used to be
#	mh look what you've done to me
#	oh I'm giving up for love
#	giving up the way that it used to be
#	I'm giving for love
#	love makes it easy for me
#	how can I go on each day
#	you took a part of me away
#	hand in hand we walk together
#	looks like you're in for stormy weather
#	oh I'm giving up for love
#	giving up the way that it used to be
#	I'm giving for love
#	love makes it easy for me
#	look what you've done to me
#	ain't like it used to be
#	all of my yesterdays are over, over
#	my life has just begun
#	you turn my world around
#	all of my yesterdays are over
#	oh I'm giving up, giving it up for love
#	giving up the way that it used to be
#	I'm givin', giving up, giving it up for love
#	love makes it easy for me
#	wish right now that I was free
#	let's love your offers not kept from me
#	loving you turned my head around
#	this love'll fan until ground above
#	oh I'm giving up for love
#	giving up the way that it used to be
#	I'm giving for love
#	love makes it easy for me
#	giving up for love
#	giving up the way that it used to be
#	I'm givin' for love
#	love makes it easy for me
#	giving up for love
#	ooh ooh giving up for love
#	giving up for love'

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

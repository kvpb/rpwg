#!/usr/bin/env ruby

character_set = [ "!", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~" ] # ASCII order, no 032, """, "\" or "#".
qwazerty_character_set = [ "!", "$", "%", "&", "'", "(", ")", "*", ",", "-", ".", "/", ":", ";", "?", "@", "A", "M", "Q", "W", "Z", "[", "]", "^", "`", "a", "m", "q", "w", "z", "{", "|", "}", "~" ]

puts `tput setaf 1` + """
RANDOM      PASSWORD     GENERATOR
   ,-----, ,-----,         ,-----,
  / /'/ / / /'/ / ,-,-,-, / /''-'
 / / | | / ,---' / / / / / /_/'/
'-'  '-''-'     '-----' '-----'
V  E  R  S  I  O  N     1  .  2  3""" + `tput sgr0` + "\n" * 2
print `tput setaf 1` + "Password length " + `tput smul` + "(digits only)" + `tput sgr0` + `tput setaf 1` + ":" + `tput sgr0` + " " + `tput setaf 3`
password_length = gets.to_i
print `tput sgr0`

print `tput setaf 1` + "QWAZERTY sensitivity " + `tput smul` + "('y' for yes)" + `tput sgr0` + `tput setaf 1` + "?" + `tput sgr0` + " " + `tput setaf 3`
qwazerty_sensitivity = gets
print `tput sgr0`

if qwazerty_sensitivity =~ /(|^)y(|$)/i
	character_set = character_set - qwazerty_character_set
else
	end

password = Array.new

while password_length > 0 do
	password << character_set.sample
	password_length -= 1
end

puts `tput setaf 1` + "Randomly generated password:" + `tput sgr0` + " " + password.map(&:inspect).join('').to_s.gsub('"', '') + "\n"

#	rpwg.rb
#	Random Password Generator
#	Version 1.23
#
#	Karl V. P. B. `kvpb`
#	+1 (DDD) DDD-DDDD
#	+33 A BB BB BB BB
#	local-part@domain
#	local-part@domain
#	https://www.linkedin.com/in/
#	https://twitter.com/
#	https://github.com/
#	https://vm.tiktok.com//
#
#	what a change come over me
#	you showed me what life could be
#	it's not grime like it used to be
#	mh look what you've done to me
#	
#	oh I'm giving up for love
#	giving up the way that it used to be
#	I'm giving for love
#	love makes it easy for me
#	
#	how can I go on each day
#	you took a part of me away
#	hand in hand we walk together
#	looks like you're in for stormy weather
#	
#	oh I'm giving up for love
#	giving up the way that it used to be
#	I'm giving for love
#	love makes it easy for me
#	
#	look what you've done to me
#	ain't like it used to be
#	all of my yesterdays are over, over
#	my life has just begun
#	you turn my world around
#	all of my yesterdays are over
#	
#	oh I'm giving up, giving it up for love
#	giving up the way that it used to be
#	I'm givin', giving up, giving it up for love
#	love makes it easy for me
#	
#	wish right now that I was free
#	let's love your offers not kept from me
#	loving you turned my head around
#	this love'll fan until ground above
#	
#	oh I'm giving up for love
#	giving up the way that it used to be
#	I'm giving for love
#	love makes it easy for me
#	
#	giving up for love
#	giving up the way that it used to be
#	I'm givin' for love
#	love makes it easy for me
#	
#	giving up for love
#	ooh ooh giving up for love
#	giving up for love

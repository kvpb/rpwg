#!/usr/bin/env ruby

character_set = [ "!", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~" ] # ASCII order, no 032, """, "\" or "#".
bad_character_set = [ "!", "$", "%", "&", "'", "(", ")", "*", ",", "-", ".", "/", ":", ";", "?", "@", "A", "M", "Q", "W", "Z", "[", "]", "^", "`", "a", "m", "q", "w", "z", "{", "|", "}", "~" ]

puts """
RANDOM      PASSWORD     GENERATOR
   ,-----, ,-----,         ,-----,
  / /'/ / / / / / ,-,-,-, / /''-'
 / / | | / ,---' / / / / / /_/'/
'-'  '-''-'     '-----' '-----'
V  E  R  S  I  O  N     1  .  0  1

Enter the password's length (in arabic numbers)."""
password_length = gets.to_i

puts "\nShall the password be qwazerty sensitive (\"yes\" or \"no\") ?"
password_type = gets

if password_type =~ /(|^)yes(|$)/i
	character_set = character_set - bad_character_set
else
	end

password = Array.new

while password_length > 0 do
	password << character_set.sample
	password_length -= 1
end

puts "\n" + password.map(&:inspect).join('').to_s.gsub('"', '') + "\n" + "\n" + "\n"

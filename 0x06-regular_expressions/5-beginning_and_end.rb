#!/usr/bin/env ruby
#Matches exactly a string that starts with h, ends with n n.
puts ARGV[0].scan(/^h.n$/).join

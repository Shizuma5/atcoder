n = gets.chomp.to_i
s = gets.chomp

s_2 = s.gsub(/^\.+/, '').gsub(/#+$/, '')
white = s_2.count('.')

black = n - s_2

if white <= black
    puts white
else
    puts black
end

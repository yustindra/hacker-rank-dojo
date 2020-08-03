def serial_average(str)
    s = str.split("-")
    avg = (((s[1].to_f) + (s[2].to_f))/2).round(2)
    return "#{s[0]}" + "-" + "#{avg}"
end

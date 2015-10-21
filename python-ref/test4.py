string_formatter = "%r %r %r %r"

print string_formatter % ("time", "is", "running", "out")
print string_formatter % ("time", "is", 500, "right now")
print string_formatter % (string_formatter, string_formatter, string_formatter, string_formatter)

# `and` has a higher priority than `or`
truthy_integer = False or 5 and 100  # 100 beacuse 5 is truthy so it returns 100
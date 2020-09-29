seconds = int(input("Input time as seconds: "))

hours = seconds // 3600
seconds -= hours * 3600

minutes = seconds // 60
seconds -= minutes * 60

print(f"{'%.2d' % hours}:{'%.2d' % minutes}:{'%.2d' % seconds}")
text = "show must go on"

for key, word in enumerate(text.split(" ")):
    print("%d:%s" % (key, word[:10]))

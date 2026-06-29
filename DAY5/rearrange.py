values={'a':21,'b':25,'c':19}

sortbyvalue=dict(sorted(values.items(), key=lambda item: item[1]))
print(sortbyvalue)

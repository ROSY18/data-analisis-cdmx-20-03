print("-" * 21)
print("Tabla de verdad")
print("-" * 21)
print("{:5} | {:5} | {:5}".format("A", "B", "A & B"))
print("{:5} | {:5} | {:5}".format(True, True, True and True))
print("{:5} | {:5} | {:5}".format(True, False, True and False))
print("{:5} | {:5} | {:5}".format(False, True, False and True))
print("{:5} | {:5} | {:5}".format(True, False, True and False))
print("{:5} | {:5} | {:5}".format(False, False, False and False))
print("-" * 21)
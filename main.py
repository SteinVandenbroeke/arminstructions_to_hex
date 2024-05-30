from keystone import *


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

    # Initialize Keystone engine for ARM64
ks = Ks(KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN)
#write code in https://godbolt.org/z/54aW9M1T9
# Assembly code

inserted_code = """
test:
  mov x0, #42
  RET
"""

assembly_code = inserted_code

# Assemble the code
encoding, count = ks.asm(assembly_code)

newList = list(divide_chunks(encoding, 4))
print (newList)

charCounter = 0
print("{", end="")
for instruction in newList:
    instruction.reverse()
    print("0x", end="")
    for numberOfInstruction in instruction:
        print(format(numberOfInstruction, '02X'), end='')
    print(",", end="")
print("}")
from assembler import assembler
    
with open("assembler_in.txt", "r") as asso:
    ass = asso.read()
    code = ass.splitlines()

with open("assembler_out.txt", "w") as assi:
    for addr in code:
        assi.write(str(assembler(str(addr))))
        assi.write(", ")
    
    assi.seek(assi.tell() - 2)
    assi.truncate()

print("Assembled succesfully")
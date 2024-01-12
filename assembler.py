def assembler(instruction):
    if len(instruction.split()) == 2:
        opcode, parameter = instruction.split()
        parameter = int(parameter)
    else:
        opcode = instruction

    if opcode == "NOP":
        return hex(0x000000)
    if opcode == "LDA":
        return hex(0x010000 + parameter)
    if opcode == "LDB":
        return hex(0x020000 + parameter)
    if opcode == "LDC":
        return hex(0x030000 + parameter)
    if opcode == "LDA_D":
        return hex(0x040000)
    if opcode == "LDB_D":
        return hex(0x050000)
    if opcode == "LDC_D":
        return hex(0x060000)
    if opcode == "STA":
        return hex(0x070000 + parameter)
    if opcode == "STB":
        return hex(0x080000 + parameter)
    if opcode == "STC":
        return hex(0x090000 + parameter)
    if opcode == "STA_D":
        return hex(0x0a0000)
    if opcode == "STB_D":
        return hex(0x0b0000)
    if opcode == "STC_D":
        return hex(0x0c0000)
    if opcode == "STI":
        return hex(0x0d0000 + parameter)
    if opcode == "IDA":
        return hex(0x0e0000 + parameter)
    if opcode == "IDB":
        return hex(0x0f0000 + parameter)
    if opcode == "IDC":
        return hex(0x100000 + parameter)
    if opcode == "ATB":
        return hex(0x110000)
    if opcode == "ATC":
        return hex(0x120000)
    if opcode == "BTA":
        return hex(0x130000)
    if opcode == "BTC":
        return hex(0x140000)
    if opcode == "CTA":
        return hex(0x150000)
    if opcode == "CTB":
        return hex(0x160000)
    if opcode == "PCA":
        return hex(0x170000)
    if opcode == "PCB":
        return hex(0x180000)
    if opcode == "PCC":
        return hex(0x190000)
    if opcode == "PUSHA":
        return hex(0x1a0000)
    if opcode == "PUSHB":
        return hex(0x1b0000)
    if opcode == "PUSHC":
        return hex(0x1c0000)
    if opcode == "PUSHI":
        return hex(0x1d0000 + parameter)
    if opcode == "PUSHM":
        return hex(0x1e0000 + parameter)
    if opcode == "PUSHM_D":
        return hex(0x1f0000)
    if opcode == "POPA":
        return hex(0x200000)
    if opcode == "POPB":
        return hex(0x210000)
    if opcode == "POPC":
        return hex(0x220000)
    if opcode == "POPM":
        return hex(0x230000 + parameter)
    if opcode == "POPM_D":
        return hex(0x240000)
    if opcode == "ADD":
        return hex(0x250000)
    if opcode == "SUB":
        return hex(0x260000)
    if opcode == "MUL":
        return hex(0x270000)
    if opcode == "DIV":
        return hex(0x280000)
    if opcode == "MOD":
        return hex(0x290000)
    if opcode == "SHL":
        return hex(0x2a0000)
    if opcode == "SHR":
        return hex(0x2b0000)
    if opcode == "AND":
        return hex(0x2c0000)
    if opcode == "OR":
        return hex(0x2d0000)
    if opcode == "XOR":
        return hex(0x2e0000)
    if opcode == "CMP":
        return hex(0x2f0000)
    if opcode == "ADDI":
        return hex(0x300000 + parameter)
    if opcode == "SUBI":
        return hex(0x310000 + parameter)
    if opcode == "MULI":
        return hex(0x320000 + parameter)
    if opcode == "DIVI":
        return hex(0x330000 + parameter)
    if opcode == "MODI":
        return hex(0x340000 + parameter)
    if opcode == "SHLI":
        return hex(0x350000 + parameter)
    if opcode == "SHRI":
        return hex(0x360000 + parameter)
    if opcode == "ANDI":
        return hex(0x370000 + parameter)
    if opcode == "ORI":
        return hex(0x380000 + parameter)
    if opcode == "XORI":
        return hex(0x390000 + parameter)
    if opcode == "CMPI":
        return hex(0x3a0000 + parameter)
    if opcode == "ADD_NA":
        return hex(0x3b0000)
    if opcode == "SUB_NA":
        return hex(0x3c0000)
    if opcode == "MUL_NA":
        return hex(0x3d0000)
    if opcode == "DIV_NA":
        return hex(0x3e0000)
    if opcode == "MOD_NA":
        return hex(0x3f0000)
    if opcode == "SHL_NA":
        return hex(0x400000)
    if opcode == "SHR_NA":
        return hex(0x410000)
    if opcode == "AND_NA":
        return hex(0x420000)
    if opcode == "OR_NA":
        return hex(0x430000)
    if opcode == "XOR_NA":
        return hex(0x440000)
    if opcode == "RNG":
        return hex(0x450000 + parameter)
    if opcode == "ADDM_D":
        return hex(0x460000)
    if opcode == "SUBM_D":
        return hex(0x470000)
    if opcode == "MULM_D":
        return hex(0x480000)
    if opcode == "DIVM_D":
        return hex(0x490000)
    if opcode == "MODM_D":
        return hex(0x4a0000)
    if opcode == "SHLM_D":
        return hex(0x4b0000)
    if opcode == "SHRM_D":
        return hex(0x4c0000)
    if opcode == "ANDM_D":
        return hex(0x4d0000)
    if opcode == "ORM_D":
        return hex(0x4e0000)
    if opcode == "XORM_D":
        return hex(0x4f0000)
    if opcode == "CMPM_D":
        return hex(0x500000)
    if opcode == "JMP":
        return hex(0x510000 + parameter)
    if opcode == "JNZ":
        return hex(0x520000 + parameter)
    if opcode == "JNC":
        return hex(0x530000 + parameter)
    if opcode == "JNN":
        return hex(0x540000 + parameter)
    if opcode == "JML":
        return hex(0x550000 + parameter)
    if opcode == "JME":
        return hex(0x560000 + parameter)
    if opcode == "JMG":
        return hex(0x570000 + parameter)
    if opcode == "JMPL":
        return hex(0x580000 + parameter)
    if opcode == "JMNZ":
        return hex(0x590000 + parameter)
    if opcode == "JMNC":
        return hex(0x5a0000 + parameter)
    if opcode == "JMNN":
        return hex(0x5b0000 + parameter)
    if opcode == "JMGE":
        return hex(0x5c0000 + parameter)
    if opcode == "JMNE":
        return hex(0x5d0000 + parameter)
    if opcode == "JMLE":
        return hex(0x5e0000 + parameter)
    if opcode == "JMP_D":
        return hex(0x5f0000)
    if opcode == "JNZ_D":
        return hex(0x600000)
    if opcode == "JNC_D":
        return hex(0x610000)
    if opcode == "JNN_D":
        return hex(0x620000)
    if opcode == "JML_D":
        return hex(0x630000)
    if opcode == "JME_D":
        return hex(0x640000)
    if opcode == "JMG_D":
        return hex(0x650000)
    if opcode == "JMPL_D":
        return hex(0x660000)
    if opcode == "JMNZ_D":
        return hex(0x670000)
    if opcode == "JMNC_D":
        return hex(0x680000)
    if opcode == "JMNN_D":
        return hex(0x690000)
    if opcode == "JMGE_D":
        return hex(0x6a0000)
    if opcode == "JMNE_D":
        return hex(0x6b0000)
    if opcode == "JMLE_D":
        return hex(0x6c0000)
    if opcode == "DV0":
        return hex(0x6d0000)
    if opcode == "DV1":
        return hex(0x6e0000)
    if opcode == "DV2":
        return hex(0x6f0000)
    if opcode == "DV3":
        return hex(0x700000)
    if opcode == "OUTA":
        return hex(0x710000)
    if opcode == "OUTB":
        return hex(0x720000)
    if opcode == "OUTC":
        return hex(0x730000)
    if opcode == "OUTM":
        return hex(0x740000 + parameter)
    if opcode == "OUTM_D":
        return hex(0x750000)
    if opcode == "DLY":
        return hex(0x760000 + parameter)
    if opcode == "INA":
        return hex(0x770000)
    if opcode == "INB":
        return hex(0x780000)
    if opcode == "INC":
        return hex(0x790000)
    if opcode == "INM":
        return hex(0x7a0000 + parameter)
    if opcode == "INM_D":
        return hex(0x7b0000)
    if opcode == "DLY_D":
        return hex(0x7c0000)
    if opcode == "OUTPS":
        return hex(0x7d0000)
    if opcode == "INPS":
        return hex(0x7e0000)
    if opcode == "HALT":
        return hex(0x7f0000)
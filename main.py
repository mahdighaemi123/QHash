import string

CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
hash_key = [[1, 0, 1, 1, 1, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0, 0, 0], [1, 0, 1, 1, 1, 1, 0, 1],
            [0, 0, 0, 1, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0], [1, 1, 0, 1, 1, 1, 0, 0], [1, 0, 1, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0, 1, 0], [0, 1, 0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0, 1],
            [1, 1, 0, 1, 1, 0, 0, 0], [1, 0, 1, 1, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1, 0, 1]]


def baseChanger(num: string, fromBase: string, toBase: int) -> string:
    return base10ToNewBase(oldBaseTo10Base(num, fromBase), toBase)


def base10ToNewBase(num, base) -> string:
    final = ""
    num = int(num)
    base = int(base)
    while 1:

        final = str(CHARS[num % base]) + final
        num = num // base

        if num == 0:
            return final


def oldBaseTo10Base(num, base) -> string:
    num = str(num).upper()
    base = int(base)
    num = num[::-1]

    final = 0
    for i in range(0, len(num)):
        final += int(CHARS.find(num[i])) * base ** i

    return final


def Hash(inter: string) -> string:
    inter = str(inter)
    inter = mixed_up(inter)

    inters = list(inter)
    inters_byte = []

    for a in inters:
        a = a.encode("utf-8")

        for b in a:
            b = base10ToNewBase(b, 2)

            b = list(b)
            b = list_string_list_int(b)

            inters_byte.append(b)

    x = integrate_hash_list(inters_byte)
    final = list_byte_list_string(x)
    final = mixed_up(final)

    return final


def integrate_hash_list(a):
    final = hash_key.copy()

    for index, a_byte in enumerate(a):
        hash_starter_index = index - (index // len(final) * len(final))
        hash_starter_byte = final[hash_starter_index]

        final[hash_starter_index] = integrate_byte(a_byte, hash_starter_byte)

    return final


def mixed_up(a):
    a = list(a)
    b = list_byte_sum_chr_code(a)
    b = b - b // len(a) * len(a)

    for i in range(0, b):
        a += [a.pop(i)]

    return list_to_string(a)


def list_bit_string(inter):
    final = ""

    for i in inter:
        final += str(i)

    return final


def list_byte_list_string(inter):
    final = ""

    for i in inter:
        my_byte = int(baseChanger(list_to_string(i), 2, 10))
        my_byte = my_byte - my_byte // 36 * 36
        final += baseChanger(my_byte, 10, 36)

    return final


def list_byte_sum_chr_code(inter):
    final = 0

    for index, letter in enumerate(inter):
        final += (ord(letter) + index) * index

    return final


def string_sum_chr_code(inter):
    final = 0

    for i in inter:
        final += ord(i)

    return final


def integrate_byte(a, b):
    final = []

    if len(a) > len(b):

        for index, bit in enumerate(b):
            final.append(int_xor(bit, a[index]))

        for index in range(len(a) - (len(a) - len(b)), len(a)):
            final.append(a[index])

    else:

        for index, bit in enumerate(a):
            final.append(int_xor(bit, b[index]))

        for index in range(len(b) - (len(b) - len(a)), len(b)):
            final.append(b[index])

    return final


def list_string_list_int(inters):
    final = []

    for inter in inters:
        final.append(int(inter))

    return final


def list_to_string(inter):
    final = ""
    for i in inter:
        final += str(i)

    return final


def int_xor(a, b):
    return 1 if bool(a) ^ bool(b) else 0


# Hashing "QHash" String
hashed = Hash("QHash")
print(f"Hashed -> {hashed}")

# AES irreducible polynomial: x^8 + x^4 + x^3 + x + 1 = 0x11B
MOD_POLY = 0x11B

def hex_to_polynomial(hex_str):
    num = int(hex_str, 16)
    terms = []
    for i in range(8):
        if (num >> i) & 1:
            if i == 0:
                terms.append("1")
            elif i == 1:
                terms.append("x")
            else:
                terms.append(f"x^{i}")
    terms.reverse()
    return " + ".join(terms) if terms else "0"

def to_binary_str(hex_str):
    num = int(hex_str, 16)
    return f"{num:08b}"

def gf_mult(a, b):
    result = 0
    for i in range(8):
        if (b & 1):
            result ^= a  # XOR is addition in GF(2)
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set:
            a ^= MOD_POLY
        a &= 0xFF
        b >>= 1
    return result

# Main script
while True:
    hex1 = input("Enter first hex value (or 'q' to quit): ").strip()
    if hex1.lower() == 'q':
        break
    hex2 = input("Enter second hex value: ").strip()
    try:
        a = int(hex1, 16)
        b = int(hex2, 16)
        product = gf_mult(a, b)
        product_hex = f"{product:02X}"

        print(f"\nInput 1:")
        print(f"  Hex       : {hex1.upper()}")
        print(f"  Polynomial: {hex_to_polynomial(hex1)}")
        print(f"  Binary    : {to_binary_str(hex1)}")

        print(f"\nInput 2:")
        print(f"  Hex       : {hex2.upper()}")
        print(f"  Polynomial: {hex_to_polynomial(hex2)}")
        print(f"  Binary    : {to_binary_str(hex2)}")

        print(f"\nGF(2^8) Product:")
        print(f"  Hex       : {product_hex}")
        print(f"  Polynomial: {hex_to_polynomial(product_hex)}")
        print(f"  Binary    : {to_binary_str(product_hex)}\n")

    except ValueError:
        print("Invalid input! Please enter valid 2-digit hex numbers (00 to FF).\n")

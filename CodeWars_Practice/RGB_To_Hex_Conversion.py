"""The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""

def rgb(ri, gi, bi):
    r = 255 if ri > 255 else 0 if ri < 0 else ri
    print(r)
    g = 255 if gi > 255 else 0 if gi < 0 else gi
    print(g)
    b = 255 if bi > 255 else 0 if bi < 0 else bi
    print(b)
    hex = {
        0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8",
        9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F",
    }
    # The line `r = hex[r//16] + hex[r%16]` is converting the decimal value of the red color component
    # `r` into its hexadecimal representation.
    r = hex[r//16] + hex[r%16]
    print(r); print(hex)
    g = hex[g//16] + hex[g%16]
    b = hex[b//16] + hex[b%16]
    return r+g+b

if __name__ == "__main__":
    print(rgb(255, 0, 255))
    print(rgb(-20, 275, 125))



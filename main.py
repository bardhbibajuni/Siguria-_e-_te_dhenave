BASE64_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def encode(text):

    data = text.encode("utf-8")

    result = ""

    for i in range(0, len(data), 3):

        block = data[i:i + 3]

        byte1 = block[0]
        byte2 = block[1] if len(block) > 1 else 0
        byte3 = block[2] if len(block) > 2 else 0

        combined = (byte1 << 16) | (byte2 << 8) | byte3



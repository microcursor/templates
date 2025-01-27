import uuid


ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def base58_encode(data: bytes) -> str:
    num = int.from_bytes(data, byteorder="big")
    encoded = []
    while num > 0:
        num, rem = divmod(num, 58)
        encoded.append(ALPHABET[rem])
    return ''.join(reversed(encoded))

def generate_base58_uuid() -> str:
    unique_id = uuid.uuid4()
    base58_id = base58_encode(unique_id.bytes)
    return f"template-{base58_id}"

short_uuid = generate_base58_uuid()
print(short_uuid)

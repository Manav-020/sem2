def decode_ways(self, index=0, current_decoding="", results=None):
    if results is None:
        results = []

    # Base case: If we've reached the end of the string, add the decoding to results
    if index == len(self):
        results.append(current_decoding)
        return

    # Take one digit and decode it if it's between 1 and 9
    num1 = int(self[index])
    if 1 <= num1 <= 9:
        decode_ways(self, index + 1, current_decoding + chr(num1 + 64), results)

    # Take two digits and decode if it's between 10 and 26
    if index + 1 < len(self):
        num2 = int(self[index:index + 2])
        if 10 <= num2 <= 26:
            decode_ways(self, index + 2, current_decoding + chr(num2 + 64), results)

    return results

# Input from user
encoded_message = input("Enter encoded message: ")
decoded_messages = decode_ways(encoded_message)
print("Possible Decodings:")
for msg in decoded_messages:
    print(msg)
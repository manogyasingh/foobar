from base64 import b64decode as b6

message='''FkYdGgQaBAAaSUdSU1IVCwQPB09BQUkMCBUNFggJEg1UVUhZRgsAHAgEAwoDXk1TTgsBDhwHBgpG
TklISggADBUcBRoLAgJPX1VVGAIGGg0bBAMKCQ1GU1NOQB0dGR0aCgsXT0FBSR0GGwMaHR1ASElV
VQoACBZPQUFJCQgWRlNTTkAfGhtTXhw='''

key="manogyasinghsuryansh"
res=""

for i, c in enumerate(b6(message)):
    res+=(chr(c ^ ord(key[i % len(key)])))

print(res)

[![Build Status](https://travis-ci.com/olagrottvik/encdec8b10b.svg?token=jVu3gMDvjaqfNCVgNVai&branch=master)](https://travis-ci.com/olagrottvik/encdec8b10b)

# encdec8b10b

Encode and decode 8B10B encoding

## Get

```
python3 -m pip install encdec8b10b
```

## Usage

### Encode Data Byte
```
from encdec8b10b import EncDec8B10B

running_disp = 0
byte_to_enc = 0xf
running_disp, encoded = EncDec8B10B.enc_8b10b(byte_to_enc, running_disp)
print(hex(encoded))
Output >> 0xba
```
### Encode Control Byte
```
from encdec8b10b import EncDec8B10B

running_disp = 0
byte_to_enc = 0xbc # comma
ctrl = 1
running_disp, encoded = EncDec8B10B.enc_8b10b(byte_to_enc, running_disp, ctrl)
print(hex(encoded))
Output >> 0x17c
```
### Decode Data Byte
```
from encdec8b10b import EncDec8B10B

byte_to_dec = 0xba
ctrl, decoded = EncDec8B10B.dec_8b10b(byte_to_dec)
print(hex(decoded))
Output >> 0xf
# ctrl variable confirm that it was a data byte
print(ctrl)
Output >> 0
```
### Decode Control Byte
```
from encdec8b10b import EncDec8B10B

byte_to_dec = 0x17c # comma encoded
ctrl, decoded = EncDec8B10B.dec_8b10b(byte_to_dec)
print(hex(decoded))
Output >> 0xbc
# ctrl variable confirm that it was a control byte
print(ctrl)
Output >> 1
```
 
 ### Verbosity
 Both functions have a verbose-mode to make it easier to confirm everything that's happening:
```
from encdec8b10b import EncDec8B10B

running_disp = 0
byte_to_enc = 0xA0
running_disp, encoded = EncDec8B10B.enc_8b10b(byte_to_enc, running_disp, verbose=True)

Output >> Encoder - In: A0 - Encoded: 146 - Running Disparity: 0

ctrl, decoded = EncDec8B10B.dec_8b10b(encoded, verbose=True)

Output >> Decoded: A0 - Control: 0
```

 
 ## 8B10B
 8B10B Encoding were implemented by Al Widmer and Peter Franaszek in 1983. It is still widely used in high-speed electronics.

- [Original article](https://ieeexplore.ieee.org/document/5390392)
- [Wikipedia](https://en.wikipedia.org/wiki/8b/10b_encoding)


### Thanks
- [Ryu Shinhyung](https://opencores.org/projects/async_8b10b_encoder_decoder) for creating the tables used in this module
- [Chuck Benz](http://asics.chuckbenz.com/) for creating awesome combinational 8B10B modules
- [Alex Forencich](http://www.alexforencich.com/wiki/en/scripts/matlab/enc8b10b)  for his 8B10B Matlab script
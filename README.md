# encdec8b10b

Encode and decode 8B10B encoding

## Usage

### Encode Data Byte
```
from encdec8b10b import EncDec8B10B

running_disp = 0
byte_to_enc = 0xf
running_disp, encoded = EncDec8B10B.enc_8b10b(byte_to_enc, running_disp)
print(hex(encoded))
0xba
```
### Encode Control Byte
```
from encdec8b10b import EncDec8B10B

running_disp = 0
byte_to_enc = 0xbc # comma
ctrl = 1
running_disp, encoded = EncDec8B10B.enc_8b10b(byte_to_enc, running_disp, ctrl)
print(hex(encoded))
0x17c
```
### Decode Data Byte
```
from encdec8b10b import EncDec8B10B

byte_to_dec = 0xba
ctrl, decoded = EncDec8B10B.dec_8b10b(byte_to_dec)
print(hex(decoded))
0xf
# ctrl variable confirm that it was a data byte
print(ctrl)
0
```
### Decode Control Byte
```
from encdec8b10b import EncDec8B10B

byte_to_dec = 0x17c # comma encoded
ctrl, decoded = EncDec8B10B.dec_8b10b(byte_to_dec)
print(hex(decoded))
0xbc
# ctrl variable confirm that it was a control byte
print(ctrl)
1
```
 
 ### Verbosity
 Both functions have a verbose-mode to make it easier to confirm everything that's happening:
```
from encdec8b10b import EncDec8B10B

running_disp = 0
byte_to_enc = 0xA0
running_disp, encoded = EncDec8B10B.enc_8b10b(byte_to_enc, running_disp, verbose=True)
Encoder - In: A0 - Encoded: 146 - Running Disparity: 0

ctrl, decoded = EncDec8B10B.dec_8b10b(encoded, verbose=True)
Decoded: A0 - Control: 0
```

 
 ## 8B10B
 8B10B Encoding were implemented by Al Widmer and Peter Franaszek in 1983. It is still widely used in high-speed electronics.

- [Original article](https://ieeexplore.ieee.org/document/5390392)
- [Wikipedia](https://en.wikipedia.org/wiki/8b/10b_encoding)


### Thanks
- [Ryu Shinhyung](https://opencores.org/projects/async_8b10b_encoder_decoder) for creating the tables used in this module
- [Chuck Benz](http://asics.chuckbenz.com/) for creating awesome combinatorial 8B10B modules
- [Alex Forencich](http://www.alexforencich.com/wiki/en/scripts/matlab/enc8b10b)  for his 8B10B Matlab script
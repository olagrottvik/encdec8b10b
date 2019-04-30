# -*- coding: utf-8 -*-

from .context import encdec8b10b
from encdec8b10b import EncDec8B10B
import random

import unittest

verbose = True  # Set to True to get test output

class TestSuite(unittest.TestCase):
    """All test cases"""

    def test_comma(self):
        print("Testing K28.5 Comma...")
        running_disparity = 0

        test_data = 0xBC
        test_ctrl = 1
        running_disparity, data_encoded = EncDec8B10B.enc_8b10b(test_data, running_disparity, test_ctrl, verbose)
        ctrl, data_decoded = EncDec8B10B.dec_8b10b(data_encoded, verbose)
        running_disparity, data_encoded = EncDec8B10B.enc_8b10b(data_decoded, running_disparity, 1, verbose)
        ctrl, data_decoded = EncDec8B10B.dec_8b10b(data_encoded, verbose)

        assert data_decoded == test_data and ctrl == test_ctrl, "K28.5 Comma Test Failed"

    def test_known_seq(self):
        print("Testing Known Sequence...")
                
        known_seq = [0xa0, 0x7a, 0xFF, 0xc2, 0x48, 0xda, 0x1b, 0x2e, 0x1f, 0x5b, 0xa5, 0x20, 0xb6, 0x10, 0xc3, 0x4d, 0xa0, 0x17, 0x83,
                     0x3b, 0x2e, 0x7d, 0x61, 0x73, 0x4d, 0xc5, 0x42, 0x59, 0x45, 0x7c, 0x12, 0x1c, 0x03, 0x52, 0xdd, 0x30, 0xa5]
        encoded_seq = [0x146, 0xda, 0x235, 0x1ad, 0x298, 0x19a, 0x9b, 0x24e, 0xb5, 0x29b, 0x165, 0x246, 0x156, 0xb6, 0x1a3, 0x28d, 0x179, 0x368, 0x123,
                       0x25b, 0x24e, 0xe2, 0x32e, 0x313, 0x28d, 0x1a5, 0x292, 0x299, 0x2a5, 0x0dc, 0x372, 0x9c, 0x363, 0x2b2, 0x1a2, 0x276, 0x165]
        result_encoded = list()
        result_decoded = list()

        # Manually set running disparity to known start
        running_disparity = 1
        test_ctrl = 0

        for byte, encoded in zip(known_seq, encoded_seq):
            running_disparity, data_encoded = EncDec8B10B.enc_8b10b(byte, running_disparity, test_ctrl, verbose)
            assert data_encoded == encoded, "Data Encoded (0x{:03X}) does not match known sequence (0x{:03X})".format(data_encoded, encoded)
            ctrl, data_decoded = EncDec8B10B.dec_8b10b(data_encoded, verbose)
            assert data_decoded == byte, "Data Decoded (0x{:02X}) does not match input byte (0x{:02X})".format(data_decoded, byte)

    def test_rand_seq(self):
        print("Testing Random Data Sequence...")
        test_ctrl = 0

        running_disparity = 0
        for i in range(100000):
            rand_byte = random.randint(0, 0xFF)
            running_disparity, data_encoded = EncDec8B10B.enc_8b10b(rand_byte, running_disparity, test_ctrl, verbose)
            ctrl, data_decoded = EncDec8B10B.dec_8b10b(data_encoded, verbose)
            assert rand_byte == data_decoded, "Data Decoded (0x{:02X}) does not match input byte (0x{:02X})".format(data_decoded, rand_byte)

        running_disparity = 1
        for i in range(100000):
            rand_byte = random.randint(0, 0xFF)
            running_disparity, data_encoded = EncDec8B10B.enc_8b10b(rand_byte, running_disparity, test_ctrl, verbose)
            ctrl, data_decoded = EncDec8B10B.dec_8b10b(data_encoded, verbose)
            assert rand_byte == data_decoded, "Data Decoded (0x{:02X}) does not match input byte (0x{:02X})".format(data_decoded, rand_byte)

    def test_ctrl_symbol(self):
        print("Testing All Control symbols...")
        test_ctrl = 1
        ctrl_symbols = [0x1c, 0x3c, 0x5c, 0x7c, 0x9c,
                        0xbc, 0xdc, 0xfc, 0xf7, 0xfb, 0xfd, 0xfe]

        running_disparity = 0
        for symbol in ctrl_symbols:
            running_disparity, data_encoded = EncDec8B10B.enc_8b10b(
                symbol, running_disparity, test_ctrl, verbose)
            ctrl, data_decoded = EncDec8B10B.dec_8b10b(data_encoded, verbose)
            assert symbol == data_decoded, "Data Decoded (0x{:02X}) does not match input byte (0x{:02X})".format(
                data_decoded, symbol)

        running_disparity = 1
        for symbol in ctrl_symbols:
            running_disparity, data_encoded = EncDec8B10B.enc_8b10b(symbol, running_disparity, test_ctrl, verbose)
            ctrl, data_decoded = EncDec8B10B.dec_8b10b(data_encoded, verbose)
            assert symbol == data_decoded, "Data Decoded (0x{:02X}) does not match input byte (0x{:02X})".format(data_decoded, symbol)


if __name__ == '__main__':
    unittest.main()

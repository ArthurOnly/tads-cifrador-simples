from django.test import SimpleTestCase

from backend.apps.cipher.business import CipherHandler


class CipherUnitTest(SimpleTestCase):
    def cipher_and_decipher_works(self):
        cipher = CipherHandler("hellz", [1, 2, 3])
        enc = cipher.encrypt()

        cipher = CipherHandler(enc, [1, 2, 3])
        dec = cipher.decrypt()

        self.assertEqual(dec, "hellz")

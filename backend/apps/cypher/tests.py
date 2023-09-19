from django.test import SimpleTestCase

from backend.apps.cypher.business import CypherHandler


class CypherUnitTest(SimpleTestCase):
    def cypher_and_decypher_works(self):
        cypher = CypherHandler("hellz", [1, 2, 3])
        enc = cypher.encrypt()

        cypher = CypherHandler(enc, [1, 2, 3])
        dec = cypher.decrypt()

        self.assertEqual(dec, "hellz")

import unittest
import script


class TestSum(unittest.TestCase):

    def test(self):
        stringToParse = "\"hola\""
        self.assertEqual(["hola"], script.parseJson(stringToParse))
        stringToParse = "\"hola\", 10"
        self.assertEqual(["hola", 10], script.parseJson(stringToParse))
        stringToParse = "\"hola\", null, 10, false"
        self.assertEqual(["hola", None, 10, False], script.parseJson(stringToParse))
        stringToParse = "\"hola\", 10, [10]"
        self.assertEqual(["hola", 10, [10]], script.parseJson(stringToParse))
        stringToParse = "\"hola\", 10, [10, \"hola\"]"
        self.assertEqual(["hola", 10, [10, "hola"]], script.parseJson(stringToParse))
        stringToParse = "\"hola\", 10, {\"hola\": \"aaaa\", \"adios\":10}"
        self.assertEqual(["hola", 10, {"hola": "aaaa", "adios": 10}], script.parseJson(stringToParse))
        stringToParse = "\"hola\", 10, [10, {\"hola\": \"aaaa\", \"adios\":10}]"
        self.assertEqual(["hola", 10, [10, {"hola": "aaaa", "adios": 10}]], script.parseJson(stringToParse))


if __name__ == '__main__':
    unittest.main()

import doctest
import unittest

znaki_s = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.',
           '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}


class Passwd:
    """
    >>> Passwd.validPasswd("shsh")
    False
    >>> Passwd.validPasswd("345")
    False
    >>> Passwd.validPasswd("Shshdddd")
    False
    >>> Passwd.validPasswd("Shshddd9")
    False
    >>> Passwd.validPasswd("Shsh?dd9")
    True
    """

    @staticmethod
    def validPasswd(passwd):

        znak_s = 0
        duza_litera = 0
        cyfra = 0

        if len(passwd) < 8:
            return False
        if type(passwd) is not str:
            return False

        for literka in passwd:
            if literka.isupper() == True:
                duza_litera = 1
            elif literka in znaki_s:
                znak_s = 1
            elif literka.isnumeric() == True:
                cyfra = 1

        if cyfra == 1 and znak_s == 1 and duza_litera == 1:
            return True
        if cyfra == 0:
            return False
        if znak_s == 0:
            return False
        else:
            return False


class PasswordTest(unittest.TestCase):

    def setUp(self):
        self.temp = Passwd()

    def test_1(self):
        self.assertEqual(False, self.temp.validPasswd("shsh"))

    def test_2(self):
        self.assertEqual(False, self.temp.validPasswd("345"))

    def test_3(self):
        self.assertEqual(False, self.temp.validPasswd("Shshdddd"))

    def test_4(self):
        self.assertEqual(False, self.temp.validPasswd("Shshddd9"))

    def test_5(self):
        self.assertEqual(True, self.temp.validPasswd("Shsh?dd9"))

    def tearDown(self):
        self.temp = None


if __name__ == "__main__":
    doctest.testmod()

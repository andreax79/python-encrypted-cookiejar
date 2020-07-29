#!/usr/bin/env python

import os
import os.path
import sys
import random
import string
import unittest
import tempfile
import cryptography
from http.cookiejar import Cookie

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
if sys.version_info <= (3, 0):
    print('Python 2 is vintage. Please use Python 3.')
    sys.exit(1)

from encrypted_cookiejar import EncryptedCookieJar, ParseException

class EncryptedCookieJarTest(unittest.TestCase):

    def test_empty(self):
        cookies = EncryptedCookieJar()
        self.assertEqual(cookies.get('x'), None)
        self.assertEqual(cookies.keys(), [])
        self.assertEqual(str(cookies), '')
        self.assertEqual(cookies, cookies)
        self.assertNotEqual(cookies, None)

    def test_get(self):
        cookies = EncryptedCookieJar()
        for i in range(0, 10):
            c = Cookie(0,
                'test{}'.format(i),
                'value{}'.format(i),
                None,
                False,
               '.example.com',
               True,
               True,
               '/',
               False,
               True,
               None,
               False,
               None,
               None,
               {})
            cookies.set_cookie(c)
        self.assertEqual(cookies.keys(), ['test0', 'test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9'])
        for i in range(0, 10):
            name = 'test{}'.format(i)
            self.assertEqual(cookies[name], cookies.get(name))
        self.assertEqual(str(cookies), 'test0=value0; test1=value1; test2=value2; test3=value3; test4=value4; test5=value5; test6=value6; test7=value7; test8=value8; test9=value9')

    def test_keyerror(self):
        def t():
            cookies = EncryptedCookieJar()
            cookies['x']
        self.assertRaises(KeyError, t)

    def test_file(self):
        cookies1 = EncryptedCookieJar()
        cookies1.load(filename='./tests/cookies1')

        f1 = os.path.join(tempfile.gettempdir(), 'cookies_test1')
        cookies1.save(filename=f1)

        cookies2 = EncryptedCookieJar()
        cookies2.load(filename=f1)
        f2 = os.path.join(tempfile.gettempdir(), 'cookies_test2')
        self.assertEqual(cookies1, cookies2)
        for cookie in cookies1:
            cookie.value = 'X'
        cookies2.save(filename=f2)

        cookies3 = EncryptedCookieJar()
        cookies3.load(filename=f2)
        self.assertEqual(cookies2, cookies3)
        self.assertNotEqual(cookies1, cookies3)

    def test_file_encrypted(self):
        password = ''.join(random.choice(string.printable) for i in range(32))
        cookies1 = EncryptedCookieJar()
        cookies1.load(filename='./tests/cookies1')

        f3 = os.path.join(tempfile.gettempdir(), 'cookies_test3')
        cookies1.save(filename=f3, password=password)

        cookies2 = EncryptedCookieJar()
        cookies2.load(filename=f3, password=password)
        self.assertEqual(cookies1, cookies2)

        def t1():
            cookies = EncryptedCookieJar()
            cookies.load(filename=f3, password='x')
        self.assertRaises(cryptography.fernet.InvalidToken, t1)

        def t2():
            cookies = EncryptedCookieJar()
            cookies.load(filename=f3)
        self.assertRaises(ParseException, t2)

        cookies3 = EncryptedCookieJar(filename='./tests/cookies1.encrypted')
        cookies3.load(password='secure')
        self.assertEqual(cookies1, cookies3)

    def test_missing_filename(self):
        def t1():
            cookies = EncryptedCookieJar()
            cookies.save()
        self.assertRaises(ValueError, t1)
        def t2():
            cookies = EncryptedCookieJar()
            cookies.load()
        self.assertRaises(ValueError, t2)


if __name__ == '__main__':
    unittest.main()

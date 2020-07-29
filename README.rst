python-encrypted-cookiejar
==========================

Fernet-encrypted cookie jar

Installation
------------
::

    pip install encrypted_cookiejar

Usage
-----

::


    from encrypted_securid import EncryptedCookieJar

    cookies = EncryptedCookieJar()
    cookies.load('encrypted_cookie_jar', password=password)
    r = requests.get(url, cookies=cookies)
    cookies.save('encrypted_cookie_jar', password=password)




Links
~~~~~

* `Project home page (GitHub) <https://github.com/andreax79/python-encrypted-securid>`_
* `Documentation (Read the Docs) <https://python-encrypted-securid.readthedocs.io/en/latest/>`_

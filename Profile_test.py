from selenium import selenium
import unittest, time, re

class Profile_test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://abo.ua/")
        self.selenium.start()
    
    def test_profile_test(self):
        sel = self.selenium
        sel.open("/")
        self.assertEqual(u"Интернет магазин гипермаркет Abo.ua. Самый дешевый интернет магазин в Киеве онлайн. Купить в интернет магазине Украины", sel.get_title())
        try: self.failUnless(sel.is_element_present("id=pAoVe4sF4xGWKzvRYYhwmw"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id=pAoVe4sF4xGWKzvRYYhwmw")
        sel.type("id=CK8vAPME4xGpjgbvYIhwmw", "mfedoranych@gmail.com")
        sel.type("id=cOZDJPME4xGTtRPvYIhwmw", "123456")
        sel.wait_for_page_to_load("30000")
        self.assertEqual(u"Интернет магазин гипермаркет Abo.ua. Самый дешевый интернет магазин в Киеве онлайн. Купить в интернет магазине Украины", sel.get_title())
        try: self.failUnless(sel.is_element_present("id=RONxWfYE4xGNRfbxYIhwmw"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id=RONxWfYE4xGNRfbxYIhwmw")
        sel.wait_for_page_to_load("30000")
        self.assertEqual(u"Мой профайл", sel.get_title())
        sel.type("id=vOg6qfYE4xGk3TTyYIhwmw", "Test")
        sel.type("id=JGV60PYE4xG7Do3yYIhwmw", "TestF")
        sel.click("css=a > b")
        sel.click(u"xpath=(//a[contains(text(),'Одесса')])[2]")
        for i in range(60):
            try:
                if sel.is_element_present("id=UpdateUserProfile"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("id=UpdateUserProfile")
        sel.click("id=LUNvgE4xGm8vPzYIhwmw")
        try: self.failUnless(sel.is_element_present("id=ui-id-2"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id=ui-id-2")
        try: self.failUnless(sel.is_element_present("//div[@id='tabs-2']/ul/li/div[2]/a"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//div[@id='tabs-2']/ul/li/div[2]/a[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//div[@id='tabs-2']/ul/li/div[2]/a[3]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("id=ui-id-3"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id=ui-id-3")
        sel.click("id=date")
        sel.select("id=date", "label=3")
        sel.select("id=month", u"label=Июль")
        sel.select("id=year", "label=1992")
        sel.select("id=gender", u"label=женский")
        sel.select("id=maritalStatus", u"label=незамужем")
        sel.click("xpath=(//input[@name='hasChildrens'])[2]")
        sel.click("id=UpdateUserInfo")
        sel.click("id=LUNvgE4xGm8vPzYIhwmw")
        for i in range(60):
            try:
                if sel.is_element_present("id=ui-id-4"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click("id=ui-id-4")
        for i in range(60):
            try:
                if sel.is_element_present(u"link=Выйти"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.click(u"link=Выйти")
        sel.wait_for_page_to_load("30000")
        self.assertEqual(u"Интернет магазин гипермаркет Abo.ua. Самый дешевый интернет магазин в Киеве онлайн. Купить в интернет магазине Украины", sel.get_title())
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

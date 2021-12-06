import json

import jsonpickle


class billingAddress:
    def __init__(self, firstName, last_Name, company_Name, Address, City, ZipCode, Email):
        self.Email = Email
        self.company_Name = company_Name
        self.firstName = firstName
        self.last_Name = last_Name
        self.Address = Address
        self.City = City
        self.ZipCode = ZipCode

    def setFirstName_In_Billing_Address(self):
        return self.firstName

    def setLastName_In_Billing_Address(self):
        return self.last_Name

    def setCompanyName_In_Billing_Address(self):
        return self.company_Name

    def setAddress_In_Billing_Address(self):
        return self.Address

    def setCityName_In_Billing_Address(self):
        return self.City

    def setZipCode_In_Billing_Address(self):
        return self.ZipCode

    def setEmail_In_Billing_Address(self):
        return self.Email


dict = billingAddress("himanshu", "shinde", "abc", "xyz", "California", "94188", "abc@Test.com")

billing_dict = dict.__dict__

with open("MybillingAdress.json", "w") as file:
    json.dump(billing_dict, file, indent=4)

# """Deserializing the JSON"""
# with open("MybillingAdress.json", "r") as file:
#     billing_dict = json.load(file)
#     myBillingAddress = billingAddress(billing_dict['firstName'], billing_dict['last_Name'],
#                                       billing_dict['company_Name'], billing_dict['Address'], billing_dict['City'],
#                                       billing_dict['ZipCode'], billing_dict['Email'])
#
#     billAddressFName = myBillingAddress.setFirstName_In_Billing_Address()
#     billAddressLName = myBillingAddress.setLastName_In_Billing_Address()
#     billAddressCompanyName = myBillingAddress.setCompanyName_In_Billing_Address()
#     billAddressField = myBillingAddress.setAddress_In_Billing_Address()
#     biliAddressCityName = myBillingAddress.setCityName_In_Billing_Address()
#     billingAddressZip = myBillingAddress.setZipCode_In_Billing_Address()
#     billingAddressEmail = myBillingAddress.setEmail_In_Billing_Address()


# serilaize json
# billing_data = json.dumps(billing_dict)
# serilaize json with JSON FILE

# with open("billing.json", "w") as file:
#     file.write(billingAd)
# # # billing_dict = {'firstName': billingA.firstName, 'lastName': billingA.last_Name}
# # # billing_dict = billingA.__dict__
# #
# # deserilize_json = jsonpickle.decode(billingAd)
# #
# #
# # with open("billing.json", "r") as file:
# #     jsonData = file.readline()
# #     billingData = jsonpickle.decode(jsonData)
# #     print(billingData)
# #     # billingData.setFirstName_In_Billing_Address()


# billingAddress

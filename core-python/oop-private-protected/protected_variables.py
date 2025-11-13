class Shape:

    def __init__(self):
        self._color = ''  # protected variable
        self._borderWidth = 0  # protected variable

    def setColor(self, c):
        self._color = c  # setter method

    def getColor(self):
        return self._color  # getter method

    def setBorderWidth(self, bw):
        self._borderWidth = bw  # setter method

    def getBorderWidth(self):
        return self._borderWidth  # getter method


# Test
s = Shape()
s.setColor("Red")
s.setBorderWidth(5)

print("Color:", s.getColor())
print("Border Width:", s.getBorderWidth())

# Accessing the protected variables directly (not recommended, but possible)
print("Protected color directly:", s._color)  # This is allowed but not encouraged










# class Account:
#     def __init__(self):
#         self.__balance = 5000     # Private variable
#         self._accountType = "Saving"  # Protected variable

#     def show(self):
#         print("Balance (Private):", self.__balance)
#         print("Account Type (Protected):", self._accountType)


# class ChildAccount(Account):
#     def display(self):
#         # print(self.__balance)   ❌ Not allowed (Private)
#         print("Accessing protected:", self._accountType)  # ✅ Allowed


# # ---------------- Example Use ----------------
# a = Account()
# a.show()

# child = ChildAccount()
# child.display()

# # Try accessing directly
# # print(a.__balance)   ❌ Error (private)
# print(a._accountType)  # ⚠️ Allowed but not recommended

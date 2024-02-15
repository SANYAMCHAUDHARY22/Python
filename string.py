#python strings
#Strings are amongst the most popular types in Python. We can create them simply by enclosing characters in quotes. Python treats single quotes the same as double quotes. Creating strings is as simple as assigning a value to a variable. For example −

var1 = 'Hello World!'
var2 = "Python Programming"
#Accessing Values in Strings
#Python does not support a character type; these are treated as strings of length one, thus also considered a substring.
#To access substrings, use the square brackets for slicing along with the index or indices to obtain your substring. For example −
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
#Python String replace() Method
#The method replace() returns a copy of the string in which the occurrences of old have been replaced with new, optionally restricting the number of replacements to max.
#Syntax
#Following is the syntax for replace() method −
#str.replace(old, new[, max])
#Parameters
#old − This is old substring to be replaced.
#new − This is new substring, which would replace old substring.
#max − If this optional argument max is given, only the first count occurrences are replaced.
#Return Value
#This method returns a copy of the string with all occurrences of substring old replaced by new. If the optional argument max is given, only the first count occurrences are replaced.
#Example
#The following example shows the usage of replace() method.
str = "this is string example....wow!!! this is really string"
print (str.replace("is", "was"))
print (str.replace("is", "was", 3))

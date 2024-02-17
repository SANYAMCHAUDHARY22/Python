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
#countring the number of occurences of a substring
#The method count() returns the number of occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.
#Syntax
#Following is the syntax for count() method −
#str.count(sub, start= 0,end=len(string))
#Parameters
#sub − This is the substring to be searched.
#start − Search starts from this index. First character starts from 0 index. By default search starts from 0 index.
#end − Search ends from this index. First character starts from 0 index. By default search ends at the last index.
#Return Value
#This method returns the number of occurrences of substring sub in the range [start, end].
#Example
#The following example shows the usage of count() method.
str = "this is string example....wow!!!"
sub = 'i'
print ("str.count('i') : ", str.count(sub))
sub = 'exam'
print ("str.count('exam', 10, 40) : ", str.count(sub,10,40))
#Python String find() Method
#The method find() determines if the string str occurs in string, or in a substring of string if the starting index beg and ending index end are given. This method is same as find(), but raises an exception if sub is not found.
#Syntax

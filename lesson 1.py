firstname = "hao"
lastname = "zhang"
secondNo = 20.0
name = "umkc"

#introduce myself

print('welcome to', name)

print('This is ', firstname, lastname)
# task 1 I used the [::1] this means that it will reverse the input.
stra = input('first name:')

strA = input('last name: ')
strb = stra[::-1]
strc = strA[::-1]
print('', strb, strc)
# task 2 I choose to do the addition operation on two numbers which is taking from user
val1 = input('please input a number: ')
val2 = input('please input another number: ')
sum = int(val1) + int(val2)
print('sum=' + str(sum))
# task 3 I use for sentence to count how many digits and letters in sentence which is getting from user
int_count = 0
str_count = 0
other_count = 0
a = input('please input a string \n')
for i in a:
    if i.isdigit():
        int_count += 1
    elif i.isalpha():
        str_count += 1
    else:
        other_count +=1
print('Letters: %d Digits: %d Others: %d ' %(str_count, int_count, other_count))





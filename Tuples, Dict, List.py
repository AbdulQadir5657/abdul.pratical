#!/usr/bin/env python
# coding: utf-8

# In[3]:


my_list = ['one','two','three',4,5]
my_list[0]


# In[4]:


my_list[1:]


# In[5]:


my_list[:3]


# In[6]:


my_list + ['new item']


# In[7]:


my_list


# In[8]:


my_list = my_list +['add new item permanetly']


# In[9]:


my_list


# In[11]:


my_list * 2


# In[12]:


my_list


# In[13]:


list1 = [1,2,3]


# In[14]:


list1.append('append me!')


# In[15]:


list1


# In[16]:


list1.pop(0)


# In[17]:


list1


# In[23]:


popped_item = list1.pop()


# In[19]:


popped_item


# In[25]:


list1


# In[33]:


new_list = ['a','e','x','b','c']


# In[34]:


new_list


# In[36]:


new_list.reverse()


# In[37]:


new_list


# In[32]:


new_list


# In[39]:


list_1=[1,2,3]
list_2=[4,5,6]
list_3=[7,8,9]

matrix = [list_1,list_2,list_3]


# In[40]:


matrix


# In[41]:


matrix[0]


# In[43]:


matrix[0][0]


# In[44]:


# Dictionaries


# In[45]:


my_dict = {'key1':'value1','key2':'value2'}


# In[46]:


my_dict['key2']


# In[49]:


my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}


# In[50]:


my_dict['key3']


# In[51]:


my_dict['key3'][0]


# In[62]:


my_dict['key3'][0].lower()


# In[53]:


my_dict['key1']


# In[65]:


my_dict['key1'] = my_dict['key1'] * 2


# In[66]:


my_dict['key1']


# In[67]:


my_dict['key1'] -=123
my_dict['key1']


# In[70]:


my_dict = {'car':20,'television':40,'mobile'50}
my_dict


# In[71]:


d = {}


# In[72]:


d['animal'] = 'Dog'


# In[77]:


d = {'key1':{'key1':{'subnestkey':'value'}}}


# In[78]:


d['key1']['nestkey']['subnestkey']


# In[79]:


d = {'key1':1,'key2':2,'key3':3}


# In[80]:


d.keys()


# In[81]:


d.values()


# In[82]:


d.items()


# In[83]:


input = ['fun','foo','Bar']


# In[84]:


# Tuples


# In[85]:


t = (1,2,3)


# In[86]:


len(t)


# In[88]:


t = ('one',2)
t


# In[93]:


t[1]


# In[94]:


t[-1]


# In[95]:


t.index('one')


# In[96]:


t.count('one')


# In[ ]:


#Sets


# In[97]:


x = set()


# In[100]:


x.add(1)


# In[101]:


x


# In[102]:


x.add(2)


# In[103]:


x


# In[104]:


x.add(1)


# In[105]:


x


# In[106]:


list1 = [1,1,2,2,3,4,5,6,1,1]


# In[107]:


set(list1)


# In[108]:


# Boolean


# In[109]:


a = True


# In[110]:


a


# In[111]:


1>2


# In[113]:


b = None


# In[114]:


print(b)


# In[115]:


# If , Else


# In[116]:


if True:
    print('its true')


# In[117]:


x = False

if x:
    print('x was true')
else:
    print('I wrill be printed in any case where x is not true')


# In[123]:


loc = 'Auto Shop'

if loc == 'Auto shop':
    print('welcome to auto shop')
elif loc == 'Bank':
     print('Welcome to Bank!')
else:
    print('where are you?')
    


# In[126]:


person = 'sammy'

if person == 'Sammy':
    print('welcome Sammy')



# In[127]:


# Loops


# In[128]:


list1 = [1,2,3,4,5,6,7,8,9,10]


# In[129]:


for num in list1:
    print(num)


# In[131]:


for num in list1:
    if num % 2 == 0:
        print(num)


# In[133]:


for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('odd number')


# In[135]:


list_sum = 0

for num in list1:
    list_sum = list_sum + num
    
print(list_sum)


# In[138]:


for letter in 'I love a lot':
    print(letter)


# In[139]:


list2 = [(2,4),(6,8),(10,12)]


# In[140]:


for tup in list2:
    print(list2)


# In[141]:


d = {'k1':1,'k2':2,'k3':3}


# In[145]:


for item in d:
    print(item)


# In[146]:


d.items()


# In[148]:


for k,v in d.items():
    print(k)
    print(v)


# In[149]:


list(d.keys())


# In[ ]:





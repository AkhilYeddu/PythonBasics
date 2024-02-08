#slicing= creating a substring by extracting the elements from another string.
#[start:stop:step] 
# start is inclusive and stop is exclusive
#index=[:::]
#slice=(,,,)
name="Akhil Yeddu"
first_name=name[0:5]
print(first_name)
last_name=name[6:]
print(last_name)
funky_name=name[::2]
print(funky_name)
reversed_name=name[::-1]
print(reversed_name)
website1="https://youtube.com"
website2="https://google.com"
slice=slice(8,-4)
print(website1[slice])
print(website2[slice])

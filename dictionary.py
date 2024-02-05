#dictionary= a changeable, unique collection of key:value pairs. They are fast beacuse they use hashing, allows us to access a value very quickly.
#Hashing is the practice of transforming a given key or string of characters into another value for the purpose of security

capitals_state={"Andhra":"Not fixed",
                "Telangana":"Hyderabad",
                "Tamil Nadu":"Chennai",
                "Maharastra":"Mumbai",
                "West Bengal":"Kolkata"
                }
print(type(capitals_state))
print(capitals_state["Tamil Nadu"]) #unsafe way
print(capitals_state.get("Punjab")) #instead,use this
print(capitals_state.keys())
print(capitals_state.items())
print(capitals_state.values())

capitals_state.update({"Karnataka":"Bengaluru"})
capitals_state.pop("Tamil Nadu")

for key,value in capitals_state.items():
    print(key,value)
 
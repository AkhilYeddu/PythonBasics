#kwargs=a parameter which packs all the arguements into a dictionary.Helpful so that a function can call varying amount of keyword arguements.
def hello(**kwargs):
    print("hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")


hello(title="Mr",first="Akhil",middle="kiyo",last="yeddu")
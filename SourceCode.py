from sklearn import tree
# Rough 1
# Smooth 0
# Tennis 1
# Cricket 2

def MarvellousML(weight,surface):
    # Step 1(Get the data for the machine learning application.) & 2(Clean, prepare and manipulate that data.) 
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
        
    Label = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    # Step 3(Decide the machine learning algorithm and train the dataset.)
    dobj = tree.DecisionTreeClassifier()
        
    #Step 4(Test the algorithm with some test dataset.)
    dobj.fit(Features,Label)
        
    #Step 5(Depending on the test result improve the algorithm.)
    result = dobj.predict([[weight,surface]])
    if result == 1:
        print("Your object looks like Tennis ball")
    else:
        print("Your object looks like Cricket ball")
     

def main():
    
    print("------------------------------Supervised Machine Learning------------------------------")
    
    print("Enter weight of object")    
    weight = int(input())
    print("Enter surface type of object")
    surface = input()
    
    if surface.lower() == "rough":
        surface = 1
    elif surface.lower() == "smooth":
        surface = 0
    else:
        print("Invalid  input")
        return

    MarvellousML(weight,surface)
        
if __name__ == "__main__":
    main()

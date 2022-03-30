class Dog:
    def __init__(self,type="dog"):
        self.type=type
        self.next=None


class Cat:
    def __init__(self,type="cat"):
        self.type=type
        self.next=None


class AnimalShelter:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,aniaml):
        "adds an animal to the shelter (only dogs and cats)"
        try:
            if aniaml.type=="dog"or "cat":
                if not self.front:
                    self.rear = aniaml 
                    self.front = aniaml
                else:  
                    self.rear.next = aniaml 
                    self.rear = aniaml
        except:
            raise ValueError("The shelter takes only dogs and cats")


    def dequeue(self,pref):
        """
        returns a dog or a cat bassed on the pref argument 
        else it will return the animal  animal has been waiting in the shelter the longest.
        """
        if self.front==None:
            raise Exception("There is no animals in the shelter")
        if pref!= "dog" and pref!="cat":
            "Stretch Goal"
            temp=self.front
            self.front=self.front.next
            temp.next=None
            return temp.type
        if self.front.type==pref:
            temp=self.front
            self.front=self.front.next
            temp.next=None
            return temp.type
        else:
            temp=self.front
            while temp:
                if temp.next.type==pref:
                    new_temp=temp.next
                    temp.next =new_temp.next
                    print(new_temp.type)
                    return new_temp.type
               
                temp=temp.next
            
    def size(self):
        """
        return an integer with the number of the animals in the shelter
        """
        current_rear=self.rear
        current_front=self.front
        size=0
        while current_front:
            current_front=current_front.next
            size +=1
            if current_rear==current_front:
                size+=1
                break
        print(f"The number of animals in the shelter is {size}")
        return size 

    
    def __str__(self):
        output="first animal --> "
        temp=self.front
        while temp:
            output+=f"{temp.type} --> "
            temp=temp.next
        output+= "None"
        print(output)
        return output

    def is_empty(self):
        "returns a boolean whether the shelter is empty or not "
        print(self.front==None)
        return self.front==None

if __name__=='__main__':
    "enqueue"
    shelter=AnimalShelter()
    cat1=Cat()
    shelter.enqueue(cat1)
    dog2=Dog()
    shelter.enqueue(dog2)
    cat2=Cat()
    shelter.enqueue(cat2)
    dog3=Dog()
    shelter.enqueue(dog3)


    "dequeue"
    # shelter.dequeue("cat")
    # shelter.dequeue("dog")
    # shelter.dequeue("5")
    shelter.dequeue("5")
   
    shelter.size()
    shelter.__str__()
    shelter.is_empty()
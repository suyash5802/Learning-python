class Books:
    count=0
    def __init__(self,title, author):
        self.title=title
        self.author=author
        self.review=[]
    def add_review(self,rev):
        self.review.append(rev)
        Books.count+=1
    
    def show_review(self):
        if not self.review:
            print("No reviews yet.")
        for i in self.review:
            print(i)


b1=Books("horror","abc",)
b1.add_review("ddd")
b1.show_review()



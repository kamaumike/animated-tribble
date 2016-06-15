class NotesApplication(object):
    def __init__(self, author):
        self.author = author
        self.notes = ["This is my chair","This is my desk"]
    
    def create(self, note_content):
        self.notes.append(note_content)
        print(self.notes)
        
    def my_list(self):
        for index, note in enumerate(self.notes):
            print("Note ID: {}".format(index))
            print(note) 
            print(" ")
        print("By Author : {}".format(self.author))
        print(" ")
                          
    def get(self, note_id):
        for note_id in self.notes:
            print(note_id)
            return note_id

    def search(self, search_text):
        print("Showing results for search {}".format(search_text))
        for word in self.notes:
            location = word.find(search_text,0,len(word))
            if location >= 0:
                print("Note ID: {}".format(note_id)) #how to add vertical spaciing
                print("\n")
                print("By Author {}".format(self.author))

    def edit(self, note_id, new_content):
        self.note_id = new_content              
        print(self.note_id)

notes = NotesApplication("Michael")
notes.create("This is my book")
notes.my_list()
notes.get(0)





        



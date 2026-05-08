from pyscript import document

class Classmate:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject

    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.subject}."

classmates_list = []

def classmate(event):
    name_el = document.getElementById("name")
    sec_el = document.getElementById("section")
    sub_el = document.getElementById("subject")

    if name_el.value and sec_el.value and sub_el.value:
        
        new_person = Classmate(name_el.value, sec_el.value, sub_el.value)
        classmates_list.append(new_person)

        container = document.getElementById("listcontainer")
        
        display_item = document.createElement("div")
        
        display_item.className = "classmate-item" 
        display_item.innerText = new_person.introduce()

        container.appendChild(display_item)

        name_el.value = ""
        sec_el.value = ""
        sub_el.value = ""
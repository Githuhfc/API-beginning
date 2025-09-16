from fastapi import FastAPI
app = FastAPI()

contacts = {}


@app.post("/contacts/{contact_id}")
def create_contact(contact_id: int,name: str, phone:str):
    contacts[contact_id] = {"name":name,"phone":phone}
    return {"message":"Contact added","data":
            contacts[contact_id]}



@app.get("/contacts/{contact_id}")
def read_contact(contact_id:int):
    return contacts.get(contact_id,{"error": "Contact not found"})
@app.put("/contacts/{contact_id}")
def update_contact(contact_id:int,name:str,phone:str):
    if contact_id in contacts:
        contacts[contact_id] = {"name": name,"phone":phone}
        return {"message":"Contact updated","data": contacts[contact_id]}
    return {"error":"Contacts not found"}
@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id:int):
    if contact_id in contacts:
        deleted = contacts.pop(contact_id)
        return{"message":"contact deleted","data":deleted}
    return{"error":"Contact not found" }



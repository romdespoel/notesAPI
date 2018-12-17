# notesAPI
#### How to start
First, make sure you've set up your virtual environment how you want it.

Install all the requirements from the requirements file. You can do this easily by using the following command:

`pip install -r requirements.txt`

Start the server with `python api.py`. As it is, this is going to be the Flask default localhost.


#### Sample Note
```
{
    "id": 1,
    "title": "this is a sample note",
    "body": "Here is the body of this note",
    "date": "Mon, 17/12/2018",
    "archived": false
}
```
#### Functionality
- `[hostname]/notes/`
  - **GET**: Returns a list of all the non-archived notes
  - **POST**: With a body containing the "title", and "body" of the note, adds this note to the database


- `[hostname]/notes/[id]`
  - **GET**: Returns note identified by id
  - **DELETE**: Deletes note identified by id
  - **PUT**: Replaces note identified by id with whatever information is in the body of the request


- `[hostname]/archives/[id]`
  - **DELETE**: Archives note identified by id


- `[hostname]/archives/`
  - **GET**: Returns all archived notes


#### Choices
Most of my coding experience is Java or C. I did a project in Python with Flask at the beginning of the term, but felt like I barely scratched the surface of what it had to offer. As such, I thought this would be a good opportunity to get some more Python & Flask in. On top of that, I used the restful extension to Flask to simplify a lot of the process.
I used an sqlAlchemy database because it's also what we considered using for our group project at the start of term (ended up not using databases).

#### What's Next?
I would like to add functionality for multiple users. I'd want people to be able to comment on notes, have different categories to sort notes by, etc... Basically, I'm picturing something like Trello to organise and manage group projects.

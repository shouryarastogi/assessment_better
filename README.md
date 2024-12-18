The project is to built a API using flask which CRUD operations on book and member and also contains the search functionality using author_name

follow the steps to run the program:
1. initialise the virtual enviournment
2. in cmd, write command as: **pip install -r requirements.txt**
3. make sure that port 8080 should not busy else change port in the code
4. use command **python api.py**
this should make the api run over the localhost


As for assumption:
  1. Books data format is:
{
  book_ids : {
  id : value,
  title : value,
  author : value,
  genre : value
  }
}
  2. Member data format is:
{
  member_ids : {
  id : value,
  name : value,
  email : value,
  phone : value
  }
}


from flask import Flask, jsonify, request

books = {}
members = {}

app = Flask(__name__)


@app.route("/books", methods = ["POST"])
def creat_book():
    data = request.get_json()
    book = {
        "id" : len(books)+1,
        "author" : data["author"],
        "title" : data["title"],
        "genre" : data["genre"]
    }
    books[book["id"]] = book
    return jsonify(book), 201

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(list(books.values())), 200

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = books.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    data = request.get_json()
    book.update(data)
    return jsonify(book), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id not in books:
        return jsonify({'message': 'Book not found'}), 404
    del books[book_id]
    return jsonify({'message': 'Book deleted'}), 200


@app.route('/members', methods=['POST']) #for members
def createMember():
    data = request.get_json()
    member = {
        'id': len(members)+1,
        'name': data['name'],
        'email': data['email'],
        'phone': data['phone']
    }
    members[member["id"]] = member
    return jsonify(member), 201

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(list(members.values())), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = members.get(member_id)
    if not member:
        return jsonify({'message': 'Member not found'}), 404
    return jsonify(member), 200

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    member = members.get(member_id)
    if not member:
        return jsonify({'message': 'Member not found'}), 404

    data = request.get_json()
    member.update(data)
    return jsonify(member), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    if member_id not in members:
        return jsonify({'message': 'Member not found'}), 404
    del members[member_id]
    return jsonify({'message': 'Member deleted'}), 200


#for search functionality by author
@app.route('/books/search/<string:author>', methods=['GET'])
def get_books_by_author(author):
    filteredBook = filter(lambda x : x.get("author")==author, list(books.values()))
    return jsonify(list(filteredBook)), 200
if __name__=="__main__":
    app.run(port=8080)
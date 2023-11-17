# 9. Create a RESTful API using Flask to perform CRUD operations on resources like books or movies

from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data as an initial list of books
# books = {'id':[1,2,3],'title':['Ramayan','Mahabharat','Importance of Time'],
#          'author':['Valmiki','Vedvyash','Vijay']}
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"}
]


# CRUD operations

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    new_book["id"] = len(books) + 1
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if book:
        updated_book = request.get_json()
        book.update(updated_book)
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [item for item in books if item["id"] != book_id]
    return jsonify({"message": "Book deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)

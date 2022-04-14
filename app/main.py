from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/')
def hello():

    if request.method == 'POST':
        return "post method on /"
    else:
        return "hello"

@app.route('/bfhl', methods=['POST'])
def bfhl():
    # if request.method == 'POST':
    input = request.get_json()
    # input = request.form
    print(input)
    numbers = input['numbers']
    # numbers=[1,2,3,4,5,6,"3",4]
    # test(numbers)
    odd = []
    even = []
    is_success = True
    for i in numbers:
        try:
            if int(i) % 2 == 0:
                even.append(int(i))
            else:
                odd.append(int(i))
        except:
            is_success = False
            # print("failed")
            return jsonify(is_success = str(is_success).lower(), user_id = "sarthak_vinchurkar_08082002")
            # return jsonify({"is_success": str(is_success).lower(), "user_id": "sarthak_vinchurkar_08082002"})

    # print("printing jsonified doc")
    return jsonify(is_success = str(is_success).lower(), user_id = "sarthak_vinchurkar_08082002", odd = odd, even = even)

@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "Modules" : 15,
            "Subject" : "Data Structures and Algorithms",
        }
  
        return jsonify(data)

# app.run()

# def test(numbers):
#     odd = []
#     even = []
#     dicct = {}
#     is_success = True
#     for i in numbers:
#         try:
#             if int(i) % 2 == 0:
#                 even.append(int(i))
#             else:
#                 odd.append(int(i))
#         except:
#             is_success = False
#             break
#     dicct['is_success'] = str(is_success).lower()
#     dicct['user_id'] = 'sarthak_vinchurkar_08082002'

#     if(is_success):
#         dicct["odd"] = odd
#         dicct['even'] = even
#     return dicct

# pprint(test([1,2,3,4,5,6,"3",4]))
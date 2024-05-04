import requests


paramters = {
    'amount': 10,
    'type': "boolean",
    'category': 18,
}

response = requests.get("https://opentdb.com/api.php", params=paramters)
response.raise_for_status()
data = response.json()
question_data = data["results"]


# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The first computer bug was formed by faulty wires.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },

# ]

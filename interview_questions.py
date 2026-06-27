def generate_questions(skills):

    questions = {

        "Python": [
            "What is the difference between list and tuple?",
            "Explain decorators in Python.",
            "What is a generator in Python?"
        ],

        "SQL": [
            "What is the difference between DELETE, DROP and TRUNCATE?",
            "Explain different types of JOINs.",
            "What is normalization?"
        ],

        "HTML": [
            "What are semantic HTML tags?",
            "Difference between id and class?",
            "What is the purpose of the DOCTYPE declaration?"
        ],

        "CSS": [
            "Difference between Flexbox and Grid?",
            "What is the CSS Box Model?",
            "How does position:absolute work?"
        ],

        "MongoDB": [
            "What is MongoDB?",
            "Difference between SQL and MongoDB?"
        ],

        "Git": [
            "What is Git?",
            "Difference between git pull and git fetch?"
        ],

        "GitHub": [
            "What is GitHub?",
            "How do you resolve merge conflicts?"
        ],

        "NumPy": [
            "Why is NumPy faster than Python lists?"
        ],

        "Pandas": [
            "Difference between Series and DataFrame?"
        ],

        "Data Structures": [
            "Explain Stack and Queue.",
            "Difference between Array and Linked List?"
        ],

        "DBMS": [
            "Explain ACID properties.",
            "What is a Primary Key?"
        ],

        "OOP": [
            "What are the four pillars of OOP?",
            "Difference between abstraction and encapsulation?"
        ]

    }

    interview_questions = {}

    for skill in skills:

        if skill in questions:

            interview_questions[skill] = questions[skill]

    return interview_questions
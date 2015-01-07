"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": "A2,B1",
            "answer": 12,
        },
        {
            "input": "A1,A1,A1",
            "answer": 3,
        },
        {
            "input": "Z9,X8,Y7",
            "answer": 672,
        },
        {
            "input": "C1,D1,B1,E1,F1",
            "answer": 140,
        },
    ],
    "Extra": [
        {
            "input": "A1",
            "answer": 1,
        },
        {
            "input": "Z9",
            "answer": 234,
        },
        {
            "input": "K5",
            "answer": 95,
        },
        {
            "input": "A1,A1,A1,A1,A1,A1,A1,A1,A1,A1",
            "answer": 10,
        },
        {
            "input": "Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9,Z9",
            "answer": 6084,
        },
        {
            "input": "A1,B2,C3,D4,E5,F6,G7,H8,I9,J1,K2,L3,M4,N5,O6,P7,Q8,R9,S1,T2,U3,V4,W5,X6,Y7,Z8",
            "answer": 3051,
        },
        {
            "input": "Z8,Y7,X6,W5,V4,U3,T2,S1,R9,Q8,P7,O6,N5,M4,L3,K2,J1,I9,H8,G7,F6,E5,D4,C3,B2,A1",
            "answer": 3051,
        },
        {
            "input": "U7,E6,K3,Q3,G1,K6,I5,M1,L2,V1,O5,U6,U9,M4,R2,X6,E8,R4,M5,Q9,X1,D4,X7,T2,J9,M8",
            "answer": 3382,
        },
        {
            "input": "T9,A8,L6,V8,Q2,X7,R6,N5,D8,F6,Q7,C2,U3,B7,V5",
            "answer": 1781,
        },
        {
            "input": "C8,I2,C5,Y4,V3,T7,G2,O3,Q2,L7,Q2,N8,M9,X4",
            "answer": 1749,
        },
        {
            "input": "B5,O6,C2,E5,N5,T7,X8,L2,U7",
            "answer": 1010,
        },
    ]
}

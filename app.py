from flask import Flask, send_from_directory,render_template, request
import random
import os

app = Flask(__name__, static_folder='.')

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



questions = [["Which data structure uses LIFO (Last In, First Out) ordering?","Queue","Stack","Linked List","Tree",2],["What is the time complexity of searching for an element in a balanced binary search tree (BST)?","O(1)","O(log n)","O(n)","O(n log n)",2],["Which sorting algorithm has the best average-case time complexity?","Bubble Sort","Selection Sort","Quick Sort","Insertion Sort",3],["What does a hash function do in a hash table?","Sorts data","Searches for data","Maps a key to an index","Merges data",3],["Which traversal of a binary tree processes the root before its subtrees?","Inorder", "Preorder","Postorder","Level-order",2],["Which of the following data structures is most suitable for implementing recursion?","Stack","Queue","Array","Linked List",1],["What is the worst-case time complexity of Quick Sort?","O(n log n)","O(log n)","O(n)","O(n²)",4],["In a min-heap, what is the relation between a parent node and its children?",
"Parent ≥ Children","Parent ≤ Children","Parent = Children","No relation",2],["Which graph traversal uses a queue and visits nodes level by level?","DFS","BFS","Dijkstra","Bellman-Ford",2],["What is the time complexity to insert an element into a binary search tree (average case)?","O(n)", "O(n log n)", "O(log n)", "O(1)",3],["Which of the following is not a stable sorting algorithm?","Merge Sort", "Insertion Sort", "Quick Sort", "Bubble Sort",3],["Which data structure is used in the implementation of a priority queue?","Stack","Array","Heap","Linked List",3],["In a graph, which algorithm guarantees the shortest path from a single source to all other vertices (no negative weights)?","BFS", "DFS", "Dijkstra", "Kruskal",3],["Which of the following problems can be solved using the sliding window technique?","Shortest Path", "Maximum Subarray Sum", "Graph Coloring", "Topological Sorting",2]]

#Rules of the game

correct_rules = [
    "You gain 1 XP! +1 towards becoming a 1337 coder!",
    "You unlock a coffee voucher — because good code deserves caffeine ☕.",
    "You’re now eligible to fix one production bug... blindfolded! 🐞",
    "Earn a badge: ‘Bug Smasher Level 1’",
    "Prize amount of 1lakh will be in your account by today !"
]

incorrect_rules = [
    "Do 10 push-ups or debug someone else's code. 🏋️‍♂️",
    "Write one line of code without using Stack Overflow. 😱",
    "You must explain Big-O to the next person who walks in. 📈",
    "Get a sticker that says: ‘I tried to binary search a linked list.’",
    "Lose 1 XP. Go back and study trees 🌳."
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        feedback = []
        for i, q in enumerate(questions):
            user_ans = int(request.form.get(f'q{i}', -1))
            correct = q[5]
            if user_ans == correct:
                feedback.append(("✅ Correct!", random.choice(correct_rules)))
                score += 1
            else:
                feedback.append(("❌ Incorrect!", random.choice(incorrect_rules)))
        return render_template("result.html", score=score, total=len(questions), feedback=feedback)
    return render_template("quiz.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)

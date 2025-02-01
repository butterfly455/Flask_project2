from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []
completed_tasks = []
trash = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks, completed_tasks=completed_tasks, trash=trash)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task.strip():  # Prevent empty tasks
        tasks.append(task)
    return redirect(url_for('home'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        completed_tasks.append(tasks.pop(task_id))
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        trash.append(tasks.pop(task_id))
    return redirect(url_for('home'))

@app.route('/restore/<int:task_id>')
def restore_task(task_id):
    if 0 <= task_id < len(trash):
        tasks.append(trash.pop(task_id))
    return redirect(url_for('home'))

@app.route('/clear_trash')
def clear_trash():
    trash.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
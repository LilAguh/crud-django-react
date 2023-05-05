export function TaskCard(tasks) {

    const task = tasks.task

    return (
            <div>
                <h2>{task.title}</h2>
                <p>{task.description}</p>
                <input type="checkbox" name={task.id} id={task.id} checked={task.done} />
                <hr/>
            </div>
    )
}


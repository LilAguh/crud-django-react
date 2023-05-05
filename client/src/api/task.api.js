import axios from 'axios'

export const getAllTask = () => {

    const url = 'http://localhost:8000/api/v1/task/'
    return (
        axios.get(url)
        .then(response => response.data)
    )
}
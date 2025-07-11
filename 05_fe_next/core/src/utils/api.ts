import axios from 'axios'

const instance = axios.create({
  baseURL: 'http://localhost:8000/api/v1', // Update as per your FastAPI backend
  headers: {
    Accept: 'application/json'
  }
})

export default instance

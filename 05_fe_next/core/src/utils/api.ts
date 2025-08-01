import axios from 'axios'

const baseUrl = "http://localhost:1234/api/v1"
// const baseUrl = "https://70d331400278.ngrok-free.app/api/v1"

const instance = axios.create({
  baseURL: baseUrl, // Update as per your FastAPI backend
  headers: {
    Accept: 'application/json'
  }
})

export default instance

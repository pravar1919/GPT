import { Link } from 'react-router-dom'

const Home = () => {
  return (
    <>
        <Link to="/app">App</Link>
        <Link to="/users">Users</Link>
    </>
  )
}

export default Home
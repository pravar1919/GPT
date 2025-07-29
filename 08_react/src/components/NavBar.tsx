import { Link } from "react-router-dom"

const NavBar = () => {
  return (
    <nav>
        <ul>
            <li><Link to="/">Navbar</Link></li>
            <li><Link to="/app">App</ Link></li>
            <li><Link to="/users">Users</ Link></li>
        </ul>
    </nav>
  ) 
}

export default NavBar
import { createBrowserRouter } from "react-router-dom";
import Home from "../Home";
import App from "../App";
import User from "../components/User";
import UserDetail from "../components/UserDetail";

const router = createBrowserRouter([
    {path:"/", element: <Home />},
    {path:"/app", element: <App />},
    {path:"/users/", element: <User />},
    {path:"/users/:id", element: <UserDetail />},
])

export default router;
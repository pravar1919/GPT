import { createBrowserRouter } from "react-router-dom";
import Home from "../Home";
import App from "../App";
import User from "../components/User";
import UserDetail from "../components/UserDetail";
import Layout from "./Layout";
import ErrorPage from "../components/ErrorPage";
import LoginPage from "../pages/LoginPage";
import PrivateRoutes from "./PrivateRoutes";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    errorElement: <ErrorPage />,
    children: [
      { path: "", element: <Home /> },
      { path: "app", element: <App /> },
      { path: "login", element: <LoginPage /> },
      {
        element: <PrivateRoutes />,
        children: [
          {
            path: "users/",
            element: <User />,
            children: [{ path: ":id", element: <UserDetail /> }],
          },
        ],
      },
    ],
  },
]);

export default router;

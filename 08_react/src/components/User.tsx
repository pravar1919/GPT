import { Link } from "react-router-dom";

const User = () => {
  const users = [
    { id: 1, name: "Pravar" },
    { id: 2, name: "Vini" },
    { id: 3, name: "Mukul" },
  ];
  return (
    <>
      <div>User</div>
      {users.map((user) => (
        <li key={user.id}>
          <Link to={`/users/${user.id}`}>{user.name}</Link>
        </li>
      ))}
    </>
  );
};

export default User;

import { Link } from "react-router-dom";
import ExpenseForm from "./components/ExpenseForm";
import ExpenseTable from "./components/ExpenseTable";

function App() {
  return (
    <div className="container">
      <Link to="/">Home</Link>
      <ExpenseForm />
      <ExpenseTable />
    </div>
  );
}

export default App;

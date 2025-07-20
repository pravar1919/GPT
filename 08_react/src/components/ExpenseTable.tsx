import { useState, type ChangeEvent } from "react";
import SelectInput from "./SelectInput";

const ExpenseTable = () => {
  const [categories, setCategories] = useState("");
  const [expenseData, setExpenseData] = useState([
    { description: "Eggs", amount: 10, category: "Groceries" },
    { description: "Milk", amount: 11, category: "Groceries" },
    { description: "Movies", amount: 32, category: "Entertainment" },
    { description: "Electricity", amount: 12, category: "Utilities" },
  ])
    const handleDelete = (des: string) =>{
        setExpenseData(expenseData.filter(e => e.description !== des))
    }
    let filteredData = expenseData.filter((d) =>
        categories === "" ? true : d.category === categories
    );
  const total = filteredData.reduce((acc, item) => acc + item.amount, 0);


  return (
    <>
      <SelectInput
        id=""
        onChange={(event: ChangeEvent<HTMLSelectElement>) =>
          setCategories(event.target.value)
        }
      />
      <table className="table">
        <thead>
          <tr>
            <th scope="col">Description</th>
            <th scope="col">Amount</th>
            <th scope="col">Category</th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          {filteredData.map((d) => (
            <tr key={d.description}>
              <td>{d.description}</td>
              <td>${d.amount}</td>
              <td>{d.category}</td>
              <td>
                <button onClick={()=>handleDelete(d.description)} className="btn btn-danger">Delete</button>
              </td>
            </tr>
          ))}
          <tr>
            <td>Total</td>
            <td colSpan={3}>${total}</td>
          </tr>
        </tbody>
      </table>
    </>
  );
};

export default ExpenseTable;

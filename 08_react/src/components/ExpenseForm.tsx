
import SelectInput from './SelectInput'

const ExpenseForm = () => {
  return (
    <form className='mb-5'>
        <div className="mb-3">
            <label htmlFor="description" className="form-label">Description</label>
            <input type="text" className="form-control" id="description" />
        </div>
        <div className="mb-3">
            <label htmlFor="amount" className="form-label">Amount</label>
            <input type="number" className="form-control" id="amount" />
        </div>
        <div className="mb-3">
            <label htmlFor="category" className="form-label">Category</label>
            <SelectInput id={"category"} />
        </div>
        <button type="submit" className="btn btn-primary">Submit</button>
        </form>
  )
}

export default ExpenseForm
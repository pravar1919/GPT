
import { type ChangeEvent } from 'react'

interface Props{
    id: string
    onChange?: (event: ChangeEvent<HTMLSelectElement>)=>void
}

const SelectInput = ({id, onChange }:Props) => {
  const values = ["Groceries", "Utilities", "Entertainment"] as const;
  return (
    <select onChange={onChange} className="form-select mb-2" id={id}>
        <option defaultValue=""></option>
        {values.map(value=><option key={value} defaultValue={value}>{value}</option>)}
    </select>
  )
}

export default SelectInput
import Button from "./Button"

interface Props{
    onClose: ()=>void;
}

const Alert = ({onClose}: Props) => {
  return (
    <>
    <div>This is an alert.</div>
    <Button onClick={onClose}>Close</Button>
    </>
  )
}

export default Alert
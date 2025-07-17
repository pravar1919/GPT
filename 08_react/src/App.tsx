import { useState } from "react";
import Button from "./components/Button"
import Alert from "./components/Alert";

function App() {
  const [visible, setVisible] = useState(false)

  return (
    <>
    {visible && <Alert onClose={()=>setVisible(false)}/>}
    <Button onClick={()=>setVisible(true)}>My Button</Button>
    </>
  )
}

export default App

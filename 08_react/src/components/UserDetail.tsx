import { useParams, useSearchParams } from "react-router-dom"


const UserDetail = () => {
    const params = useParams()
    const [searchParams, setSearchParams] = useSearchParams()
    console.log(params);
    console.log(searchParams.toString());
    console.log(searchParams.get("filter_id"));
    
  return (
    <div>UserDetail - {params.id}</div>
  )
}

export default UserDetail
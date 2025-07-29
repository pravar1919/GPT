import { useLocation, useParams, useSearchParams } from "react-router-dom"


const UserDetail = () => {
    const params = useParams()
    const [searchParams, setSearchParams] = useSearchParams()
    const location = useLocation()
    console.log(params);
    console.log(searchParams.toString());
    console.log(searchParams.get("filter_id"));
    console.log(location);
    
    
  return (
    <div>UserDetail - {params.id}</div>
  )
}

export default UserDetail
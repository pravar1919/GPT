"use client"
import { signOut, useSession } from "next-auth/react";
import { getToken } from "next-auth/jwt"


export default function Home() {
  const {status, data} = useSession()
  
  return (
    <>
    <div>
      {status}
      <p>{data?.user?.email}</p>
      <p>{JSON.stringify(data)}</p>
        <button className="cursor-pointer" onClick={()=>signOut()}>Logout</button>
    </div>
      </>
  );
}

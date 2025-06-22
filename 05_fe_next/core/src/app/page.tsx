import { getServerSession } from "next-auth"
import { authOptions } from "./api/auth/[...nextauth]/route"
import ResumeJDUploader from "@/components/ResumeJDUploader"
import { redirect } from "next/navigation"


export default async function HomePage() {
  const session = await getServerSession(authOptions)

  if (!session){
    redirect("/auth")
  }

  return (
    <>
      <div className="p-10">
        <ResumeJDUploader />
      </div>
    </>
  )
}

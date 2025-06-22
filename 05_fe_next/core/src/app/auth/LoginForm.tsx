'use client'
import { signIn } from "next-auth/react"

export default function LoginForm() {
  return (
    <div className="flex items-center justify-center min-h-screen">
      <div className="p-10 text-center">
        <h2 className="text-xl mb-4">Login</h2>
        <button
          onClick={() => signIn("google")}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Sign in with Google
        </button>
      </div>
    </div>
  )
}

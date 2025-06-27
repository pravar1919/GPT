'use client'

import { signOut } from 'next-auth/react'

export default function LogoutButton() {
  return (
    <button
      onClick={() => signOut({ callbackUrl: '/auth' })}
      className="bg-red-500 text-white px-4 rounded"
    >
      Logout
    </button>
  )
}

'use client'

import { signOut } from 'next-auth/react'

export default function LogoutButton() {
  return (
    <button
      onClick={() => signOut({ callbackUrl: '/auth' })}
      className="bg-red-500 text-white px-4 py-2 rounded mt-4"
    >
      Logout
    </button>
  )
}

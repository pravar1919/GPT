'use client';
import Link from 'next/link'
import LogoutButton from '../app/auth/LogoutButton';
import { useSession } from 'next-auth/react';

export default function Navbar() {
  const {status, data: session} = useSession()
  console.log(status, session);
  
  return (
    <nav className="w-full flex justify-between items-center px-6 py-4 shadow bg-dark shadow-blue-500/50">
      <Link href="/" className="text-xl font-semibold">Resume Matcher</Link>

      <div className="flex items-center space-x-4">
        {status === 'loading' && <span>Loading...</span>}
        {session?.user ? (
          <>
            <span className="text-gray-700">{session.user.name}</span>
            {session.user.image && (
              <img src={session.user.image} alt="Profile" className="w-8 h-8 rounded-full" />
            )}
            <LogoutButton />
          </>
        ) : (
          <>
            <Link href="/auth" className="text-blue-500 hover:underline">Login/Signup</Link>
          </>
        )}
      </div>
    </nav>
  )
}

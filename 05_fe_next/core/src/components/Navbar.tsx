import Link from 'next/link'
import { getServerSession } from 'next-auth'
import { authOptions } from '@/app/api/auth/[...nextauth]/route'
import LogoutButton from '../app/auth/LogoutButton';

export default async function Navbar() {
  const session = await getServerSession(authOptions)

  return (
    <nav className="w-full flex justify-between items-center px-6 py-4 shadow bg-dark shadow-blue-500/50">
      <Link href="/" className="text-xl font-semibold">Resume Matcher</Link>

      <div className="flex items-center space-x-4">
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

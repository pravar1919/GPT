// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
import { getToken } from 'next-auth/jwt';

export async function middleware(request: NextRequest) {
  const token = await getToken({ req: request, secret: process.env.NEXTAUTH_SECRET });
    console.log(token, ">>>>>>>>>>>>");
    
  if (!token) {
    // Redirect to login if token is not present
    return NextResponse.redirect(new URL('/auth/signin', request.url));
  }

  // If token is valid, continue
  return NextResponse.next();
}

// Optional: Apply middleware only to specific routes
export const config = {
  matcher: ['/'], // Protect these routes
};

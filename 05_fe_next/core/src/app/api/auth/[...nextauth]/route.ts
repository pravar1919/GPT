// app/api/auth/[...nextauth]/route.ts
import axios from "@/utils/api"
import NextAuth from "next-auth"
import GoogleProvider from "next-auth/providers/google"

export const authOptions = {
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    }),
  ],
  secret: process.env.NEXTAUTH_SECRET,
  callbacks: {
    async signIn({ user, account, profile }) {
      try {
        // Send user data to FastAPI
        await axios.post('/auth/save-user', {
          name: user.name,
          email: user.email,
          image: user.image
        })
      } catch (error) {
        console.error('Error sending user to backend:', error)
      }
      return true
    }
  }
}

const handler = NextAuth(authOptions)

export { handler as GET, handler as POST }


import CredentialsProvider from "next-auth/providers/credentials"

import NextAuth from "next-auth"
import { AuthOptions } from 'next-auth';
import axios from "axios";


interface UserResponseAPI{
    id: number,
    email: string,
    name: string
}

interface APIResponse {
    access: string,
    refresh: string
    user: UserResponseAPI
    access_token_expiry: string
}

export const authOptions: AuthOptions = {
    session: {
        strategy: "jwt"
    },
    providers: [
        CredentialsProvider({
            name: 'Credentials',
            credentials: {
                email: { label: 'Email', type: 'text' },
                password: { label: 'Password', type: 'password' },
            },
            async authorize(credentials, req) {
                if (!credentials) return null;
                const url = "http://localhost:8000/api/token/"
                 try {
                    const response = await axios.post<APIResponse>(url, {
                        email: credentials.email,
                        password: credentials.password
                    })
                    console.log(")))))))))", await response.data)
                    const data = response.data
                    console.log(data, ">>>>>>")
                    return {
                        id: String(data.user.id), // this is the mandatory field and has to be string.
                        email: data.user.email,
                        name: data.user.name,
                        access: data.access,
                        refresh: data.refresh,
                        expiry: data.access_token_expiry
                    }
                 } catch (error) {
                    if (axios.isAxiosError(error)) {
                        const message =
                        error.response?.data?.detail ||
                        error.response?.data?.message ||
                        "Invalid credentials";
                        throw new Error(message);
                    }

                    throw new Error("Unexpected error during authentication");
                 }

            } 
        })
    ],
    callbacks: {
        async jwt({token, user}){
            if (user){
                token.id = user.id;
                token.name = user.name;
                token.email = user.email;
                token.access = user.access;
                token.refresh = user.refresh;
                token.expiry = user.expiry;
            }
            return token
        },
        async session({ token, session }) {
            session.user = session.user || {};

            session.user.id = token.id as string;
            session.user.name = token.name;
            session.user.email = token.email;

            session.access = token.access;
            session.refresh = token.refresh;

            return session;
        }

    }
}

const handler = NextAuth(authOptions)

export { handler as GET, handler as POST }
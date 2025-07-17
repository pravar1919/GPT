import { NextRequest } from "next/server";
import { getToken } from "next-auth/jwt";


export default async function GET(request: NextRequest){
    const token = await getToken({ req: request, secret: process.env.NEXTAUTH_SECRET });
    
}
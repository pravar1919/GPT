// types/next-auth.d.ts
import NextAuth from "next-auth";
import { JWT } from "next-auth/jwt";

declare module "next-auth" {
  interface Session {
    access?: string;
    refresh?: string;
    user: {
      id: string;
      name?: string | null;
      email?: string | null;
    };
  }

  interface User {
    id: string;
    email: string;
    name: string;
    access: string;
    refresh: string;
    expiry: string;
  }
}

declare module "next-auth/jwt" {
  interface JWT {
    id?: string;
    name?: string;
    email?: string;
    access?: string;
    refresh?: string;
    expiry?: string;
  }
}
